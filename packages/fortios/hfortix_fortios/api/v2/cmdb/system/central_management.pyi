from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CentralManagementPayload(TypedDict, total=False):
    """
    Type hints for system/central_management payload fields.
    
    Configure central management.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: local-cert)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: fortigate-cloud-sso-default-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: CentralManagementPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: Literal["normal", "backup"]  # Central management mode. | Default: normal
    type: Literal["fortimanager", "fortiguard", "none"]  # Central management type. | Default: fortiguard
    fortigate_cloud_sso_default_profile: str  # Override access profile. Permission is set to read | MaxLen: 35
    schedule_config_restore: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    schedule_script_restore: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_push_configuration: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_push_firmware: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_remote_firmware_upgrade: Literal["enable", "disable"]  # Enable/disable remotely upgrading the firmware on | Default: enable
    allow_monitor: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    serial_number: str  # Serial number.
    fmg: str  # IP address or FQDN of the FortiManager.
    fmg_source_ip: str  # IPv4 source address that this FortiGate uses when | Default: 0.0.0.0
    fmg_source_ip6: str  # IPv6 source address that this FortiGate uses when | Default: ::
    local_cert: str  # Certificate to be used by FGFM protocol. | MaxLen: 35
    ca_cert: str  # CA certificate to be used by FGFM protocol.
    vdom: str  # Virtual domain (VDOM) name to use when communicati | Default: root | MaxLen: 31
    server_list: list[dict[str, Any]]  # Additional severs that the FortiGate can use for u
    fmg_update_port: Literal["8890", "443"]  # Port used to communicate with FortiManager that is | Default: 8890
    fmg_update_http_header: Literal["enable", "disable"]  # Enable/disable inclusion of HTTP header in update | Default: disable
    include_default_servers: Literal["enable", "disable"]  # Enable/disable inclusion of public FortiGuard serv | Default: enable
    enc_algorithm: Literal["default", "high", "low"]  # Encryption strength for communications between the | Default: high
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

class CentralManagementServerlistItem(TypedDict):
    """Type hints for server-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    server_type: Literal["update", "rating", "vpatch-query", "iot-collect"]  # FortiGuard service type.
    addr_type: Literal["ipv4", "ipv6", "fqdn"]  # Indicate whether the FortiGate communicates with t | Default: ipv4
    server_address: str  # IPv4 address of override server. | Default: 0.0.0.0
    server_address6: str  # IPv6 address of override server. | Default: ::
    fqdn: str  # FQDN address of override server. | MaxLen: 255


# Nested classes for table field children (object mode)

@final
class CentralManagementServerlistObject:
    """Typed object for server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # FortiGuard service type.
    server_type: Literal["update", "rating", "vpatch-query", "iot-collect"]
    # Indicate whether the FortiGate communicates with the overrid | Default: ipv4
    addr_type: Literal["ipv4", "ipv6", "fqdn"]
    # IPv4 address of override server. | Default: 0.0.0.0
    server_address: str
    # IPv6 address of override server. | Default: ::
    server_address6: str
    # FQDN address of override server. | MaxLen: 255
    fqdn: str
    
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
class CentralManagementResponse(TypedDict):
    """
    Type hints for system/central_management API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    mode: Literal["normal", "backup"]  # Central management mode. | Default: normal
    type: Literal["fortimanager", "fortiguard", "none"]  # Central management type. | Default: fortiguard
    fortigate_cloud_sso_default_profile: str  # Override access profile. Permission is set to read | MaxLen: 35
    schedule_config_restore: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    schedule_script_restore: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_push_configuration: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_push_firmware: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    allow_remote_firmware_upgrade: Literal["enable", "disable"]  # Enable/disable remotely upgrading the firmware on | Default: enable
    allow_monitor: Literal["enable", "disable"]  # Enable/disable allowing the central management ser | Default: enable
    serial_number: str  # Serial number.
    fmg: str  # IP address or FQDN of the FortiManager.
    fmg_source_ip: str  # IPv4 source address that this FortiGate uses when | Default: 0.0.0.0
    fmg_source_ip6: str  # IPv6 source address that this FortiGate uses when | Default: ::
    local_cert: str  # Certificate to be used by FGFM protocol. | MaxLen: 35
    ca_cert: str  # CA certificate to be used by FGFM protocol.
    vdom: str  # Virtual domain (VDOM) name to use when communicati | Default: root | MaxLen: 31
    server_list: list[CentralManagementServerlistItem]  # Additional severs that the FortiGate can use for u
    fmg_update_port: Literal["8890", "443"]  # Port used to communicate with FortiManager that is | Default: 8890
    fmg_update_http_header: Literal["enable", "disable"]  # Enable/disable inclusion of HTTP header in update | Default: disable
    include_default_servers: Literal["enable", "disable"]  # Enable/disable inclusion of public FortiGuard serv | Default: enable
    enc_algorithm: Literal["default", "high", "low"]  # Encryption strength for communications between the | Default: high
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class CentralManagementObject:
    """Typed FortiObject for system/central_management with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Central management mode. | Default: normal
    mode: Literal["normal", "backup"]
    # Central management type. | Default: fortiguard
    type: Literal["fortimanager", "fortiguard", "none"]
    # Override access profile. Permission is set to read-only with | MaxLen: 35
    fortigate_cloud_sso_default_profile: str
    # Enable/disable allowing the central management server to res | Default: enable
    schedule_config_restore: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to res | Default: enable
    schedule_script_restore: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to pus | Default: enable
    allow_push_configuration: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to pus | Default: enable
    allow_push_firmware: Literal["enable", "disable"]
    # Enable/disable remotely upgrading the firmware on this Forti | Default: enable
    allow_remote_firmware_upgrade: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to rem | Default: enable
    allow_monitor: Literal["enable", "disable"]
    # Serial number.
    serial_number: str
    # IP address or FQDN of the FortiManager.
    fmg: str
    # IPv4 source address that this FortiGate uses when communicat | Default: 0.0.0.0
    fmg_source_ip: str
    # IPv6 source address that this FortiGate uses when communicat | Default: ::
    fmg_source_ip6: str
    # Certificate to be used by FGFM protocol. | MaxLen: 35
    local_cert: str
    # CA certificate to be used by FGFM protocol.
    ca_cert: str
    # Virtual domain (VDOM) name to use when communicating with Fo | Default: root | MaxLen: 31
    vdom: str
    # Additional severs that the FortiGate can use for updates
    server_list: list[CentralManagementServerlistObject]
    # Port used to communicate with FortiManager that is acting as | Default: 8890
    fmg_update_port: Literal["8890", "443"]
    # Enable/disable inclusion of HTTP header in update request. | Default: disable
    fmg_update_http_header: Literal["enable", "disable"]
    # Enable/disable inclusion of public FortiGuard servers in the | Default: enable
    include_default_servers: Literal["enable", "disable"]
    # Encryption strength for communications between the FortiGate | Default: high
    enc_algorithm: Literal["default", "high", "low"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
    def to_dict(self) -> CentralManagementPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class CentralManagement:
    """
    Configure central management.
    
    Path: system/central_management
    Category: cmdb
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> CentralManagementObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> CentralManagementObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> CentralManagementObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "CentralManagement",
    "CentralManagementPayload",
    "CentralManagementResponse",
    "CentralManagementObject",
]