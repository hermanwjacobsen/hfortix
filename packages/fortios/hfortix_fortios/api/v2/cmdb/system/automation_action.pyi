from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutomationActionPayload(TypedDict, total=False):
    """
    Type hints for system/automation_action payload fields.
    
    Action for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: tls-certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: AutomationActionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 64
    description: str  # Description. | MaxLen: 255
    action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]  # Action type. | Default: alert
    system_action: Literal["reboot", "shutdown", "backup-config"]  # System action type.
    tls_certificate: str  # Custom TLS certificate for API request. | MaxLen: 35
    forticare_email: Literal["enable", "disable"]  # Enable/disable use of your FortiCare email address | Default: disable
    email_to: list[dict[str, Any]]  # Email addresses.
    email_from: str  # Email sender name. | MaxLen: 127
    email_subject: str  # Email subject. | MaxLen: 511
    minimum_interval: int  # Limit execution to no more than once in this inter | Default: 0 | Min: 0 | Max: 2592000
    aws_api_key: str  # AWS API Gateway API key. | MaxLen: 123
    azure_function_authorization: Literal["anonymous", "function", "admin"]  # Azure function authorization level. | Default: anonymous
    azure_api_key: str  # Azure function API key. | MaxLen: 123
    alicloud_function_authorization: Literal["anonymous", "function"]  # AliCloud function authorization type. | Default: anonymous
    alicloud_access_key_id: str  # AliCloud AccessKey ID. | MaxLen: 35
    alicloud_access_key_secret: str  # AliCloud AccessKey secret. | MaxLen: 59
    message_type: Literal["text", "json", "form-data"]  # Message type. | Default: text
    message: str  # Message content. | Default: Time: %%log.date%% %%log.time%%
Device: %%log.devid%% (%%log.vd%%)
Level: %%log.level%%
Event: %%log.logdesc%%
Raw log:
%%log%% | MaxLen: 4095
    replacement_message: Literal["enable", "disable"]  # Enable/disable replacement message. | Default: disable
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    protocol: Literal["http", "https"]  # Request protocol. | Default: http
    method: Literal["post", "put", "get", "patch", "delete"]  # Request method (POST, PUT, GET, PATCH or DELETE). | Default: post
    uri: str  # Request API URI. | MaxLen: 1023
    http_body: str  # Request body (if necessary). Should be serialized | MaxLen: 4095
    port: int  # Protocol port. | Default: 0 | Min: 1 | Max: 65535
    http_headers: list[dict[str, Any]]  # Request headers.
    form_data: list[dict[str, Any]]  # Form data parts for content type multipart/form-da
    verify_host_cert: Literal["enable", "disable"]  # Enable/disable verification of the remote host cer | Default: enable
    script: str  # CLI script. | MaxLen: 1023
    output_size: int  # Number of megabytes to limit script output to | Default: 10 | Min: 1 | Max: 1024
    timeout: int  # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300
    duration: int  # Maximum running time for this script in seconds. | Default: 5 | Min: 1 | Max: 36000
    output_interval: int  # Collect the outputs for each output-interval in se | Default: 0 | Min: 0 | Max: 36000
    file_only: Literal["enable", "disable"]  # Enable/disable the output in files only. | Default: disable
    execute_security_fabric: Literal["enable", "disable"]  # Enable/disable execution of CLI script on all or o | Default: disable
    accprofile: str  # Access profile for CLI script action to access For | MaxLen: 35
    regular_expression: str  # Regular expression string. | MaxLen: 1023
    log_debug_print: Literal["enable", "disable"]  # Enable/disable logging debug print output from dia | Default: disable
    security_tag: str  # NSX security tag. | MaxLen: 255
    sdn_connector: list[dict[str, Any]]  # NSX SDN connector names.

# Nested TypedDicts for table field children (dict mode)

class AutomationActionEmailtoItem(TypedDict):
    """Type hints for email-to table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Email address. | MaxLen: 255


class AutomationActionHttpheadersItem(TypedDict):
    """Type hints for http-headers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    key: str  # Request header key. | MaxLen: 1023
    value: str  # Request header value. | MaxLen: 4095


class AutomationActionFormdataItem(TypedDict):
    """Type hints for form-data table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    key: str  # Key of the part of Multipart/form-data. | MaxLen: 1023
    value: str  # Value of the part of Multipart/form-data. | MaxLen: 4095


