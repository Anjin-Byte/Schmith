"""Schema processing module.

This module contains schema filtering, type mapping, and naming:
- filter: Schema filtering and relationship detection
- type_mapping: Type conversion utilities
- naming: Semantic naming strategies for DataObject generation
"""

from .filter import (
    filter_schemas,
    find_parent_child_relationships_from_ir,
    find_reachable_component_names,
    find_reachable_schemas,
    get_root_schemas,
    is_error_schema,
    is_primitive_schema,
    is_variant_schema,
    SchemaInfo,
)
from .type_mapping import (
    IR_TO_CSHARP_TYPE,
    build_field_info,
    extract_clean_name,
    format_data_object_name,
    json_name_to_csharp_property,
    schema_id_to_csharp_type,
)
from .naming import (
    NamingConfig,
    NamingStrategy,
    VerboseNamingStrategy,
    SemanticNamingStrategy,
    ResourceNamingStrategy,
    STRATEGIES,
    get_naming_strategy,
    create_config_from_dict,
    generate_operation_name,
    generate_response_name,
)

__all__ = [
    # filter
    "filter_schemas",
    "find_parent_child_relationships_from_ir",
    "find_reachable_component_names",
    "find_reachable_schemas",
    "get_root_schemas",
    "is_error_schema",
    "is_primitive_schema",
    "is_variant_schema",
    "SchemaInfo",
    # type_mapping
    "IR_TO_CSHARP_TYPE",
    "build_field_info",
    "extract_clean_name",
    "format_data_object_name",
    "json_name_to_csharp_property",
    "schema_id_to_csharp_type",
    # naming
    "NamingConfig",
    "NamingStrategy",
    "VerboseNamingStrategy",
    "SemanticNamingStrategy",
    "ResourceNamingStrategy",
    "STRATEGIES",
    "get_naming_strategy",
    "create_config_from_dict",
    "generate_operation_name",
    "generate_response_name",
]
