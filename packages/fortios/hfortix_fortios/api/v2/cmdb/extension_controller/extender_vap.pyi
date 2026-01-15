from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExtenderVapPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender_vap payload fields.
    
    FortiExtender wifi vap configuration.
    
    **Usage:**
        payload: ExtenderVapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Wi-Fi VAP name. | MaxLen: 15
    type: Literal["local-vap", "lan-ext-vap"]  # Wi-Fi VAP type local-vap / lan-extension-vap.
    ssid: str  # Wi-Fi SSID. | MaxLen: 32
    max_clients: int  # Wi-Fi max clients (0 - 512), default = 0 | Default: 0 | Min: 0 | Max: 512
    broadcast_ssid: Literal["disable", "enable"]  # Wi-Fi broadcast SSID enable / disable. | Default: enable
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]  # Wi-Fi security. | Default: WPA2-Personal
    dtim: int  # Wi-Fi DTIM (1 - 255) default = 1. | Default: 1 | Min: 1 | Max: 255
    rts_threshold: int  # Wi-Fi RTS Threshold (256 - 2347), default = 2347 | Default: 2347 | Min: 256 | Max: 2347
    pmf: Literal["disabled", "optional", "required"]  # Wi-Fi pmf enable/disable, default = disable. | Default: disabled
    target_wake_time: Literal["disable", "enable"]  # Wi-Fi 802.11AX target wake time enable / disable, | Default: enable
    bss_color_partial: Literal["disable", "enable"]  # Wi-Fi 802.11AX bss color partial enable / disable, | Default: enable
    mu_mimo: Literal["disable", "enable"]  # Wi-Fi multi-user MIMO enable / disable, default = | Default: enable
    passphrase: str  # Wi-Fi passphrase. | MaxLen: 59
    sae_password: str  # Wi-Fi SAE Password. | MaxLen: 124
    auth_server_address: str  # Wi-Fi Authentication Server Address (IPv4 format). | MaxLen: 63
    auth_server_port: int  # Wi-Fi Authentication Server Port. | Default: 0 | Min: 1 | Max: 65535
    auth_server_secret: str  # Wi-Fi Authentication Server Secret. | MaxLen: 63
    ip_address: str  # Extender ip address. | Default: 0.0.0.0 0.0.0.0
    start_ip: str  # Start ip address. | Default: 0.0.0.0
    end_ip: str  # End ip address. | Default: 0.0.0.0
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]  # Control management access to the managed extender.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ExtenderVapResponse(TypedDict):
    """
    Type hints for extension_controller/extender_vap API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Wi-Fi VAP name. | MaxLen: 15
    type: Literal["local-vap", "lan-ext-vap"]  # Wi-Fi VAP type local-vap / lan-extension-vap.
    ssid: str  # Wi-Fi SSID. | MaxLen: 32
    max_clients: int  # Wi-Fi max clients (0 - 512), default = 0 | Default: 0 | Min: 0 | Max: 512
    broadcast_ssid: Literal["disable", "enable"]  # Wi-Fi broadcast SSID enable / disable. | Default: enable
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]  # Wi-Fi security. | Default: WPA2-Personal
    dtim: int  # Wi-Fi DTIM (1 - 255) default = 1. | Default: 1 | Min: 1 | Max: 255
    rts_threshold: int  # Wi-Fi RTS Threshold (256 - 2347), default = 2347 | Default: 2347 | Min: 256 | Max: 2347
    pmf: Literal["disabled", "optional", "required"]  # Wi-Fi pmf enable/disable, default = disable. | Default: disabled
    target_wake_time: Literal["disable", "enable"]  # Wi-Fi 802.11AX target wake time enable / disable, | Default: enable
    bss_color_partial: Literal["disable", "enable"]  # Wi-Fi 802.11AX bss color partial enable / disable, | Default: enable
    mu_mimo: Literal["disable", "enable"]  # Wi-Fi multi-user MIMO enable / disable, default = | Default: enable
    passphrase: str  # Wi-Fi passphrase. | MaxLen: 59
    sae_password: str  # Wi-Fi SAE Password. | MaxLen: 124
    auth_server_address: str  # Wi-Fi Authentication Server Address (IPv4 format). | MaxLen: 63
    auth_server_port: int  # Wi-Fi Authentication Server Port. | Default: 0 | Min: 1 | Max: 65535
    auth_server_secret: str  # Wi-Fi Authentication Server Secret. | MaxLen: 63
    ip_address: str  # Extender ip address. | Default: 0.0.0.0 0.0.0.0
    start_ip: str  # Start ip address. | Default: 0.0.0.0
    end_ip: str  # End ip address. | Default: 0.0.0.0
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]  # Control management access to the managed extender.


@final
class ExtenderVapObject:
    """Typed FortiObject for extension_controller/extender_vap with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Wi-Fi VAP name. | MaxLen: 15
    name: str
    # Wi-Fi VAP type local-vap / lan-extension-vap.
    type: Literal["local-vap", "lan-ext-vap"]
    # Wi-Fi SSID. | MaxLen: 32
    ssid: str
    # Wi-Fi max clients (0 - 512), default = 0 (no limit) | Default: 0 | Min: 0 | Max: 512
    max_clients: int
    # Wi-Fi broadcast SSID enable / disable. | Default: enable
    broadcast_ssid: Literal["disable", "enable"]
    # Wi-Fi security. | Default: WPA2-Personal
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]
    # Wi-Fi DTIM (1 - 255) default = 1. | Default: 1 | Min: 1 | Max: 255
    dtim: int
    # Wi-Fi RTS Threshold (256 - 2347), default = 2347 | Default: 2347 | Min: 256 | Max: 2347
    rts_threshold: int
    # Wi-Fi pmf enable/disable, default = disable. | Default: disabled
    pmf: Literal["disabled", "optional", "required"]
    # Wi-Fi 802.11AX target wake time enable / disable, default = | Default: enable
    target_wake_time: Literal["disable", "enable"]
    # Wi-Fi 802.11AX bss color partial enable / disable, default = | Default: enable
    bss_color_partial: Literal["disable", "enable"]
    # Wi-Fi multi-user MIMO enable / disable, default = enable. | Default: enable
    mu_mimo: Literal["disable", "enable"]
    # Wi-Fi passphrase. | MaxLen: 59
    passphrase: str
    # Wi-Fi SAE Password. | MaxLen: 124
    sae_password: str
    # Wi-Fi Authentication Server Address (IPv4 format). | MaxLen: 63
    auth_server_address: str
    # Wi-Fi Authentication Server Port. | Default: 0 | Min: 1 | Max: 65535
    auth_server_port: int
    # Wi-Fi Authentication Server Secret. | MaxLen: 63
    auth_server_secret: str
    # Extender ip address. | Default: 0.0.0.0 0.0.0.0
    ip_address: str
    # Start ip address. | Default: 0.0.0.0
    start_ip: str
    # End ip address. | Default: 0.0.0.0
    end_ip: str
    # Control management access to the managed extender. Separate
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    
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
    def to_dict(self) -> ExtenderVapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExtenderVap:
    """
    FortiExtender wifi vap configuration.
    
    Path: extension_controller/extender_vap
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> list[ExtenderVapObject]: ...
    
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> list[ExtenderVapObject]: ...
    
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> ExtenderVapObject: ...
    
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
    ) -> list[ExtenderVapObject]: ...
    
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
    ) -> ExtenderVapObject | list[ExtenderVapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
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
    ) -> ExtenderVapObject: ...
    
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
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
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
    "ExtenderVap",
    "ExtenderVapPayload",
    "ExtenderVapResponse",
    "ExtenderVapObject",
]