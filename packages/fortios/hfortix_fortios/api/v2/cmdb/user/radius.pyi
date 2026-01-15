from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RadiusPayload(TypedDict, total=False):
    """
    Type hints for user/radius payload fields.
    
    Configure RADIUS server entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ca-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: client-cert)

    **Usage:**
        payload: RadiusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # RADIUS server entry name. | MaxLen: 35
    server: str  # Primary RADIUS server CN domain name or IP address | MaxLen: 63
    secret: str  # Pre-shared secret key used to access the primary R | MaxLen: 128
    secondary_server: str  # Secondary RADIUS CN domain name or IP address. | MaxLen: 63
    secondary_secret: str  # Secret key to access the secondary server. | MaxLen: 128
    tertiary_server: str  # Tertiary RADIUS CN domain name or IP address. | MaxLen: 63
    tertiary_secret: str  # Secret key to access the tertiary server. | MaxLen: 128
    timeout: int  # Time in seconds to retry connecting server. | Default: 5 | Min: 1 | Max: 300
    status_ttl: int  # Time for which server reachability is cached so th | Default: 300 | Min: 0 | Max: 600
    all_usergroup: Literal["disable", "enable"]  # Enable/disable automatically including this RADIUS | Default: disable
    use_management_vdom: Literal["enable", "disable"]  # Enable/disable using management VDOM to send reque | Default: disable
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"]  # Enable/Disable switch-controller nas-ip dynamic to | Default: disable
    nas_ip: str  # IP address used to communicate with the RADIUS ser | Default: 0.0.0.0
    nas_id_type: Literal["legacy", "custom", "hostname"]  # NAS identifier type configuration | Default: legacy
    call_station_id_type: Literal["legacy", "IP", "MAC"]  # Calling & Called station identifier type configura | Default: legacy
    nas_id: str  # Custom NAS identifier. | MaxLen: 255
    acct_interim_interval: int  # Time in seconds between each accounting interim up | Default: 0 | Min: 60 | Max: 86400
    radius_coa: Literal["enable", "disable"]  # Enable to allow a mechanism to change the attribut | Default: disable
    radius_port: int  # RADIUS service port number. | Default: 0 | Min: 0 | Max: 65535
    h3c_compatibility: Literal["enable", "disable"]  # Enable/disable compatibility with the H3C, a mecha | Default: disable
    auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]  # Authentication methods/protocols permitted for thi | Default: auto
    source_ip: str  # Source IP address for communications to the RADIUS | MaxLen: 63
    source_ip_interface: str  # Source interface for communication with the RADIUS | MaxLen: 15
    username_case_sensitive: Literal["enable", "disable"]  # Enable/disable case sensitive user names. | Default: disable
    group_override_attr_type: Literal["filter-Id", "class"]  # RADIUS attribute type to override user group infor
    password_renewal: Literal["enable", "disable"]  # Enable/disable password renewal. | Default: enable
    require_message_authenticator: Literal["enable", "disable"]  # Require message authenticator in authentication re | Default: enable
    password_encoding: Literal["auto", "ISO-8859-1"]  # Password encoding. | Default: auto
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication password delimiter | Default: hyphen
    mac_case: Literal["uppercase", "lowercase"]  # MAC authentication case (default = lowercase). | Default: lowercase
    acct_all_servers: Literal["enable", "disable"]  # Enable/disable sending of accounting messages to a | Default: disable
    switch_controller_acct_fast_framedip_detect: int  # Switch controller accounting message Framed-IP det | Default: 2 | Min: 2 | Max: 600
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]  # RADIUS service type.
    transport_protocol: Literal["udp", "tcp", "tls"]  # Transport protocol to be used (default = udp). | Default: udp
    tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for TLS connect | Default: default
    ca_cert: str  # CA of server to trust under TLS. | MaxLen: 79
    client_cert: str  # Client certificate to use under TLS. | MaxLen: 35
    server_identity_check: Literal["enable", "disable"]  # Enable/disable RADIUS server identity check | Default: enable
    account_key_processing: Literal["same", "strip"]  # Account key processing operation. The FortiGate wi | Default: same
    account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"]  # Define subject identity field in certificate for u | Default: othername
    rsso: Literal["enable", "disable"]  # Enable/disable RADIUS based single sign on feature | Default: disable
    rsso_radius_server_port: int  # UDP port to listen on for RADIUS Start and Stop re | Default: 1813 | Min: 0 | Max: 65535
    rsso_radius_response: Literal["enable", "disable"]  # Enable/disable sending RADIUS response packets aft | Default: disable
    rsso_validate_request_secret: Literal["enable", "disable"]  # Enable/disable validating the RADIUS request share | Default: disable
    rsso_secret: str  # RADIUS secret used by the RADIUS accounting server | MaxLen: 31
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to extract the user end poi | Default: Calling-Station-Id
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to block a user.
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attribute that contains the profile group n | Default: Class
    sso_attribute_key: str  # Key prefix for SSO group value in the SSO attribut | MaxLen: 35
    sso_attribute_value_override: Literal["enable", "disable"]  # Enable/disable override old attribute value with n | Default: enable
    rsso_context_timeout: int  # Time in seconds before the logged out user is remo | Default: 28800 | Min: 0 | Max: 4294967295
    rsso_log_period: int  # Time interval in seconds that group event log mess | Default: 0 | Min: 0 | Max: 4294967295
    rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]  # Events to log. | Default: protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other
    rsso_flush_ip_session: Literal["enable", "disable"]  # Enable/disable flushing user IP sessions on RADIUS | Default: disable
    rsso_ep_one_ip_only: Literal["enable", "disable"]  # Enable/disable the replacement of old IP addresses | Default: disable
    delimiter: Literal["plus", "comma"]  # Configure delimiter to be used for separating prof | Default: plus
    accounting_server: list[dict[str, Any]]  # Additional accounting servers.

# Nested TypedDicts for table field children (dict mode)

class RadiusClassItem(TypedDict):
    """Type hints for class table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Class name. | MaxLen: 79


