from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AccprofilePayload(TypedDict, total=False):
    """
    Type hints for system/accprofile payload fields.
    
    Configure access profiles for system administrators.
    
    **Usage:**
        payload: AccprofilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 35
    scope: Literal["vdom", "global"]  # Scope of admin access: global or specific VDOM(s). | Default: vdom
    comments: str  # Comment. | MaxLen: 255
    secfabgrp: Literal["none", "read", "read-write", "custom"]  # Security Fabric. | Default: none
    ftviewgrp: Literal["none", "read", "read-write"]  # FortiView. | Default: none
    authgrp: Literal["none", "read", "read-write"]  # Administrator access to Users and Devices. | Default: none
    sysgrp: Literal["none", "read", "read-write", "custom"]  # System Configuration. | Default: none
    netgrp: Literal["none", "read", "read-write", "custom"]  # Network Configuration. | Default: none
    loggrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to Logging and Reporting incl | Default: none
    fwgrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to the Firewall configuration | Default: none
    vpngrp: Literal["none", "read", "read-write"]  # Administrator access to IPsec, SSL, PPTP, and L2TP | Default: none
    utmgrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to Security Profiles. | Default: none
    wanoptgrp: Literal["none", "read", "read-write"]  # Administrator access to WAN Opt & Cache. | Default: none
    wifi: Literal["none", "read", "read-write"]  # Administrator access to the WiFi controller and Sw | Default: none
    netgrp_permission: str  # Custom network permission.
    sysgrp_permission: str  # Custom system permission.
    fwgrp_permission: str  # Custom firewall permission.
    loggrp_permission: str  # Custom Log & Report permission.
    utmgrp_permission: str  # Custom Security Profile permissions.
    secfabgrp_permission: str  # Custom Security Fabric permissions.
    admintimeout_override: Literal["enable", "disable"]  # Enable/disable overriding the global administrator | Default: disable
    admintimeout: int  # Administrator timeout for this access profile | Default: 10 | Min: 1 | Max: 480
    cli_diagnose: Literal["enable", "disable"]  # Enable/disable permission to run diagnostic comman | Default: disable
    cli_get: Literal["enable", "disable"]  # Enable/disable permission to run get commands. | Default: disable
    cli_show: Literal["enable", "disable"]  # Enable/disable permission to run show commands. | Default: disable
    cli_exec: Literal["enable", "disable"]  # Enable/disable permission to run execute commands. | Default: disable
    cli_config: Literal["enable", "disable"]  # Enable/disable permission to run config commands. | Default: disable
    system_execute_ssh: Literal["enable", "disable"]  # Enable/disable permission to execute SSH commands. | Default: enable
    system_execute_telnet: Literal["enable", "disable"]  # Enable/disable permission to execute TELNET comman | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class AccprofileResponse(TypedDict):
    """
    Type hints for system/accprofile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 35
    scope: Literal["vdom", "global"]  # Scope of admin access: global or specific VDOM(s). | Default: vdom
    comments: str  # Comment. | MaxLen: 255
    secfabgrp: Literal["none", "read", "read-write", "custom"]  # Security Fabric. | Default: none
    ftviewgrp: Literal["none", "read", "read-write"]  # FortiView. | Default: none
    authgrp: Literal["none", "read", "read-write"]  # Administrator access to Users and Devices. | Default: none
    sysgrp: Literal["none", "read", "read-write", "custom"]  # System Configuration. | Default: none
    netgrp: Literal["none", "read", "read-write", "custom"]  # Network Configuration. | Default: none
    loggrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to Logging and Reporting incl | Default: none
    fwgrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to the Firewall configuration | Default: none
    vpngrp: Literal["none", "read", "read-write"]  # Administrator access to IPsec, SSL, PPTP, and L2TP | Default: none
    utmgrp: Literal["none", "read", "read-write", "custom"]  # Administrator access to Security Profiles. | Default: none
    wanoptgrp: Literal["none", "read", "read-write"]  # Administrator access to WAN Opt & Cache. | Default: none
    wifi: Literal["none", "read", "read-write"]  # Administrator access to the WiFi controller and Sw | Default: none
    netgrp_permission: str  # Custom network permission.
    sysgrp_permission: str  # Custom system permission.
    fwgrp_permission: str  # Custom firewall permission.
    loggrp_permission: str  # Custom Log & Report permission.
    utmgrp_permission: str  # Custom Security Profile permissions.
    secfabgrp_permission: str  # Custom Security Fabric permissions.
    admintimeout_override: Literal["enable", "disable"]  # Enable/disable overriding the global administrator | Default: disable
    admintimeout: int  # Administrator timeout for this access profile | Default: 10 | Min: 1 | Max: 480
    cli_diagnose: Literal["enable", "disable"]  # Enable/disable permission to run diagnostic comman | Default: disable
    cli_get: Literal["enable", "disable"]  # Enable/disable permission to run get commands. | Default: disable
    cli_show: Literal["enable", "disable"]  # Enable/disable permission to run show commands. | Default: disable
    cli_exec: Literal["enable", "disable"]  # Enable/disable permission to run execute commands. | Default: disable
    cli_config: Literal["enable", "disable"]  # Enable/disable permission to run config commands. | Default: disable
    system_execute_ssh: Literal["enable", "disable"]  # Enable/disable permission to execute SSH commands. | Default: enable
    system_execute_telnet: Literal["enable", "disable"]  # Enable/disable permission to execute TELNET comman | Default: enable


