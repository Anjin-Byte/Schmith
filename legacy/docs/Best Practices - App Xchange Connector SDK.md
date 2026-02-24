# Connector Best Practices and Approval Criteria

App Xchange code approval focuses on safety and avoiding security and performance risks, not optimization or design. It is typically the connector builder's responsibility to do quality assurance on their connector and confirm that the connector design supports their business requirements, including taking any [pre-development considerations](https://help.trimble.com/en/app-xchange/app-xchange/connectivity/build-a-connector/pre-development-considerations) into account.

Connectors that do not meet minimum criteria will not be deployed to the platform, and connectors that do not follow best practices will receive feedback and require specific reasoning before deployment.

### How to use these criteria

- Connectors that do not meet the "mandatory" criteria will not be released or may be withdrawn from production

- Connectors that do not meet the "prefer" criteria will receive feedback and guidance before approval

  - We will typically ask for an explanation if not provided if these criteria are not followed

## Criteria

### MANDATORY

- If the connector is intended to be public, confirm with App Xchange any change to the connector name or description in the settings.json file.

- [Limit network calls in a connector to the connecting system](#limit-network-calls-in-a-connector-to-the-connecting-system)

- Only communicate with the external system it connects to and can only connect to a single external system

- Scope cache access to the connector (cannot request data from other connectors)

- Pass all security scans and checks

- Do not use `Console.WriteLine` or similar logging to standard output. `ILogger` must be used. For more information on logging best practices, refer to the [local testing guide](../local-testing/#logging)

- Provide action outcomes and handle exceptions for action handlers

- Log out events when appropriate for troubleshooting. Use different log levels as [appropriate](../local-testing/#logging-best-practices) (Information, Warning, Error, etc.)

- Use NuGet package management for dependencies

- [Not use conditional compilation preprocessor directives](#not-use-conditional-compilation-preprocessor-directives)

- [Not include credentials or sensitive information within connector code](#not-include-credentials-or-sensitive-information-within-connector-code) (Note that testSettings.json is ignored during code submission)

- Not log sensitive data such as objects with sensitive properties, tokens, secrets, credentials etc.

- [Mark all Personally Identifiable Information (PII) and financially sensitive information with the "WriteOnly" attribute.](#mark-all-personally-identifiable-information-pii-and-financially-sensitive-information-with-the-writeonly-attribute)

- [Not introduce breaking schema changes for existing connectors without a migration or versioning plan for dependent integrations](#not-introduce-breaking-schema-changes-for-existing-connectors-without-a-migration-or-versioning-plan-for-dependent-integrations)

- Not mix Newtonsoft and System.Text.Json Library Usage

- Be proactive with exception handling, such as catching JSON deserialization exceptions or confirming a successful response before attempting to deserialize

- Do not read from files or environment variables

### PREFER

- Use the latest SDK at the time of approval

- Use PascalCase for names and follow [naming conventions](https://trimble-xchange.github.io/connector-docs/guides/object-schema/#metadata-attributes)

- [Limit dependencies on additional third party libraries](#limit-dependencies-on-additional-third-party-libraries)

- Favor .NET and Xchange libraries over unsupported third-party libraries for equivalent function, e.g. prefer `System.Text.Json` over `NewtonSoft.Json`

- Use cancellation token support when applicable within action handlers and data readers

- Avoid mixing JSON serialization libraries

- Use public NuGet repositories for additional dependencies

- Use `StandardActionFailure` types for failed action outcomes

- Handle and inform service runners of exception cases

- Limit source files to those needed for operating the connector

- Aggregate related errors when appropriate - e.g. based on a previous response, handle recovery, failure and next steps

- Use base `Config` types when extending service configurations

- Use configurations from the host context rather than custom configuration strategies

- Represent a reasonably stable API, i.e. version or modules are not expected to change frequently

- [Compile without warnings](#compile-without-warnings)

- Descriptions are provided for all data objects and actions

### CONSIDER USING

- Asynchronous iterators for data reader implementations

- Supported API clients, middleware, and delegating handlers

- Action and Data Object names which follow connecting API resource naming conventions

- Validation on Action inputs

- Data object definitions which are generally less restrictive than action input validations

---

## Examples and additional guidance

The examples and guidance provided assume the connector code uses organization concepts encouraged by the SDK tooling, i.e. CLI code generation commands.

#### Limit network calls in a connector to the connecting system

- Most network calls should be limited to provided `ApiClient` classes to leverage middleware, i.e. connections, authentication, retry policies, etc.

- Do not use `HttpClient` classes, hardcoded URLs, or other libraries that make network requests invoked within data readers or action handlers.

- Verify that `ApiClient` classes use injected `HttpClient` classes and connection details from configurations.

- Do not instantiate new http objects - a new HttpClient would not use the pooling HttpMessageHandler that would get used by injected HttpClients. Creating many HttpMessageHandlers can result in socket exhaustion and DNS issues.

```
// Connector.Client.ApiClient.cs - Good usage of connection details from configuration
...
 public ApiClient(HttpClient httpClient, ConnectorRegistrationConfig registrationConfig)
 {
 _httpClient = httpClient;
 _httpClient.BaseAddress = new System.Uri(registrationConfig.ApiDetails.BaseUrl);
 }
...
```

#### Not use conditional compilation preprocessor directives

Conditional preprocessor directives are often used for environment or configuration conditions. We support configuration from the App Xchange app and local testing cases.

#### Not include credentials or sensitive information within connector code

Connections, Connector Registrations, any API client pipeline code, should not have credentials in the connector code. Sensitive credentials should be marked as such and loaded from configuration or Connections. No business logic or proprietary information should be included.

#### Mark all Personally Identifiable Information (PII) and financially sensitive information with the "WriteOnly" attribute

Note that the [WriteOnly](../object-schema/#writeonly-attribute) attribute will *not* prevent data transfer; it simply obscures data on the App Xchange platform for added security.

PII and sensitive data that must be obscured includes but is not limited to:

- Government issued ID numbers such as social security, passport, driver's license, and comparable numbers

- Payment information such as account, credit card, and debit card numbers

- Income, salary, benefits, Worker's Compensation or other compensation data

- Medical data or health information

- Any kind of authentication data such as usernames, passwords, keys, tokens, etc.

- SEC regulated information

- Personal information such as full name, birthday, age, sex, gender, orientation, religion, race, ethnicity, etc.

- Contact information such as street address, phone, fax, email, etc.

- Confidential business information such as trade secrets, patents, marketing, revenue, upcoming plans, etc.

- Operating financial data such as taxes, bills, activity, etc.

- Legal information

- Sensitive Information Technology data such as configurations, IP addresses and privileged usernames

#### Not introduce breaking schema changes for existing connectors without a migration or versioning plan for dependent integrations

Connector code should be reviewed for breaking changes if updates are made to an existing connector that has in-use integrations, i.e. the connector is no longer under development and is used to transfer customer data.

Breaking changes are changes to connector code that cause downstream issues to caching data from the connector or detecting changes to cached data.

The key areas to examine breaking changes are:

- Changes that impact the data object and action path as they could impact caching and change detection

 - Connector key, module URL part, data object URL part, data object keys

- Changes to schema generation points that introduce a breaking change, e.g. removal of a non-nullable property, more restrictive type-change

 - Data object annotations, data object key names, data object key changes, action input/output/error objects

- Changes to actions or data objects that impact cached objects

 - Default values or nullable values for properties used by data objects or actions

### Limit dependencies on additional third party libraries

- The more external tools are brought in for validation, mapping, or serialization, the more moving parts exist that may be out of date or break later

- Some external libraries have performance considerations

### Libraries used for JSON serialization should be consistent

The serializing and deserializing should be done using the same library. For example, avoid mixing Newtonsoft and System.Text.Json.

The SDK uses System.Text.Json by default and Connectors should as well. There are aspects that require System.Text.Json within the SDK, such as producing the Connector's metadata. The attributes used for object schema generation will not recognize Newtonsoft's attributes, nor will Newtonsoft recognize System.Text.Json attributes.

There are isolated aspects where Newtonsoft could be used without issue, but it is recommended to avoid using Newtonsoft entirely as mixing two libraries can create confusion and bugs in the Connector code base.

### Compile without warnings

- the most common example is missing the nullable type `?` which is needed in addition to the Json attribute [nullable(true)] as applicable on data object properties. See here for more: [Object Schema Nullable Attribute](https://trimble-xchange.github.io/connector-docs/guides/object-schema/#nullable-attribute)
