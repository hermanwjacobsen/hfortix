from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VipPayload(TypedDict, total=False):
    """
    Type hints for firewall/vip payload fields.
    
    Configure virtual IP for IPv4.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: mapped-addr)
        - :class:`~.system.interface.InterfaceEndpoint` (via: extintf)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)

    **Usage:**
        payload: VipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Virtual IP name. | MaxLen: 79
    id: int  # Custom defined ID. | Default: 0 | Min: 0 | Max: 65535
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    comment: str  # Comment. | MaxLen: 255
    type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]  # Configure a static NAT, load balance, server load | Default: static-nat
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]  # Protocol to be load balanced by the virtual server
    dns_mapping_ttl: int  # DNS mapping TTL | Default: 0 | Min: 0 | Max: 604800
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    src_filter: list[dict[str, Any]]  # Source address filter. Each address must be either
    src_vip_filter: Literal["disable", "enable"]  # Enable/disable use of 'src-filter' to match destin | Default: disable
    service: list[dict[str, Any]]  # Service name.
    extip: str  # IP address or address range on the external interf
    extaddr: list[dict[str, Any]]  # External FQDN address name.
    h2_support: Literal["enable", "disable"]  # Enable/disable HTTP2 support (default = enable). | Default: enable
    h3_support: Literal["enable", "disable"]  # Enable/disable HTTP3/QUIC support | Default: disable
    quic: str  # QUIC setting.
    nat44: Literal["disable", "enable"]  # Enable/disable NAT44. | Default: enable
    nat46: Literal["disable", "enable"]  # Enable/disable NAT46. | Default: disable
    add_nat46_route: Literal["disable", "enable"]  # Enable/disable adding NAT46 route. | Default: enable
    mappedip: list[dict[str, Any]]  # IP address or address range on the destination net
    mapped_addr: str  # Mapped FQDN address name. | MaxLen: 79
    extintf: str  # Interface connected to the source network that rec | MaxLen: 35
    arp_reply: Literal["disable", "enable"]  # Enable to respond to ARP requests for this virtual | Default: enable
    http_redirect: Literal["enable", "disable"]  # Enable/disable redirection of HTTP to HTTPS. | Default: disable
    persistence: Literal["none", "http-cookie", "ssl-session-id"]  # Configure how to make sure that clients connect to | Default: none
    nat_source_vip: Literal["disable", "enable"]  # Enable/disable forcing the source NAT mapped IP to | Default: disable
    portforward: Literal["disable", "enable"]  # Enable/disable port forwarding. | Default: disable
    status: Literal["disable", "enable"]  # Enable/disable VIP. | Default: enable
    protocol: Literal["tcp", "udp", "sctp", "icmp"]  # Protocol to use when forwarding packets. | Default: tcp
    extport: str  # Incoming port number range that you want to map to
    mappedport: str  # Port number range on the destination network to wh
    gratuitous_arp_interval: int  # Enable to have the VIP send gratuitous ARPs. 0=dis | Default: 0 | Min: 5 | Max: 8640000
    srcintf_filter: list[dict[str, Any]]  # Interfaces to which the VIP applies. Separate the
    portmapping_type: Literal["1-to-1", "m-to-n"]  # Port mapping type. | Default: 1-to-1
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action for an empty client certificate. | Default: block
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable detecting device type by HTTP user- | Default: enable
    client_cert: Literal["disable", "enable"]  # Enable/disable requesting client certificate. | Default: enable
    realservers: list[dict[str, Any]]  # Select the real servers that this server load bala
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across virtual servers. | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    http_multiplex: Literal["enable", "disable"]  # Enable/disable HTTP multiplexing. | Default: disable
    http_multiplex_ttl: int  # Time-to-live for idle connections to servers. | Default: 15 | Min: 0 | Max: 2147483647
    http_multiplex_max_request: int  # Maximum number of requests that a multiplex server | Default: 0 | Min: 0 | Max: 2147483647
    http_multiplex_max_concurrent_request: int  # Maximum number of concurrent requests that a multi | Default: 0 | Min: 0 | Max: 2147483647
    http_ip_header: Literal["enable", "disable"]  # For HTTP multiplexing, enable to add the original | Default: disable
    http_ip_header_name: str  # For HTTP multiplexing, enter a custom HTTPS header | MaxLen: 35
    outlook_web_access: Literal["disable", "enable"]  # Enable to add the Front-End-Https header for Micro | Default: disable
    weblogic_server: Literal["disable", "enable"]  # Enable to add an HTTP header to indicate SSL offlo | Default: disable
    websphere_server: Literal["disable", "enable"]  # Enable to add an HTTP header to indicate SSL offlo | Default: disable
    ssl_mode: Literal["half", "full"]  # Apply SSL offloading between the client and the Fo | Default: half
    ssl_certificate: list[dict[str, Any]]  # Name of the certificate to use for SSL handshake.
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low", "custom"]  # Permitted encryption algorithms for SSL sessions a | Default: high
    ssl_cipher_suites: list[dict[str, Any]]  # SSL/TLS cipher suites acceptable from a client, or
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]  # Permitted encryption algorithms for the server sid | Default: client
    ssl_server_cipher_suites: list[dict[str, Any]]  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_pfs: Literal["require", "deny", "allow"]  # Select the cipher suites that can be used for SSL | Default: require
    ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a client. | Default: tls-1.1
    ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a client. | Default: tls-1.3
    ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]  # Lowest SSL/TLS version acceptable from a server. U | Default: client
    ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]  # Highest SSL/TLS version acceptable from a server. | Default: client
    ssl_accept_ffdhe_groups: Literal["enable", "disable"]  # Enable/disable FFDHE cipher suite for SSL key exch | Default: enable
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid CB | Default: enable
    ssl_client_fallback: Literal["disable", "enable"]  # Enable/disable support for preventing Downgrade At | Default: enable
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]  # Allow, deny, or require secure renegotiation of cl | Default: secure
    ssl_client_session_state_type: Literal["disable", "time", "count", "both"]  # How to expire SSL sessions for the segment of the | Default: both
    ssl_client_session_state_timeout: int  # Number of minutes to keep client to FortiGate SSL | Default: 30 | Min: 1 | Max: 14400
    ssl_client_session_state_max: int  # Maximum number of client to FortiGate SSL session | Default: 1000 | Min: 1 | Max: 10000
    ssl_client_rekey_count: int  # Maximum length of data in MB before triggering a c | Default: 0 | Min: 200 | Max: 1048576
    ssl_server_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable
    ssl_server_session_state_type: Literal["disable", "time", "count", "both"]  # How to expire SSL sessions for the segment of the | Default: both
    ssl_server_session_state_timeout: int  # Number of minutes to keep FortiGate to Server SSL | Default: 60 | Min: 1 | Max: 14400
    ssl_server_session_state_max: int  # Maximum number of FortiGate to Server SSL session | Default: 100 | Min: 1 | Max: 10000
    ssl_http_location_conversion: Literal["enable", "disable"]  # Enable to replace HTTP with HTTPS in the reply's L | Default: disable
    ssl_http_match_host: Literal["enable", "disable"]  # Enable/disable HTTP host matching for location con | Default: enable
    ssl_hpkp: Literal["disable", "enable", "report-only"]  # Enable/disable including HPKP header in response. | Default: disable
    ssl_hpkp_primary: str  # Certificate to generate primary HPKP pin from. | MaxLen: 79
    ssl_hpkp_backup: str  # Certificate to generate backup HPKP pin from. | MaxLen: 79
    ssl_hpkp_age: int  # Number of seconds the client should honor the HPKP | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hpkp_report_uri: str  # URL to report HPKP violations to. | MaxLen: 255
    ssl_hpkp_include_subdomains: Literal["disable", "enable"]  # Indicate that HPKP header applies to all subdomain | Default: disable
    ssl_hsts: Literal["disable", "enable"]  # Enable/disable including HSTS header in response. | Default: disable
    ssl_hsts_age: int  # Number of seconds the client should honor the HSTS | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hsts_include_subdomains: Literal["disable", "enable"]  # Indicate that HSTS header applies to all subdomain | Default: disable
    monitor: list[dict[str, Any]]  # Name of the health check monitor to use when polli
    max_embryonic_connections: int  # Maximum number of incomplete connections. | Default: 1000 | Min: 0 | Max: 100000
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    ipv6_mappedip: str  # Range of mapped IPv6 addresses. Specify the start
    ipv6_mappedport: str  # IPv6 port number range on the destination network
    one_click_gslb_server: Literal["disable", "enable"]  # Enable/disable one click GSLB server integration w | Default: disable
    gslb_hostname: str  # Hostname to use within the configured FortiGSLB do | MaxLen: 35
    gslb_domain_name: str  # Domain to use when integrating with FortiGSLB. | MaxLen: 255
    gslb_public_ips: list[dict[str, Any]]  # Publicly accessible IP addresses for the FortiGSLB

# Nested TypedDicts for table field children (dict mode)

class VipSrcfilterItem(TypedDict):
    """Type hints for src-filter table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    range: str  # Source-filter range. | MaxLen: 79


