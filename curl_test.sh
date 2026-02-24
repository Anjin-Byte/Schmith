#!/usr/bin/env bash
set -euo pipefail

# Auto-load local env files when present.
for f in ".env" ".env.local"; do
  if [ -f "$f" ]; then
    set -a
    # shellcheck disable=SC1090
    . "$f"
    set +a
  fi
done

BASE_URL="${BASE_URL:-https://api.procore.com}"
PROJECT_ID="${PROJECT_ID:-2htJhdxcSUsdHMeocn2dQXsNR_n3db7v_x1ozo8sCDM}"
ACCESS_TOKEN="${ACCESS_TOKEN:-oTHcOvmQcaA2NvY-EXsDL4WglMh2GxHISo3BJEvxmPs}"
CLIENT_ID="${PROCORE_CLIENT_ID:-${CLIENT_ID:-}}"
CLIENT_SECRET="${PROCORE_CLIENT_SECRET:-${CLIENT_SECRET:-}}"
REFRESH_TOKEN="${PROCORE_REFRESH_TOKEN:-${REFRESH_TOKEN:-}}"

URL="${BASE_URL}/rest/v1.0/projects/${PROJECT_ID}/timesheets"
TOKEN_URL="https://login.procore.com/oauth/token"

TMP_BODY="$(mktemp)"
TMP_HEADERS="$(mktemp)"
trap 'rm -f "$TMP_BODY" "$TMP_HEADERS"' EXIT

print_response() {
  local label="$1"
  local http_code="$2"
  echo "$label"
  echo "URL: $URL"
  echo "HTTP: $http_code"
  echo
  echo "Headers:"
  cat "$TMP_HEADERS"
  echo
  echo "Body:"
  if [ -s "$TMP_BODY" ]; then
    cat "$TMP_BODY"
    echo
  else
    echo "(empty body)"
  fi
  echo
}

call_timesheets() {
  curl -sS \
    -o "$TMP_BODY" \
    -D "$TMP_HEADERS" \
    -w "%{http_code}" \
    -X GET "$URL" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Accept: application/json"
}

refresh_access_token() {
  if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ] || [ -z "$REFRESH_TOKEN" ]; then
    echo "Cannot refresh token automatically. Set PROCORE_CLIENT_ID/CLIENT_ID, PROCORE_CLIENT_SECRET/CLIENT_SECRET, and PROCORE_REFRESH_TOKEN/REFRESH_TOKEN." >&2
    return 1
  fi

  local refresh_json
  refresh_json="$(
    curl -sS \
      -X POST "$TOKEN_URL" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      --data-urlencode "grant_type=refresh_token" \
      --data-urlencode "client_id=$CLIENT_ID" \
      --data-urlencode "client_secret=$CLIENT_SECRET" \
      --data-urlencode "refresh_token=$REFRESH_TOKEN"
  )"

  local new_access_token new_refresh_token
  new_access_token="$(
    python3 -c 'import json,sys; print((json.loads(sys.stdin.read()).get("access_token") or "").strip())' <<< "$refresh_json"
  )"
  new_refresh_token="$(
    python3 -c 'import json,sys; print((json.loads(sys.stdin.read()).get("refresh_token") or "").strip())' <<< "$refresh_json"
  )"

  if [ -z "$new_access_token" ]; then
    echo "Token refresh failed; response was:" >&2
    echo "$refresh_json" >&2
    return 1
  fi

  ACCESS_TOKEN="$new_access_token"
  if [ -n "$new_refresh_token" ]; then
    REFRESH_TOKEN="$new_refresh_token"
  fi

  echo "Access token refreshed successfully."
}

HTTP_CODE="$(call_timesheets)"
print_response "Initial request:" "$HTTP_CODE"

if [ "$HTTP_CODE" = "401" ]; then
  echo "Received 401. Attempting token refresh..."
  refresh_access_token
  HTTP_CODE="$(call_timesheets)"
  print_response "Retry after refresh:" "$HTTP_CODE"
fi