class RadiusAccountingserverItem(TypedDict):
    """Type hints for accounting-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Status. | Default: disable
    server: str  # Server CN domain name or IP address. | MaxLen: 63
    secret: str  # Secret key. | MaxLen: 128
    port: int  # RADIUS accounting port number. | Default: 0 | Min: 0 | Max: 65535
    source_ip: str  # Source IP address for communications to the RADIUS | MaxLen: 63
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


# Nested classes for table field children (object mode)

@final
class RadiusClassObject:
    """Typed object for class table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Class name. | MaxLen: 79
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
class RadiusAccountingserverObject:
    """Typed object for accounting-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Server CN domain name or IP address. | MaxLen: 63
    server: str
    # Secret key. | MaxLen: 128
    secret: str
    # RADIUS accounting port number. | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Source IP address for communications to the RADIUS server. | MaxLen: 63
    source_ip: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
class RadiusResponse(TypedDict):
    """
    Type hints for user/radius API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # RADIUS server entry name. | MaxLen: 35
    server: str  # Primary RADIUS server CN domain name or IP address | MaxLen: 63
    secret: str  # Pre-shared secret key used to access the primary R | MaxLen: 128
    secondary_server: str  # Secondary RADIUS CN domain name or IP address. | MaxLen: 63
    secondary_secret: str  # Secret key to access the secondary server. | MaxLen: 128
    tertiary_server: str  # Tertiary RADIUS CN domain name or IP address. | MaxLen: 63
    tertiary_secret: str  # Secret key to access the tertiary server. | MaxLen: 128
    timeout: int  # Time in seconds to retry connecting server. | Default: 5 | Min: 1 | Max: 300
    status_ttl: int  # Time for which server reachability is cached so th | Default: 300 | Min: 0 | Max: 600
    all_usergroup: Literal["disable", "enable"]  # Enable/disable automatically including this RADIUS | Default: disable
    use_management_vdom: Literal["enable", "disable"]  # Enable/disable using management VDOM to send reque | Default: disable
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"]  # Enable/Disable switch-controller nas-ip dynamic to | Default: disable
    nas_ip: str  # IP address used to communicate with the RADIUS ser | Default: 0.0.0.0
    nas_id_type: Literal["legacy", "custom", "hostname"]  # NAS identifier type configuration | Default: legacy
    call_station_id_type: Literal["legacy", "IP", "MAC"]  # Calling & Called station identifier type configura | Default: legacy
    nas_id: str  # Custom NAS identifier. | MaxLen: 255
    acct_interim_interval: int  # Time in seconds between each accounting interim up | Default: 0 | Min: 60 | Max: 86400
    radius_coa: Literal["enable", "disable"]  # Enable to allow a mechanism to change the attribut | Default: disable
    radius_port: int  # RADIUS service port number. | Default: 0 | Min: 0 | Max: 65535
    h3c_compatibility: Literal["enable", "disable"]  # Enable/disable compatibility with the H3C, a mecha | Default: disable
    auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]  # Authentication methods/protocols permitted for thi | Default: auto
    source_ip: str  # Source IP address for communications to the RADIUS | MaxLen: 63
    source_ip_interface: str  # Source interface for communication with the RADIUS | MaxLen: 15
    username_case_sensitive: Literal["enable", "disable"]  # Enable/disable case sensitive user names. | Default: disable
    group_override_attr_type: Literal["filter-Id", "class"]  # RADIUS attribute type to override user group infor
    password_renewal: Literal["enable", "disable"]  # Enable/disable password renewal. | Default: enable
    require_message_authenticator: Literal["enable", "disable"]  # Require message authenticator in authentication re | Default: enable
    password_encoding: Literal["auto", "ISO-8859-1"]  # Password encoding. | Default: auto
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication password delimiter | Default: hyphen
    mac_case: Literal["uppercase", "lowercase"]  # MAC authentication case (default = lowercase). | Default: lowercase
    acct_all_servers: Literal["enable", "disable"]  # Enable/disable sending of accounting messages to a | Default: disable
    switch_controller_acct_fast_framedip_detect: int  # Switch controller accounting message Framed-IP det | Default: 2 | Min: 2 | Max: 600
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]  # RADIUS service type.
    transport_protocol: Literal["udp", "tcp", "tls"]  # Transport protocol to be used (default = udp). | Default: udp
    tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for TLS connect | Default: default
    ca_cert: str  # CA of server to trust under TLS. | MaxLen: 79
    client_cert: str  # Client certificate to use under TLS. | MaxLen: 35
    server_identity_check: Literal["enable", "disable"]  # Enable/disable RADIUS server identity check | Default: enable
    account_key_processing: Literal["same", "strip"]  # Account key processing operation. The FortiGate wi | Default: same
    account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"]  # Define subject identity field in certificate for u | Default: othername
    rsso: Literal["enable", "disable"]  # Enable/disable RADIUS based single sign on feature | Default: disable
    rsso_radius_server_port: int  # UDP port to listen on for RADIUS Start and Stop re | Default: 1813 | Min: 0 | Max: 65535
    rsso_radius_response: Literal["enable", "disable"]  # Enable/disable sending RADIUS response packets aft | Default: disable
    rsso_validate_request_secret: Literal["enable", "disable"]  # Enable/disable validating the RADIUS request share | Default: disable
    rsso_secret: str  # RADIUS secret used by the RADIUS accounting server | MaxLen: 31
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to extract the user end poi | Default: Calling-Station-Id
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to block a user.
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attribute that contains the profile group n | Default: Class
    sso_attribute_key: str  # Key prefix for SSO group value in the SSO attribut | MaxLen: 35
    sso_attribute_value_override: Literal["enable", "disable"]  # Enable/disable override old attribute value with n | Default: enable
    rsso_context_timeout: int  # Time in seconds before the logged out user is remo | Default: 28800 | Min: 0 | Max: 4294967295
    rsso_log_period: int  # Time interval in seconds that group event log mess | Default: 0 | Min: 0 | Max: 4294967295
    rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]  # Events to log. | Default: protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other
    rsso_flush_ip_session: Literal["enable", "disable"]  # Enable/disable flushing user IP sessions on RADIUS | Default: disable
    rsso_ep_one_ip_only: Literal["enable", "disable"]  # Enable/disable the replacement of old IP addresses | Default: disable
    delimiter: Literal["plus", "comma"]  # Configure delimiter to be used for separating prof | Default: plus
    accounting_server: list[RadiusAccountingserverItem]  # Additional accounting servers.