class VipServiceItem(TypedDict):
    """Type hints for service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Service name. | MaxLen: 79


class VipExtaddrItem(TypedDict):
    """Type hints for extaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class VipMappedipItem(TypedDict):
    """Type hints for mappedip table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    range: str  # Mapped IP range. | MaxLen: 79


class VipSrcintffilterItem(TypedDict):
    """Type hints for srcintf-filter table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Interface name. | MaxLen: 79


class VipRealserversItem(TypedDict):
    """Type hints for realservers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Real server ID. | Default: 0 | Min: 0 | Max: 4294967295
    type: Literal["ip", "address"]  # Type of address. | Default: ip
    address: str  # Dynamic address of the real server. | MaxLen: 79
    ip: str  # IP address of the real server.
    port: int  # Port for communicating with the real server. Requi | Default: 0 | Min: 1 | Max: 65535
    status: Literal["active", "standby", "disable"]  # Set the status of the real server to active so tha | Default: active
    weight: int  # Weight of the real server. If weighted load balanc | Default: 1 | Min: 1 | Max: 255
    holddown_interval: int  # Time in seconds that the system waits before re-ac | Default: 300 | Min: 30 | Max: 65535
    healthcheck: Literal["disable", "enable", "vip"]  # Enable to check the responsiveness of the real ser | Default: vip
    http_host: str  # HTTP server domain name in HTTP header. | MaxLen: 63
    translate_host: Literal["enable", "disable"]  # Enable/disable translation of hostname/IP from vir | Default: enable
    max_connections: int  # Max number of active connections that can be direc | Default: 0 | Min: 0 | Max: 2147483647
    monitor: str  # Name of the health check monitor to use when polli
    client_ip: str  # Only clients in this IP range can connect to this
    verify_cert: Literal["enable", "disable"]  # Enable/disable certificate verification of the rea | Default: enable


class VipSslcertificateItem(TypedDict):
    """Type hints for ssl-certificate table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | MaxLen: 79