@final
class AccprofileObject:
    """Typed FortiObject for system/accprofile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 35
    name: str
    # Scope of admin access: global or specific VDOM(s). | Default: vdom
    scope: Literal["vdom", "global"]
    # Comment. | MaxLen: 255
    comments: str
    # Security Fabric. | Default: none
    secfabgrp: Literal["none", "read", "read-write", "custom"]
    # FortiView. | Default: none
    ftviewgrp: Literal["none", "read", "read-write"]
    # Administrator access to Users and Devices. | Default: none
    authgrp: Literal["none", "read", "read-write"]
    # System Configuration. | Default: none
    sysgrp: Literal["none", "read", "read-write", "custom"]
    # Network Configuration. | Default: none
    netgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to Logging and Reporting including view | Default: none
    loggrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to the Firewall configuration. | Default: none
    fwgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to IPsec, SSL, PPTP, and L2TP VPN. | Default: none
    vpngrp: Literal["none", "read", "read-write"]
    # Administrator access to Security Profiles. | Default: none
    utmgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to WAN Opt & Cache. | Default: none
    wanoptgrp: Literal["none", "read", "read-write"]
    # Administrator access to the WiFi controller and Switch contr | Default: none
    wifi: Literal["none", "read", "read-write"]
    # Custom network permission.
    netgrp_permission: str
    # Custom system permission.
    sysgrp_permission: str
    # Custom firewall permission.
    fwgrp_permission: str
    # Custom Log & Report permission.
    loggrp_permission: str
    # Custom Security Profile permissions.
    utmgrp_permission: str
    # Custom Security Fabric permissions.
    secfabgrp_permission: str
    # Enable/disable overriding the global administrator idle time | Default: disable
    admintimeout_override: Literal["enable", "disable"]
    # Administrator timeout for this access profile | Default: 10 | Min: 1 | Max: 480
    admintimeout: int
    # Enable/disable permission to run diagnostic commands. | Default: disable
    cli_diagnose: Literal["enable", "disable"]
    # Enable/disable permission to run get commands. | Default: disable
    cli_get: Literal["enable", "disable"]
    # Enable/disable permission to run show commands. | Default: disable
    cli_show: Literal["enable", "disable"]
    # Enable/disable permission to run execute commands. | Default: disable
    cli_exec: Literal["enable", "disable"]
    # Enable/disable permission to run config commands. | Default: disable
    cli_config: Literal["enable", "disable"]
    # Enable/disable permission to execute SSH commands. | Default: enable
    system_execute_ssh: Literal["enable", "disable"]
    # Enable/disable permission to execute TELNET commands. | Default: enable
    system_execute_telnet: Literal["enable", "disable"]
    
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
    def to_dict(self) -> AccprofilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Accprofile:
    """
    Configure access profiles for system administrators.
    
    Path: system/accprofile
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
    ) -> AccprofileObject: ...
    
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
    ) -> AccprofileObject: ...
    
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
    ) -> FortiObjectList[AccprofileObject]: ...
    
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
    ) -> AccprofileObject: ...
    
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
    ) -> AccprofileObject: ...
    
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
    ) -> FortiObjectList[AccprofileObject]: ...
    
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
    ) -> AccprofileObject: ...
    
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
    ) -> AccprofileObject: ...
    
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
    ) -> FortiObjectList[AccprofileObject]: ...
    
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
    ) -> AccprofileObject | list[AccprofileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccprofileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccprofileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccprofileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
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
    "Accprofile",
    "AccprofilePayload",
    "AccprofileResponse",
    "AccprofileObject",
]