class AutomationActionSdnconnectorItem(TypedDict):
    """Type hints for sdn-connector table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # SDN connector name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class AutomationActionEmailtoObject:
    """Typed object for email-to table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Email address. | MaxLen: 255
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class AutomationActionHttpheadersObject:
    """Typed object for http-headers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Request header key. | MaxLen: 1023
    key: str
    # Request header value. | MaxLen: 4095
    value: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class AutomationActionFormdataObject:
    """Typed object for form-data table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Key of the part of Multipart/form-data. | MaxLen: 1023
    key: str
    # Value of the part of Multipart/form-data. | MaxLen: 4095
    value: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class AutomationActionSdnconnectorObject:
    """Typed object for sdn-connector table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SDN connector name. | MaxLen: 79
    name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AutomationActionResponse(TypedDict):
    """
    Type hints for system/automation_action API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 64
    description: str  # Description. | MaxLen: 255
    action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]  # Action type. | Default: alert
    system_action: Literal["reboot", "shutdown", "backup-config"]  # System action type.
    tls_certificate: str  # Custom TLS certificate for API request. | MaxLen: 35
    forticare_email: Literal["enable", "disable"]  # Enable/disable use of your FortiCare email address | Default: disable
    email_to: list[AutomationActionEmailtoItem]  # Email addresses.
    email_from: str  # Email sender name. | MaxLen: 127
    email_subject: str  # Email subject. | MaxLen: 511
    minimum_interval: int  # Limit execution to no more than once in this inter | Default: 0 | Min: 0 | Max: 2592000
    aws_api_key: str  # AWS API Gateway API key. | MaxLen: 123
    azure_function_authorization: Literal["anonymous", "function", "admin"]  # Azure function authorization level. | Default: anonymous
    azure_api_key: str  # Azure function API key. | MaxLen: 123
    alicloud_function_authorization: Literal["anonymous", "function"]  # AliCloud function authorization type. | Default: anonymous
    alicloud_access_key_id: str  # AliCloud AccessKey ID. | MaxLen: 35
    alicloud_access_key_secret: str  # AliCloud AccessKey secret. | MaxLen: 59
    message_type: Literal["text", "json", "form-data"]  # Message type. | Default: text
    message: str  # Message content. | Default: Time: %%log.date%% %%log.time%%
Device: %%log.devid%% (%%log.vd%%)
Level: %%log.level%%
Event: %%log.logdesc%%
Raw log:
%%log%% | MaxLen: 4095
    replacement_message: Literal["enable", "disable"]  # Enable/disable replacement message. | Default: disable
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    protocol: Literal["http", "https"]  # Request protocol. | Default: http
    method: Literal["post", "put", "get", "patch", "delete"]  # Request method (POST, PUT, GET, PATCH or DELETE). | Default: post
    uri: str  # Request API URI. | MaxLen: 1023
    http_body: str  # Request body (if necessary). Should be serialized | MaxLen: 4095
    port: int  # Protocol port. | Default: 0 | Min: 1 | Max: 65535
    http_headers: list[AutomationActionHttpheadersItem]  # Request headers.
    form_data: list[AutomationActionFormdataItem]  # Form data parts for content type multipart/form-da
    verify_host_cert: Literal["enable", "disable"]  # Enable/disable verification of the remote host cer | Default: enable
    script: str  # CLI script. | MaxLen: 1023
    output_size: int  # Number of megabytes to limit script output to | Default: 10 | Min: 1 | Max: 1024
    timeout: int  # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300
    duration: int  # Maximum running time for this script in seconds. | Default: 5 | Min: 1 | Max: 36000
    output_interval: int  # Collect the outputs for each output-interval in se | Default: 0 | Min: 0 | Max: 36000
    file_only: Literal["enable", "disable"]  # Enable/disable the output in files only. | Default: disable
    execute_security_fabric: Literal["enable", "disable"]  # Enable/disable execution of CLI script on all or o | Default: disable
    accprofile: str  # Access profile for CLI script action to access For | MaxLen: 35
    regular_expression: str  # Regular expression string. | MaxLen: 1023
    log_debug_print: Literal["enable", "disable"]  # Enable/disable logging debug print output from dia | Default: disable
    security_tag: str  # NSX security tag. | MaxLen: 255
    sdn_connector: list[AutomationActionSdnconnectorItem]  # NSX SDN connector names.