class VipSslciphersuitesItem(TypedDict):
    """Type hints for ssl-cipher-suites table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    priority: int  # SSL/TLS cipher suites priority. | Default: 0 | Min: 0 | Max: 4294967295
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]  # Cipher suite name.
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # SSL/TLS versions that the cipher suite can be used | Default: ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3


class VipSslserverciphersuitesItem(TypedDict):
    """Type hints for ssl-server-cipher-suites table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    priority: int  # SSL/TLS cipher suites priority. | Default: 0 | Min: 0 | Max: 4294967295
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]  # Cipher suite name.
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # SSL/TLS versions that the cipher suite can be used | Default: ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3


class VipMonitorItem(TypedDict):
    """Type hints for monitor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Health monitor name. | MaxLen: 79


class VipGslbpublicipsItem(TypedDict):
    """Type hints for gslb-public-ips table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    index: int  # Index of this public IP setting. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # The publicly accessible IP address. | Default: 0.0.0.0


# Nested classes for table field children (object mode)

@final
class VipSrcfilterObject:
    """Typed object for src-filter table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Source-filter range. | MaxLen: 79
    range: str
    
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
class VipServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name. | MaxLen: 79
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
class VipExtaddrObject:
    """Typed object for extaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class VipMappedipObject:
    """Typed object for mappedip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Mapped IP range. | MaxLen: 79
    range: str
    
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
class VipSrcintffilterObject:
    """Typed object for srcintf-filter table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    interface_name: str
    
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
class VipRealserversObject:
    """Typed object for realservers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Real server ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Type of address. | Default: ip
    type: Literal["ip", "address"]
    # Dynamic address of the real server. | MaxLen: 79
    address: str
    # IP address of the real server.
    ip: str
    # Port for communicating with the real server. Required if por | Default: 0 | Min: 1 | Max: 65535
    port: int
    # Set the status of the real server to active so that it can a | Default: active
    status: Literal["active", "standby", "disable"]
    # Weight of the real server. If weighted load balancing is ena | Default: 1 | Min: 1 | Max: 255
    weight: int
    # Time in seconds that the system waits before re-activating a | Default: 300 | Min: 30 | Max: 65535
    holddown_interval: int
    # Enable to check the responsiveness of the real server before | Default: vip
    healthcheck: Literal["disable", "enable", "vip"]
    # HTTP server domain name in HTTP header. | MaxLen: 63
    http_host: str
    # Enable/disable translation of hostname/IP from virtual serve | Default: enable
    translate_host: Literal["enable", "disable"]
    # Max number of active connections that can be directed to the | Default: 0 | Min: 0 | Max: 2147483647
    max_connections: int
    # Name of the health check monitor to use when polling to dete
    monitor: str
    # Only clients in this IP range can connect to this real serve
    client_ip: str
    # Enable/disable certificate verification of the real server. | Default: enable
    verify_cert: Literal["enable", "disable"]
    
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
class VipSslcertificateObject:
    """Typed object for ssl-certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list. | MaxLen: 79
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
class VipSslciphersuitesObject:
    """Typed object for ssl-cipher-suites table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SSL/TLS cipher suites priority. | Default: 0 | Min: 0 | Max: 4294967295
    priority: int
    # Cipher suite name.
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]
    # SSL/TLS versions that the cipher suite can be used with. | Default: ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    
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
class VipSslserverciphersuitesObject:
    """Typed object for ssl-server-cipher-suites table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SSL/TLS cipher suites priority. | Default: 0 | Min: 0 | Max: 4294967295
    priority: int
    # Cipher suite name.
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]
    # SSL/TLS versions that the cipher suite can be used with. | Default: ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    
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
class VipMonitorObject:
    """Typed object for monitor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Health monitor name. | MaxLen: 79
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
class VipGslbpublicipsObject:
    """Typed object for gslb-public-ips table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Index of this public IP setting. | Default: 0 | Min: 0 | Max: 4294967295
    index: int
    # The publicly accessible IP address. | Default: 0.0.0.0
    ip: str
    
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
class VipResponse(TypedDict):
    """
    Type hints for firewall/vip API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Virtual IP name. | MaxLen: 79
    id: int  # Custom defined ID. | Default: 0 | Min: 0 | Max: 65535
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    comment: str  # Comment. | MaxLen: 255
    type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]  # Configure a static NAT, load balance, server load | Default: static-nat
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]  # Protocol to be load balanced by the virtual server
    dns_mapping_ttl: int  # DNS mapping TTL | Default: 0 | Min: 0 | Max: 604800
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    src_filter: list[VipSrcfilterItem]  # Source address filter. Each address must be either
    src_vip_filter: Literal["disable", "enable"]  # Enable/disable use of 'src-filter' to match destin | Default: disable
    service: list[VipServiceItem]  # Service name.
    extip: str  # IP address or address range on the external interf
    extaddr: list[VipExtaddrItem]  # External FQDN address name.
    h2_support: Literal["enable", "disable"]  # Enable/disable HTTP2 support (default = enable). | Default: enable
    h3_support: Literal["enable", "disable"]  # Enable/disable HTTP3/QUIC support | Default: disable
    quic: str  # QUIC setting.
    nat44: Literal["disable", "enable"]  # Enable/disable NAT44. | Default: enable
    nat46: Literal["disable", "enable"]  # Enable/disable NAT46. | Default: disable
    add_nat46_route: Literal["disable", "enable"]  # Enable/disable adding NAT46 route. | Default: enable
    mappedip: list[VipMappedipItem]  # IP address or address range on the destination net
    mapped_addr: str  # Mapped FQDN address name. | MaxLen: 79
    extintf: str  # Interface connected to the source network that rec | MaxLen: 35
    arp_reply: Literal["disable", "enable"]  # Enable to respond to ARP requests for this virtual | Default: enable
    http_redirect: Literal["enable", "disable"]  # Enable/disable redirection of HTTP to HTTPS. | Default: disable
    persistence: Literal["none", "http-cookie", "ssl-session-id"]  # Configure how to make sure that clients connect to | Default: none
    nat_source_vip: Literal["disable", "enable"]  # Enable/disable forcing the source NAT mapped IP to | Default: disable
    portforward: Literal["disable", "enable"]  # Enable/disable port forwarding. | Default: disable
    status: Literal["disable", "enable"]  # Enable/disable VIP. | Default: enable
    protocol: Literal["tcp", "udp", "sctp", "icmp"]  # Protocol to use when forwarding packets. | Default: tcp
    extport: str  # Incoming port number range that you want to map to
    mappedport: str  # Port number range on the destination network to wh
    gratuitous_arp_interval: int  # Enable to have the VIP send gratuitous ARPs. 0=dis | Default: 0 | Min: 5 | Max: 8640000
    srcintf_filter: list[VipSrcintffilterItem]  # Interfaces to which the VIP applies. Separate the
    portmapping_type: Literal["1-to-1", "m-to-n"]  # Port mapping type. | Default: 1-to-1
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]  # Action for an empty client certificate. | Default: block
    user_agent_detect: Literal["disable", "enable"]  # Enable/disable detecting device type by HTTP user- | Default: enable
    client_cert: Literal["disable", "enable"]  # Enable/disable requesting client certificate. | Default: enable
    realservers: list[VipRealserversItem]  # Select the real servers that this server load bala
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across virtual servers. | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    http_multiplex: Literal["enable", "disable"]  # Enable/disable HTTP multiplexing. | Default: disable
    http_multiplex_ttl: int  # Time-to-live for idle connections to servers. | Default: 15 | Min: 0 | Max: 2147483647
    http_multiplex_max_request: int  # Maximum number of requests that a multiplex server | Default: 0 | Min: 0 | Max: 2147483647
    http_multiplex_max_concurrent_request: int  # Maximum number of concurrent requests that a multi | Default: 0 | Min: 0 | Max: 2147483647
    http_ip_header: Literal["enable", "disable"]  # For HTTP multiplexing, enable to add the original | Default: disable
    http_ip_header_name: str  # For HTTP multiplexing, enter a custom HTTPS header | MaxLen: 35
    outlook_web_access: Literal["disable", "enable"]  # Enable to add the Front-End-Https header for Micro | Default: disable
    weblogic_server: Literal["disable", "enable"]  # Enable to add an HTTP header to indicate SSL offlo | Default: disable
    websphere_server: Literal["disable", "enable"]  # Enable to add an HTTP header to indicate SSL offlo | Default: disable
    ssl_mode: Literal["half", "full"]  # Apply SSL offloading between the client and the Fo | Default: half
    ssl_certificate: list[VipSslcertificateItem]  # Name of the certificate to use for SSL handshake.
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low", "custom"]  # Permitted encryption algorithms for SSL sessions a | Default: high
    ssl_cipher_suites: list[VipSslciphersuitesItem]  # SSL/TLS cipher suites acceptable from a client, or
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]  # Permitted encryption algorithms for the server sid | Default: client
    ssl_server_cipher_suites: list[VipSslserverciphersuitesItem]  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_pfs: Literal["require", "deny", "allow"]  # Select the cipher suites that can be used for SSL | Default: require
    ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a client. | Default: tls-1.1
    ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a client. | Default: tls-1.3
    ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]  # Lowest SSL/TLS version acceptable from a server. U | Default: client
    ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]  # Highest SSL/TLS version acceptable from a server. | Default: client
    ssl_accept_ffdhe_groups: Literal["enable", "disable"]  # Enable/disable FFDHE cipher suite for SSL key exch | Default: enable
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid CB | Default: enable
    ssl_client_fallback: Literal["disable", "enable"]  # Enable/disable support for preventing Downgrade At | Default: enable
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]  # Allow, deny, or require secure renegotiation of cl | Default: secure
    ssl_client_session_state_type: Literal["disable", "time", "count", "both"]  # How to expire SSL sessions for the segment of the | Default: both
    ssl_client_session_state_timeout: int  # Number of minutes to keep client to FortiGate SSL | Default: 30 | Min: 1 | Max: 14400
    ssl_client_session_state_max: int  # Maximum number of client to FortiGate SSL session | Default: 1000 | Min: 1 | Max: 10000
    ssl_client_rekey_count: int  # Maximum length of data in MB before triggering a c | Default: 0 | Min: 200 | Max: 1048576
    ssl_server_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable
    ssl_server_session_state_type: Literal["disable", "time", "count", "both"]  # How to expire SSL sessions for the segment of the | Default: both
    ssl_server_session_state_timeout: int  # Number of minutes to keep FortiGate to Server SSL | Default: 60 | Min: 1 | Max: 14400
    ssl_server_session_state_max: int  # Maximum number of FortiGate to Server SSL session | Default: 100 | Min: 1 | Max: 10000
    ssl_http_location_conversion: Literal["enable", "disable"]  # Enable to replace HTTP with HTTPS in the reply's L | Default: disable
    ssl_http_match_host: Literal["enable", "disable"]  # Enable/disable HTTP host matching for location con | Default: enable
    ssl_hpkp: Literal["disable", "enable", "report-only"]  # Enable/disable including HPKP header in response. | Default: disable
    ssl_hpkp_primary: str  # Certificate to generate primary HPKP pin from. | MaxLen: 79
    ssl_hpkp_backup: str  # Certificate to generate backup HPKP pin from. | MaxLen: 79
    ssl_hpkp_age: int  # Number of seconds the client should honor the HPKP | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hpkp_report_uri: str  # URL to report HPKP violations to. | MaxLen: 255
    ssl_hpkp_include_subdomains: Literal["disable", "enable"]  # Indicate that HPKP header applies to all subdomain | Default: disable
    ssl_hsts: Literal["disable", "enable"]  # Enable/disable including HSTS header in response. | Default: disable
    ssl_hsts_age: int  # Number of seconds the client should honor the HSTS | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hsts_include_subdomains: Literal["disable", "enable"]  # Indicate that HSTS header applies to all subdomain | Default: disable
    monitor: list[VipMonitorItem]  # Name of the health check monitor to use when polli
    max_embryonic_connections: int  # Maximum number of incomplete connections. | Default: 1000 | Min: 0 | Max: 100000
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    ipv6_mappedip: str  # Range of mapped IPv6 addresses. Specify the start
    ipv6_mappedport: str  # IPv6 port number range on the destination network
    one_click_gslb_server: Literal["disable", "enable"]  # Enable/disable one click GSLB server integration w | Default: disable
    gslb_hostname: str  # Hostname to use within the configured FortiGSLB do | MaxLen: 35
    gslb_domain_name: str  # Domain to use when integrating with FortiGSLB. | MaxLen: 255
    gslb_public_ips: list[VipGslbpublicipsItem]  # Publicly accessible IP addresses for the FortiGSLB


@final
class VipObject:
    """Typed FortiObject for firewall/vip with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Virtual IP name. | MaxLen: 79
    name: str
    # Custom defined ID. | Default: 0 | Min: 0 | Max: 65535
    id: int
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Comment. | MaxLen: 255
    comment: str
    # Configure a static NAT, load balance, server load balance, a | Default: static-nat
    type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]
    # Protocol to be load balanced by the virtual server
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]
    # DNS mapping TTL | Default: 0 | Min: 0 | Max: 604800
    dns_mapping_ttl: int
    # Method used to distribute sessions to real servers. | Default: static
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]
    # Source address filter. Each address must be either an IP/sub
    src_filter: list[VipSrcfilterObject]
    # Enable/disable use of 'src-filter' to match destinations for | Default: disable
    src_vip_filter: Literal["disable", "enable"]
    # Service name.
    service: list[VipServiceObject]
    # IP address or address range on the external interface that y
    extip: str
    # External FQDN address name.
    extaddr: list[VipExtaddrObject]
    # Enable/disable HTTP2 support (default = enable). | Default: enable
    h2_support: Literal["enable", "disable"]
    # Enable/disable HTTP3/QUIC support (default = disable). | Default: disable
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Enable/disable NAT44. | Default: enable
    nat44: Literal["disable", "enable"]
    # Enable/disable NAT46. | Default: disable
    nat46: Literal["disable", "enable"]
    # Enable/disable adding NAT46 route. | Default: enable
    add_nat46_route: Literal["disable", "enable"]
    # IP address or address range on the destination network to wh
    mappedip: list[VipMappedipObject]
    # Mapped FQDN address name. | MaxLen: 79
    mapped_addr: str
    # Interface connected to the source network that receives the | MaxLen: 35
    extintf: str
    # Enable to respond to ARP requests for this virtual IP addres | Default: enable
    arp_reply: Literal["disable", "enable"]
    # Enable/disable redirection of HTTP to HTTPS. | Default: disable
    http_redirect: Literal["enable", "disable"]
    # Configure how to make sure that clients connect to the same | Default: none
    persistence: Literal["none", "http-cookie", "ssl-session-id"]
    # Enable/disable forcing the source NAT mapped IP to the exter | Default: disable
    nat_source_vip: Literal["disable", "enable"]
    # Enable/disable port forwarding. | Default: disable
    portforward: Literal["disable", "enable"]
    # Enable/disable VIP. | Default: enable
    status: Literal["disable", "enable"]
    # Protocol to use when forwarding packets. | Default: tcp
    protocol: Literal["tcp", "udp", "sctp", "icmp"]
    # Incoming port number range that you want to map to a port nu
    extport: str
    # Port number range on the destination network to which the ex
    mappedport: str
    # Enable to have the VIP send gratuitous ARPs. 0=disabled. Set | Default: 0 | Min: 5 | Max: 8640000
    gratuitous_arp_interval: int
    # Interfaces to which the VIP applies. Separate the names with
    srcintf_filter: list[VipSrcintffilterObject]
    # Port mapping type. | Default: 1-to-1
    portmapping_type: Literal["1-to-1", "m-to-n"]
    # Action for an empty client certificate. | Default: block
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Enable/disable detecting device type by HTTP user-agent if n | Default: enable
    user_agent_detect: Literal["disable", "enable"]
    # Enable/disable requesting client certificate. | Default: enable
    client_cert: Literal["disable", "enable"]
    # Select the real servers that this server load balancing VIP
    realservers: list[VipRealserversObject]
    # Enable/disable use of HTTP cookie domain from host field in | Default: disable
    http_cookie_domain_from_host: Literal["disable", "enable"]
    # Domain that HTTP cookie persistence should apply to. | MaxLen: 35
    http_cookie_domain: str
    # Limit HTTP cookie persistence to the specified path. | MaxLen: 35
    http_cookie_path: str
    # Generation of HTTP cookie to be accepted. Changing invalidat | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_generation: int
    # Time in minutes that client web browsers should keep a cooki | Default: 60 | Min: 0 | Max: 525600
    http_cookie_age: int
    # Control sharing of cookies across virtual servers. Use of sa | Default: same-ip
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are | Default: disable
    https_cookie_secure: Literal["disable", "enable"]
    # Enable/disable HTTP multiplexing. | Default: disable
    http_multiplex: Literal["enable", "disable"]
    # Time-to-live for idle connections to servers. | Default: 15 | Min: 0 | Max: 2147483647
    http_multiplex_ttl: int
    # Maximum number of requests that a multiplex server can handl | Default: 0 | Min: 0 | Max: 2147483647
    http_multiplex_max_request: int
    # Maximum number of concurrent requests that a multiplex serve | Default: 0 | Min: 0 | Max: 2147483647
    http_multiplex_max_concurrent_request: int
    # For HTTP multiplexing, enable to add the original client IP | Default: disable
    http_ip_header: Literal["enable", "disable"]
    # For HTTP multiplexing, enter a custom HTTPS header name. The | MaxLen: 35
    http_ip_header_name: str
    # Enable to add the Front-End-Https header for Microsoft Outlo | Default: disable
    outlook_web_access: Literal["disable", "enable"]
    # Enable to add an HTTP header to indicate SSL offloading for | Default: disable
    weblogic_server: Literal["disable", "enable"]
    # Enable to add an HTTP header to indicate SSL offloading for | Default: disable
    websphere_server: Literal["disable", "enable"]
    # Apply SSL offloading between the client and the FortiGate | Default: half
    ssl_mode: Literal["half", "full"]
    # Name of the certificate to use for SSL handshake.
    ssl_certificate: list[VipSslcertificateObject]
    # Number of bits to use in the Diffie-Hellman exchange for RSA | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for SSL sessions according t | Default: high
    ssl_algorithm: Literal["high", "medium", "low", "custom"]
    # SSL/TLS cipher suites acceptable from a client, ordered by p
    ssl_cipher_suites: list[VipSslciphersuitesObject]
    # Permitted encryption algorithms for the server side of SSL f | Default: client
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]
    # SSL/TLS cipher suites to offer to a server, ordered by prior
    ssl_server_cipher_suites: list[VipSslserverciphersuitesObject]
    # Select the cipher suites that can be used for SSL perfect fo | Default: require
    ssl_pfs: Literal["require", "deny", "allow"]
    # Lowest SSL/TLS version acceptable from a client. | Default: tls-1.1
    ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a client. | Default: tls-1.3
    ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Lowest SSL/TLS version acceptable from a server. Use the cli | Default: client
    ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    # Highest SSL/TLS version acceptable from a server. Use the cl | Default: client
    ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    # Enable/disable FFDHE cipher suite for SSL key exchange. | Default: enable
    ssl_accept_ffdhe_groups: Literal["enable", "disable"]
    # Enable/disable sending empty fragments to avoid CBC IV attac | Default: enable
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Enable/disable support for preventing Downgrade Attacks on c | Default: enable
    ssl_client_fallback: Literal["disable", "enable"]
    # Allow, deny, or require secure renegotiation of client sessi | Default: secure
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]
    # How to expire SSL sessions for the segment of the SSL connec | Default: both
    ssl_client_session_state_type: Literal["disable", "time", "count", "both"]
    # Number of minutes to keep client to FortiGate SSL session st | Default: 30 | Min: 1 | Max: 14400
    ssl_client_session_state_timeout: int
    # Maximum number of client to FortiGate SSL session states to | Default: 1000 | Min: 1 | Max: 10000
    ssl_client_session_state_max: int
    # Maximum length of data in MB before triggering a client reke | Default: 0 | Min: 200 | Max: 1048576
    ssl_client_rekey_count: int
    # Enable/disable secure renegotiation to comply with RFC 5746. | Default: enable
    ssl_server_renegotiation: Literal["enable", "disable"]
    # How to expire SSL sessions for the segment of the SSL connec | Default: both
    ssl_server_session_state_type: Literal["disable", "time", "count", "both"]
    # Number of minutes to keep FortiGate to Server SSL session st | Default: 60 | Min: 1 | Max: 14400
    ssl_server_session_state_timeout: int
    # Maximum number of FortiGate to Server SSL session states to | Default: 100 | Min: 1 | Max: 10000
    ssl_server_session_state_max: int
    # Enable to replace HTTP with HTTPS in the reply's Location HT | Default: disable
    ssl_http_location_conversion: Literal["enable", "disable"]
    # Enable/disable HTTP host matching for location conversion. | Default: enable
    ssl_http_match_host: Literal["enable", "disable"]
    # Enable/disable including HPKP header in response. | Default: disable
    ssl_hpkp: Literal["disable", "enable", "report-only"]
    # Certificate to generate primary HPKP pin from. | MaxLen: 79
    ssl_hpkp_primary: str
    # Certificate to generate backup HPKP pin from. | MaxLen: 79
    ssl_hpkp_backup: str
    # Number of seconds the client should honor the HPKP setting. | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hpkp_age: int
    # URL to report HPKP violations to. | MaxLen: 255
    ssl_hpkp_report_uri: str
    # Indicate that HPKP header applies to all subdomains. | Default: disable
    ssl_hpkp_include_subdomains: Literal["disable", "enable"]
    # Enable/disable including HSTS header in response. | Default: disable
    ssl_hsts: Literal["disable", "enable"]
    # Number of seconds the client should honor the HSTS setting. | Default: 5184000 | Min: 60 | Max: 157680000
    ssl_hsts_age: int
    # Indicate that HSTS header applies to all subdomains. | Default: disable
    ssl_hsts_include_subdomains: Literal["disable", "enable"]
    # Name of the health check monitor to use when polling to dete
    monitor: list[VipMonitorObject]
    # Maximum number of incomplete connections. | Default: 1000 | Min: 0 | Max: 100000
    max_embryonic_connections: int
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
    # Range of mapped IPv6 addresses. Specify the start IPv6 addre
    ipv6_mappedip: str
    # IPv6 port number range on the destination network to which t
    ipv6_mappedport: str
    # Enable/disable one click GSLB server integration with FortiG | Default: disable
    one_click_gslb_server: Literal["disable", "enable"]
    # Hostname to use within the configured FortiGSLB domain. | MaxLen: 35
    gslb_hostname: str
    # Domain to use when integrating with FortiGSLB. | MaxLen: 255
    gslb_domain_name: str
    # Publicly accessible IP addresses for the FortiGSLB service.
    gslb_public_ips: list[VipGslbpublicipsObject]
    
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
    def to_dict(self) -> VipPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vip:
    """
    Configure virtual IP for IPv4.
    
    Path: firewall/vip
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
    ) -> VipObject: ...
    
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
    ) -> VipObject: ...
    
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
    ) -> list[VipObject]: ...
    
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
    ) -> VipObject: ...
    
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
    ) -> VipObject: ...
    
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
    ) -> list[VipObject]: ...
    
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
    ) -> VipObject: ...
    
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
    ) -> VipObject: ...
    
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
    ) -> list[VipObject]: ...
    
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
    ) -> VipObject | list[VipObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> VipObject: ...
    
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
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Vip",
    "VipPayload",
    "VipResponse",
    "VipObject",
]