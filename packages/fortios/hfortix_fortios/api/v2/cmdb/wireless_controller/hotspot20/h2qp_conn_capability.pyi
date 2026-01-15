from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class H2qpConnCapabilityPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/h2qp_conn_capability payload fields.
    
    Configure connection capability.
    
    **Usage:**
        payload: H2qpConnCapabilityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Connection capability name. | MaxLen: 35
    icmp_port: Literal["closed", "open", "unknown"]  # Set ICMP port service status. | Default: unknown
    ftp_port: Literal["closed", "open", "unknown"]  # Set FTP port service status. | Default: unknown
    ssh_port: Literal["closed", "open", "unknown"]  # Set SSH port service status. | Default: unknown
    http_port: Literal["closed", "open", "unknown"]  # Set HTTP port service status. | Default: unknown
    tls_port: Literal["closed", "open", "unknown"]  # Set TLS VPN (HTTPS) port service status. | Default: unknown
    pptp_vpn_port: Literal["closed", "open", "unknown"]  # Set Point to Point Tunneling Protocol (PPTP) VPN p | Default: unknown
    voip_tcp_port: Literal["closed", "open", "unknown"]  # Set VoIP TCP port service status. | Default: unknown
    voip_udp_port: Literal["closed", "open", "unknown"]  # Set VoIP UDP port service status. | Default: unknown
    ikev2_port: Literal["closed", "open", "unknown"]  # Set IKEv2 port service for IPsec VPN status. | Default: unknown
    ikev2_xx_port: Literal["closed", "open", "unknown"]  # Set UDP port 4500 | Default: unknown
    esp_port: Literal["closed", "open", "unknown"]  # Set ESP port service (used by IPsec VPNs) status. | Default: unknown

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class H2qpConnCapabilityResponse(TypedDict):
    """
    Type hints for wireless_controller/hotspot20/h2qp_conn_capability API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Connection capability name. | MaxLen: 35
    icmp_port: Literal["closed", "open", "unknown"]  # Set ICMP port service status. | Default: unknown
    ftp_port: Literal["closed", "open", "unknown"]  # Set FTP port service status. | Default: unknown
    ssh_port: Literal["closed", "open", "unknown"]  # Set SSH port service status. | Default: unknown
    http_port: Literal["closed", "open", "unknown"]  # Set HTTP port service status. | Default: unknown
    tls_port: Literal["closed", "open", "unknown"]  # Set TLS VPN (HTTPS) port service status. | Default: unknown
    pptp_vpn_port: Literal["closed", "open", "unknown"]  # Set Point to Point Tunneling Protocol (PPTP) VPN p | Default: unknown
    voip_tcp_port: Literal["closed", "open", "unknown"]  # Set VoIP TCP port service status. | Default: unknown
    voip_udp_port: Literal["closed", "open", "unknown"]  # Set VoIP UDP port service status. | Default: unknown
    ikev2_port: Literal["closed", "open", "unknown"]  # Set IKEv2 port service for IPsec VPN status. | Default: unknown
    ikev2_xx_port: Literal["closed", "open", "unknown"]  # Set UDP port 4500 | Default: unknown
    esp_port: Literal["closed", "open", "unknown"]  # Set ESP port service (used by IPsec VPNs) status. | Default: unknown


@final
class H2qpConnCapabilityObject:
    """Typed FortiObject for wireless_controller/hotspot20/h2qp_conn_capability with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Connection capability name. | MaxLen: 35
    name: str
    # Set ICMP port service status. | Default: unknown
    icmp_port: Literal["closed", "open", "unknown"]
    # Set FTP port service status. | Default: unknown
    ftp_port: Literal["closed", "open", "unknown"]
    # Set SSH port service status. | Default: unknown
    ssh_port: Literal["closed", "open", "unknown"]
    # Set HTTP port service status. | Default: unknown
    http_port: Literal["closed", "open", "unknown"]
    # Set TLS VPN (HTTPS) port service status. | Default: unknown
    tls_port: Literal["closed", "open", "unknown"]
    # Set Point to Point Tunneling Protocol (PPTP) VPN port servic | Default: unknown
    pptp_vpn_port: Literal["closed", "open", "unknown"]
    # Set VoIP TCP port service status. | Default: unknown
    voip_tcp_port: Literal["closed", "open", "unknown"]
    # Set VoIP UDP port service status. | Default: unknown
    voip_udp_port: Literal["closed", "open", "unknown"]
    # Set IKEv2 port service for IPsec VPN status. | Default: unknown
    ikev2_port: Literal["closed", "open", "unknown"]
    # Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) | Default: unknown
    ikev2_xx_port: Literal["closed", "open", "unknown"]
    # Set ESP port service (used by IPsec VPNs) status. | Default: unknown
    esp_port: Literal["closed", "open", "unknown"]
    
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
    def to_dict(self) -> H2qpConnCapabilityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class H2qpConnCapability:
    """
    Configure connection capability.
    
    Path: wireless_controller/hotspot20/h2qp_conn_capability
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> FortiObjectList[H2qpConnCapabilityObject]: ...
    
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> FortiObjectList[H2qpConnCapabilityObject]: ...
    
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> FortiObjectList[H2qpConnCapabilityObject]: ...
    
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
    ) -> H2qpConnCapabilityObject | list[H2qpConnCapabilityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> H2qpConnCapabilityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> H2qpConnCapabilityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> H2qpConnCapabilityObject: ...
    
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
        payload_dict: H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
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
    "H2qpConnCapability",
    "H2qpConnCapabilityPayload",
    "H2qpConnCapabilityResponse",
    "H2qpConnCapabilityObject",
]