@final
class AutomationActionObject:
    """Typed FortiObject for system/automation_action with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 64
    name: str
    # Description. | MaxLen: 255
    description: str
    # Action type. | Default: alert
    action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]
    # System action type.
    system_action: Literal["reboot", "shutdown", "backup-config"]
    # Custom TLS certificate for API request. | MaxLen: 35
    tls_certificate: str
    # Enable/disable use of your FortiCare email address as the em | Default: disable
    forticare_email: Literal["enable", "disable"]
    # Email addresses.
    email_to: list[AutomationActionEmailtoObject]
    # Email sender name. | MaxLen: 127
    email_from: str
    # Email subject. | MaxLen: 511
    email_subject: str
    # Limit execution to no more than once in this interval | Default: 0 | Min: 0 | Max: 2592000
    minimum_interval: int
    # AWS API Gateway API key. | MaxLen: 123
    aws_api_key: str
    # Azure function authorization level. | Default: anonymous
    azure_function_authorization: Literal["anonymous", "function", "admin"]
    # Azure function API key. | MaxLen: 123
    azure_api_key: str
    # AliCloud function authorization type. | Default: anonymous
    alicloud_function_authorization: Literal["anonymous", "function"]
    # AliCloud AccessKey ID. | MaxLen: 35
    alicloud_access_key_id: str
    # AliCloud AccessKey secret. | MaxLen: 59
    alicloud_access_key_secret: str
    # Message type. | Default: text
    message_type: Literal["text", "json", "form-data"]
    # Message content. | Default: Time: %%log.date%% %%log.time%%
Device: %%log.devid%% (%%log.vd%%)
Level: %%log.level%%
Event: %%log.logdesc%%
Raw log:
%%log%% | MaxLen: 4095
    message: str
    # Enable/disable replacement message. | Default: disable
    replacement_message: Literal["enable", "disable"]
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # Request protocol. | Default: http
    protocol: Literal["http", "https"]
    # Request method (POST, PUT, GET, PATCH or DELETE). | Default: post
    method: Literal["post", "put", "get", "patch", "delete"]
    # Request API URI. | MaxLen: 1023
    uri: str
    # Request body (if necessary). Should be serialized json strin | MaxLen: 4095
    http_body: str
    # Protocol port. | Default: 0 | Min: 1 | Max: 65535
    port: int
    # Request headers.
    http_headers: list[AutomationActionHttpheadersObject]
    # Form data parts for content type multipart/form-data.
    form_data: list[AutomationActionFormdataObject]
    # Enable/disable verification of the remote host certificate. | Default: enable
    verify_host_cert: Literal["enable", "disable"]
    # CLI script. | MaxLen: 1023
    script: str
    # Number of megabytes to limit script output to | Default: 10 | Min: 1 | Max: 1024
    output_size: int
    # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300
    timeout: int
    # Maximum running time for this script in seconds. | Default: 5 | Min: 1 | Max: 36000
    duration: int
    # Collect the outputs for each output-interval in seconds | Default: 0 | Min: 0 | Max: 36000
    output_interval: int
    # Enable/disable the output in files only. | Default: disable
    file_only: Literal["enable", "disable"]
    # Enable/disable execution of CLI script on all or only one Fo | Default: disable
    execute_security_fabric: Literal["enable", "disable"]
    # Access profile for CLI script action to access FortiGate fea | MaxLen: 35
    accprofile: str
    # Regular expression string. | MaxLen: 1023
    regular_expression: str
    # Enable/disable logging debug print output from diagnose acti | Default: disable
    log_debug_print: Literal["enable", "disable"]
    # NSX security tag. | MaxLen: 255
    security_tag: str
    # NSX SDN connector names.
    sdn_connector: list[AutomationActionSdnconnectorObject]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AutomationActionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutomationAction:
    """
    Action for automation stitches.
    
    Path: system/automation_action
    Category: cmdb
    Primary Key: name
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[AutomationActionObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[AutomationActionObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[AutomationActionObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject | list[AutomationActionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationActionObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "AutomationAction",
    "AutomationActionPayload",
    "AutomationActionResponse",
    "AutomationActionObject",
]