from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExtenderPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender payload fields.
    
    Extender controller configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.extension-controller.extender-profile.ExtenderProfileEndpoint` (via: profile)

    **Usage:**
        payload: ExtenderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # FortiExtender entry name. | MaxLen: 19
    id: str  # FortiExtender serial number. | MaxLen: 19
    authorized: Literal["discovered", "disable", "enable"]  # FortiExtender Administration (enable or disable). | Default: discovered
    ext_name: str  # FortiExtender name. | MaxLen: 31
    description: str  # Description. | MaxLen: 255
    vdom: int  # VDOM. | Default: 1 | Min: 0 | Max: 4294967295
    device_id: int  # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    extension_type: Literal["wan-extension", "lan-extension"]  # Extension type for this FortiExtender.
    profile: str  # FortiExtender profile configuration. | MaxLen: 31
    override_allowaccess: Literal["enable", "disable"]  # Enable to override the extender profile management | Default: disable
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]  # Control management access to the managed extender.
    override_login_password_change: Literal["enable", "disable"]  # Enable to override the extender profile login-pass | Default: disable
    login_password_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_password: str  # Set the managed extender's administrator password. | MaxLen: 27
    override_enforce_bandwidth: Literal["enable", "disable"]  # Enable to override the extender profile enforce-ba | Default: disable
    enforce_bandwidth: Literal["enable", "disable"]  # Enable/disable enforcement of bandwidth on LAN ext | Default: disable
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps) | Default: 1024 | Min: 1 | Max: 16776000
    wan_extension: str  # FortiExtender wan extension configuration.
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ExtenderResponse(TypedDict):
    """
    Type hints for extension_controller/extender API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # FortiExtender entry name. | MaxLen: 19
    id: str  # FortiExtender serial number. | MaxLen: 19
    authorized: Literal["discovered", "disable", "enable"]  # FortiExtender Administration (enable or disable). | Default: discovered
    ext_name: str  # FortiExtender name. | MaxLen: 31
    description: str  # Description. | MaxLen: 255
    vdom: int  # VDOM. | Default: 1 | Min: 0 | Max: 4294967295
    device_id: int  # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    extension_type: Literal["wan-extension", "lan-extension"]  # Extension type for this FortiExtender.
    profile: str  # FortiExtender profile configuration. | MaxLen: 31
    override_allowaccess: Literal["enable", "disable"]  # Enable to override the extender profile management | Default: disable
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]  # Control management access to the managed extender.
    override_login_password_change: Literal["enable", "disable"]  # Enable to override the extender profile login-pass | Default: disable
    login_password_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_password: str  # Set the managed extender's administrator password. | MaxLen: 27
    override_enforce_bandwidth: Literal["enable", "disable"]  # Enable to override the extender profile enforce-ba | Default: disable
    enforce_bandwidth: Literal["enable", "disable"]  # Enable/disable enforcement of bandwidth on LAN ext | Default: disable
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps) | Default: 1024 | Min: 1 | Max: 16776000
    wan_extension: str  # FortiExtender wan extension configuration.
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable


@final
class ExtenderObject:
    """Typed FortiObject for extension_controller/extender with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # FortiExtender entry name. | MaxLen: 19
    name: str
    # FortiExtender serial number. | MaxLen: 19
    id: str
    # FortiExtender Administration (enable or disable). | Default: discovered
    authorized: Literal["discovered", "disable", "enable"]
    # FortiExtender name. | MaxLen: 31
    ext_name: str
    # Description. | MaxLen: 255
    description: str
    # VDOM. | Default: 1 | Min: 0 | Max: 4294967295
    vdom: int
    # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    device_id: int
    # Extension type for this FortiExtender.
    extension_type: Literal["wan-extension", "lan-extension"]
    # FortiExtender profile configuration. | MaxLen: 31
    profile: str
    # Enable to override the extender profile management access co | Default: disable
    override_allowaccess: Literal["enable", "disable"]
    # Control management access to the managed extender. Separate
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    # Enable to override the extender profile login-password | Default: disable
    override_login_password_change: Literal["enable", "disable"]
    # Change or reset the administrator password of a managed exte | Default: no
    login_password_change: Literal["yes", "default", "no"]
    # Set the managed extender's administrator password. | MaxLen: 27
    login_password: str
    # Enable to override the extender profile enforce-bandwidth se | Default: disable
    override_enforce_bandwidth: Literal["enable", "disable"]
    # Enable/disable enforcement of bandwidth on LAN extension int | Default: disable
    enforce_bandwidth: Literal["enable", "disable"]
    # FortiExtender LAN extension bandwidth limit (Mbps). | Default: 1024 | Min: 1 | Max: 16776000
    bandwidth_limit: int
    # FortiExtender wan extension configuration.
    wan_extension: str
    # Enable/disable one-time automatic provisioning of the latest | Default: disable
    firmware_provision_latest: Literal["disable", "once"]
    
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
    def to_dict(self) -> ExtenderPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Extender:
    """
    Extender controller configuration.
    
    Path: extension_controller/extender
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
    ) -> ExtenderObject: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> list[ExtenderObject]: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> list[ExtenderObject]: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> list[ExtenderObject]: ...
    
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
    ) -> ExtenderObject | list[ExtenderObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExtenderObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExtenderObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
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
    ) -> ExtenderObject: ...
    
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
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
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
    "Extender",
    "ExtenderPayload",
    "ExtenderResponse",
    "ExtenderObject",
]