@final
class RadiusObject:
    """Typed FortiObject for user/radius with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # RADIUS server entry name. | MaxLen: 35
    name: str
    # Primary RADIUS server CN domain name or IP address. | MaxLen: 63
    server: str
    # Pre-shared secret key used to access the primary RADIUS serv | MaxLen: 128
    secret: str
    # Secondary RADIUS CN domain name or IP address. | MaxLen: 63
    secondary_server: str
    # Secret key to access the secondary server. | MaxLen: 128
    secondary_secret: str
    # Tertiary RADIUS CN domain name or IP address. | MaxLen: 63
    tertiary_server: str
    # Secret key to access the tertiary server. | MaxLen: 128
    tertiary_secret: str
    # Time in seconds to retry connecting server. | Default: 5 | Min: 1 | Max: 300
    timeout: int
    # Time for which server reachability is cached so that when a | Default: 300 | Min: 0 | Max: 600
    status_ttl: int
    # Enable/disable automatically including this RADIUS server in | Default: disable
    all_usergroup: Literal["disable", "enable"]
    # Enable/disable using management VDOM to send requests. | Default: disable
    use_management_vdom: Literal["enable", "disable"]
    # Enable/Disable switch-controller nas-ip dynamic to dynamical | Default: disable
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"]
    # IP address used to communicate with the RADIUS server and us | Default: 0.0.0.0
    nas_ip: str
    # NAS identifier type configuration (default = legacy). | Default: legacy
    nas_id_type: Literal["legacy", "custom", "hostname"]
    # Calling & Called station identifier type configuration | Default: legacy
    call_station_id_type: Literal["legacy", "IP", "MAC"]
    # Custom NAS identifier. | MaxLen: 255
    nas_id: str
    # Time in seconds between each accounting interim update messa | Default: 0 | Min: 60 | Max: 86400
    acct_interim_interval: int
    # Enable to allow a mechanism to change the attributes of an a | Default: disable
    radius_coa: Literal["enable", "disable"]
    # RADIUS service port number. | Default: 0 | Min: 0 | Max: 65535
    radius_port: int
    # Enable/disable compatibility with the H3C, a mechanism that | Default: disable
    h3c_compatibility: Literal["enable", "disable"]
    # Authentication methods/protocols permitted for this RADIUS s | Default: auto
    auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]
    # Source IP address for communications to the RADIUS server. | MaxLen: 63
    source_ip: str
    # Source interface for communication with the RADIUS server. | MaxLen: 15
    source_ip_interface: str
    # Enable/disable case sensitive user names. | Default: disable
    username_case_sensitive: Literal["enable", "disable"]
    # RADIUS attribute type to override user group information.
    group_override_attr_type: Literal["filter-Id", "class"]
    # Enable/disable password renewal. | Default: enable
    password_renewal: Literal["enable", "disable"]
    # Require message authenticator in authentication response. | Default: enable
    require_message_authenticator: Literal["enable", "disable"]
    # Password encoding. | Default: auto
    password_encoding: Literal["auto", "ISO-8859-1"]
    # MAC authentication username delimiter (default = hyphen). | Default: hyphen
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC authentication password delimiter (default = hyphen). | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC authentication case (default = lowercase). | Default: lowercase
    mac_case: Literal["uppercase", "lowercase"]
    # Enable/disable sending of accounting messages to all configu | Default: disable
    acct_all_servers: Literal["enable", "disable"]
    # Switch controller accounting message Framed-IP detection fro | Default: 2 | Min: 2 | Max: 600
    switch_controller_acct_fast_framedip_detect: int
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    # RADIUS service type.
    switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]
    # Transport protocol to be used (default = udp). | Default: udp
    transport_protocol: Literal["udp", "tcp", "tls"]
    # Minimum supported protocol version for TLS connections | Default: default
    tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # CA of server to trust under TLS. | MaxLen: 79
    ca_cert: str
    # Client certificate to use under TLS. | MaxLen: 35
    client_cert: str
    # Enable/disable RADIUS server identity check | Default: enable
    server_identity_check: Literal["enable", "disable"]
    # Account key processing operation. The FortiGate will keep ei | Default: same
    account_key_processing: Literal["same", "strip"]
    # Define subject identity field in certificate for user access | Default: othername
    account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"]
    # Enable/disable RADIUS based single sign on feature. | Default: disable
    rsso: Literal["enable", "disable"]
    # UDP port to listen on for RADIUS Start and Stop records. | Default: 1813 | Min: 0 | Max: 65535
    rsso_radius_server_port: int
    # Enable/disable sending RADIUS response packets after receivi | Default: disable
    rsso_radius_response: Literal["enable", "disable"]
    # Enable/disable validating the RADIUS request shared secret i | Default: disable
    rsso_validate_request_secret: Literal["enable", "disable"]
    # RADIUS secret used by the RADIUS accounting server. | MaxLen: 31
    rsso_secret: str
    # RADIUS attributes used to extract the user end point identif | Default: Calling-Station-Id
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # RADIUS attributes used to block a user.
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # RADIUS attribute that contains the profile group name to be | Default: Class
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # Key prefix for SSO group value in the SSO attribute. | MaxLen: 35
    sso_attribute_key: str
    # Enable/disable override old attribute value with new value f | Default: enable
    sso_attribute_value_override: Literal["enable", "disable"]
    # Time in seconds before the logged out user is removed from t | Default: 28800 | Min: 0 | Max: 4294967295
    rsso_context_timeout: int
    # Time interval in seconds that group event log messages will | Default: 0 | Min: 0 | Max: 4294967295
    rsso_log_period: int
    # Events to log. | Default: protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other
    rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]
    # Enable/disable flushing user IP sessions on RADIUS accountin | Default: disable
    rsso_flush_ip_session: Literal["enable", "disable"]
    # Enable/disable the replacement of old IP addresses with new | Default: disable
    rsso_ep_one_ip_only: Literal["enable", "disable"]
    # Configure delimiter to be used for separating profile group | Default: plus
    delimiter: Literal["plus", "comma"]
    # Additional accounting servers.
    accounting_server: list[RadiusAccountingserverObject]
    
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
    def to_dict(self) -> RadiusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Radius:
    """
    Configure RADIUS server entries.
    
    Path: user/radius
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
    ) -> RadiusObject: ...
    
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
    ) -> RadiusObject: ...
    
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
    ) -> FortiObjectList[RadiusObject]: ...
    
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
    ) -> RadiusObject: ...
    
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
    ) -> RadiusObject: ...
    
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
    ) -> FortiObjectList[RadiusObject]: ...
    
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
    ) -> RadiusObject: ...
    
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
    ) -> RadiusObject: ...
    
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
    ) -> FortiObjectList[RadiusObject]: ...
    
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
    ) -> RadiusObject | list[RadiusObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RadiusObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RadiusObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RadiusObject: ...
    
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
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Radius",
    "RadiusPayload",
    "RadiusResponse",
    "RadiusObject",
]