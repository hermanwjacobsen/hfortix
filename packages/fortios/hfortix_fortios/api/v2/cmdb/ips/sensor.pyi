from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SensorPayload(TypedDict, total=False):
    """
    Type hints for ips/sensor payload fields.
    
    Configure IPS sensor.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: SensorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Sensor name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    block_malicious_url: Literal["disable", "enable"]  # Enable/disable malicious URL blocking. | Default: disable
    scan_botnet_connections: Literal["disable", "block", "monitor"]  # Block or monitor connections to Botnet servers, or | Default: disable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging. | Default: disable
    entries: list[dict[str, Any]]  # IPS sensor filter.

# Nested TypedDicts for table field children (dict mode)

class SensorEntriesItem(TypedDict):
    """Type hints for entries table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Rule ID in IPS database (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    rule: str  # Identifies the predefined or custom IPS signatures
    location: str  # Protect client or server traffic. | Default: all
    severity: str  # Relative severity of the signature, from info to c | Default: all
    protocol: str  # Protocols to be examined. Use all for every protoc | Default: all
    os: str  # Operating systems to be protected. Use all for eve | Default: all
    application: str  # Operating systems to be protected. Use all for eve | Default: all
    default_action: Literal["all", "pass", "block"]  # Signature default action filter. | Default: all
    default_status: Literal["all", "enable", "disable"]  # Signature default status filter. | Default: all
    cve: str  # List of CVE IDs of the signatures to add to the se
    vuln_type: str  # List of signature vulnerability types to filter by
    last_modified: str  # Filter by signature last modified date. Formats: b
    status: Literal["disable", "enable", "default"]  # Status of the signatures included in filter. Only | Default: default
    log: Literal["disable", "enable"]  # Enable/disable logging of signatures included in f | Default: enable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet logging. Enable to save the | Default: disable
    log_attack_context: Literal["disable", "enable"]  # Enable/disable logging of attack context: URL buff | Default: disable
    action: Literal["pass", "block", "reset", "default"]  # Action taken with traffic in which signatures are | Default: default
    rate_count: int  # Count of the rate. | Default: 0 | Min: 0 | Max: 65535
    rate_duration: int  # Duration (sec) of the rate. | Default: 60 | Min: 1 | Max: 65535
    rate_mode: Literal["periodical", "continuous"]  # Rate limit mode. | Default: continuous
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]  # Track the packet protocol field. | Default: none
    exempt_ip: str  # Traffic from selected source or destination IP add
    quarantine: Literal["none", "attacker"]  # Quarantine method. | Default: none
    quarantine_expiry: str  # Duration of quarantine. | Default: 5m
    quarantine_log: Literal["disable", "enable"]  # Enable/disable quarantine logging. | Default: enable


# Nested classes for table field children (object mode)

@final
class SensorEntriesObject:
    """Typed object for entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID in IPS database (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Identifies the predefined or custom IPS signatures to add to
    rule: str
    # Protect client or server traffic. | Default: all
    location: str
    # Relative severity of the signature, from info to critical. L | Default: all
    severity: str
    # Protocols to be examined. Use all for every protocol and oth | Default: all
    protocol: str
    # Operating systems to be protected. Use all for every operati | Default: all
    os: str
    # Operating systems to be protected. Use all for every applica | Default: all
    application: str
    # Signature default action filter. | Default: all
    default_action: Literal["all", "pass", "block"]
    # Signature default status filter. | Default: all
    default_status: Literal["all", "enable", "disable"]
    # List of CVE IDs of the signatures to add to the sensor.
    cve: str
    # List of signature vulnerability types to filter by.
    vuln_type: str
    # Filter by signature last modified date. Formats: before <dat
    last_modified: str
    # Status of the signatures included in filter. Only those filt | Default: default
    status: Literal["disable", "enable", "default"]
    # Enable/disable logging of signatures included in filter. | Default: enable
    log: Literal["disable", "enable"]
    # Enable/disable packet logging. Enable to save the packet tha | Default: disable
    log_packet: Literal["disable", "enable"]
    # Enable/disable logging of attack context: URL buffer, header | Default: disable
    log_attack_context: Literal["disable", "enable"]
    # Action taken with traffic in which signatures are detected. | Default: default
    action: Literal["pass", "block", "reset", "default"]
    # Count of the rate. | Default: 0 | Min: 0 | Max: 65535
    rate_count: int
    # Duration (sec) of the rate. | Default: 60 | Min: 1 | Max: 65535
    rate_duration: int
    # Rate limit mode. | Default: continuous
    rate_mode: Literal["periodical", "continuous"]
    # Track the packet protocol field. | Default: none
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]
    # Traffic from selected source or destination IP addresses is
    exempt_ip: str
    # Quarantine method. | Default: none
    quarantine: Literal["none", "attacker"]
    # Duration of quarantine. | Default: 5m
    quarantine_expiry: str
    # Enable/disable quarantine logging. | Default: enable
    quarantine_log: Literal["disable", "enable"]
    
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
class SensorResponse(TypedDict):
    """
    Type hints for ips/sensor API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Sensor name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    block_malicious_url: Literal["disable", "enable"]  # Enable/disable malicious URL blocking. | Default: disable
    scan_botnet_connections: Literal["disable", "block", "monitor"]  # Block or monitor connections to Botnet servers, or | Default: disable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging. | Default: disable
    entries: list[SensorEntriesItem]  # IPS sensor filter.


@final
class SensorObject:
    """Typed FortiObject for ips/sensor with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sensor name. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # Enable/disable malicious URL blocking. | Default: disable
    block_malicious_url: Literal["disable", "enable"]
    # Block or monitor connections to Botnet servers, or disable B | Default: disable
    scan_botnet_connections: Literal["disable", "block", "monitor"]
    # Enable/disable extended logging. | Default: disable
    extended_log: Literal["enable", "disable"]
    # IPS sensor filter.
    entries: list[SensorEntriesObject]
    
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
    def to_dict(self) -> SensorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sensor:
    """
    Configure IPS sensor.
    
    Path: ips/sensor
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
    ) -> SensorObject: ...
    
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
    ) -> SensorObject: ...
    
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
    ) -> list[SensorObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> SensorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[SensorObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[SensorObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> SensorObject | list[SensorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "Sensor",
    "SensorPayload",
    "SensorResponse",
    "SensorObject",
]