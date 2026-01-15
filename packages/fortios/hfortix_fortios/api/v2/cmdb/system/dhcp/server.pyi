from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ServerPayload(TypedDict, total=False):
    """
    Type hints for system/dhcp/server payload fields.
    
    Configure DHCP servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.timezone.TimezoneEndpoint` (via: timezone)

    **Usage:**
        payload: ServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["disable", "enable"]  # Enable/disable this DHCP configuration. | Default: enable
    lease_time: int  # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    mac_acl_default_action: Literal["assign", "block"]  # MAC access control default action | Default: assign
    forticlient_on_net_status: Literal["disable", "enable"]  # Enable/disable FortiClient-On-Net service for this | Default: enable
    dns_service: Literal["local", "default", "specify"]  # Options for assigning DNS servers to DHCP clients. | Default: specify
    dns_server1: str  # DNS server 1. | Default: 0.0.0.0
    dns_server2: str  # DNS server 2. | Default: 0.0.0.0
    dns_server3: str  # DNS server 3. | Default: 0.0.0.0
    dns_server4: str  # DNS server 4. | Default: 0.0.0.0
    wifi_ac_service: Literal["specify", "local"]  # Options for assigning WiFi access controllers to D | Default: specify
    wifi_ac1: str  # WiFi Access Controller 1 IP address | Default: 0.0.0.0
    wifi_ac2: str  # WiFi Access Controller 2 IP address | Default: 0.0.0.0
    wifi_ac3: str  # WiFi Access Controller 3 IP address | Default: 0.0.0.0
    ntp_service: Literal["local", "default", "specify"]  # Options for assigning Network Time Protocol (NTP) | Default: specify
    ntp_server1: str  # NTP server 1. | Default: 0.0.0.0
    ntp_server2: str  # NTP server 2. | Default: 0.0.0.0
    ntp_server3: str  # NTP server 3. | Default: 0.0.0.0
    domain: str  # Domain name suffix for the IP addresses that the D | MaxLen: 35
    wins_server1: str  # WINS server 1. | Default: 0.0.0.0
    wins_server2: str  # WINS server 2. | Default: 0.0.0.0
    default_gateway: str  # Default gateway IP address assigned by the DHCP se | Default: 0.0.0.0
    next_server: str  # IP address of a server (for example, a TFTP sever) | Default: 0.0.0.0
    netmask: str  # Netmask assigned by the DHCP server. | Default: 0.0.0.0
    interface: str  # DHCP server can assign IP configurations to client | MaxLen: 15
    ip_range: list[dict[str, Any]]  # DHCP IP range configuration.
    timezone_option: Literal["disable", "default", "specify"]  # Options for the DHCP server to set the client's ti | Default: disable
    timezone: str  # Select the time zone to be assigned to DHCP client | MaxLen: 63
    tftp_server: list[dict[str, Any]]  # One or more hostnames or IP addresses of the TFTP
    filename: str  # Name of the boot file on the TFTP server. | MaxLen: 127
    options: list[dict[str, Any]]  # DHCP options.
    server_type: Literal["regular", "ipsec"]  # DHCP server can be a normal DHCP server or an IPse | Default: regular
    ip_mode: Literal["range", "usrgrp"]  # Method used to assign client IP. | Default: range
    conflicted_ip_timeout: int  # Time in seconds to wait after a conflicted IP addr | Default: 1800 | Min: 60 | Max: 8640000
    ipsec_lease_hold: int  # DHCP over IPsec leases expire this many seconds af | Default: 60 | Min: 0 | Max: 8640000
    auto_configuration: Literal["disable", "enable"]  # Enable/disable auto configuration. | Default: enable
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]  # Enable/disable populating of DHCP server settings | Default: disable
    auto_managed_status: Literal["disable", "enable"]  # Enable/disable use of this DHCP server once this i | Default: enable
    ddns_update: Literal["disable", "enable"]  # Enable/disable DDNS update for DHCP. | Default: disable
    ddns_update_override: Literal["disable", "enable"]  # Enable/disable DDNS update override for DHCP. | Default: disable
    ddns_server_ip: str  # DDNS server IP. | Default: 0.0.0.0
    ddns_zone: str  # Zone of your domain name (ex. DDNS.com). | MaxLen: 64
    ddns_auth: Literal["disable", "tsig"]  # DDNS authentication mode. | Default: disable
    ddns_keyname: str  # DDNS update key name. | MaxLen: 64
    ddns_key: str  # DDNS update key (base 64 encoding).
    ddns_ttl: int  # TTL. | Default: 300 | Min: 60 | Max: 86400
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class identifier (VCI) match | Default: disable
    vci_string: list[dict[str, Any]]  # One or more VCI strings in quotes separated by spa
    exclude_range: list[dict[str, Any]]  # Exclude one or more ranges of IP addresses from be
    shared_subnet: Literal["disable", "enable"]  # Enable/disable shared subnet. | Default: disable
    relay_agent: str  # Relay agent IP. | Default: 0.0.0.0
    reserved_address: list[dict[str, Any]]  # Options for the DHCP server to assign IP settings

# Nested TypedDicts for table field children (dict mode)

class ServerIprangeItem(TypedDict):
    """Type hints for ip-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_ip: str  # Start of IP range. | Default: 0.0.0.0
    end_ip: str  # End of IP range. | Default: 0.0.0.0
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class identifier (VCI) match | Default: disable
    vci_string: str  # One or more VCI strings in quotes separated by spa
    uci_match: Literal["disable", "enable"]  # Enable/disable user class identifier (UCI) matchin | Default: disable
    uci_string: str  # One or more UCI strings in quotes separated by spa
    lease_time: int  # Lease time in seconds, 0 means default lease time. | Default: 0 | Min: 300 | Max: 8640000


class ServerTftpserverItem(TypedDict):
    """Type hints for tftp-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    tftp_server: str  # TFTP server. | MaxLen: 63


class ServerOptionsItem(TypedDict):
    """Type hints for options table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    code: int  # DHCP option code. | Default: 0 | Min: 0 | Max: 255
    type: Literal["hex", "string", "ip", "fqdn"]  # DHCP option type. | Default: hex
    value: str  # DHCP option value. | MaxLen: 312
    ip: str  # DHCP option IPs.
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class identifier (VCI) match | Default: disable
    vci_string: str  # One or more VCI strings in quotes separated by spa
    uci_match: Literal["disable", "enable"]  # Enable/disable user class identifier (UCI) matchin | Default: disable
    uci_string: str  # One or more UCI strings in quotes separated by spa


class ServerVcistringItem(TypedDict):
    """Type hints for vci-string table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vci_string: str  # VCI strings. | MaxLen: 255


class ServerExcluderangeItem(TypedDict):
    """Type hints for exclude-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_ip: str  # Start of IP range. | Default: 0.0.0.0
    end_ip: str  # End of IP range. | Default: 0.0.0.0
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class identifier (VCI) match | Default: disable
    vci_string: str  # One or more VCI strings in quotes separated by spa
    uci_match: Literal["disable", "enable"]  # Enable/disable user class identifier (UCI) matchin | Default: disable
    uci_string: str  # One or more UCI strings in quotes separated by spa
    lease_time: int  # Lease time in seconds, 0 means default lease time. | Default: 0 | Min: 300 | Max: 8640000


class ServerReservedaddressItem(TypedDict):
    """Type hints for reserved-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    type: Literal["mac", "option82"]  # DHCP reserved-address type. | Default: mac
    ip: str  # IP address to be reserved for the MAC address. | Default: 0.0.0.0
    mac: str  # MAC address of the client that will get the reserv | Default: 00:00:00:00:00:00
    action: Literal["assign", "block", "reserved"]  # Options for the DHCP server to configure the clien | Default: reserved
    circuit_id_type: Literal["hex", "string"]  # DHCP option type. | Default: string
    circuit_id: str  # Option 82 circuit-ID of the client that will get t | MaxLen: 312
    remote_id_type: Literal["hex", "string"]  # DHCP option type. | Default: string
    remote_id: str  # Option 82 remote-ID of the client that will get th | MaxLen: 312
    description: str  # Description. | MaxLen: 255


# Nested classes for table field children (object mode)

@final
class ServerIprangeObject:
    """Typed object for ip-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of IP range. | Default: 0.0.0.0
    start_ip: str
    # End of IP range. | Default: 0.0.0.0
    end_ip: str
    # Enable/disable vendor class identifier (VCI) matching. When | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: str
    # Enable/disable user class identifier (UCI) matching. When en | Default: disable
    uci_match: Literal["disable", "enable"]
    # One or more UCI strings in quotes separated by spaces.
    uci_string: str
    # Lease time in seconds, 0 means default lease time. | Default: 0 | Min: 300 | Max: 8640000
    lease_time: int
    
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
class ServerTftpserverObject:
    """Typed object for tftp-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # TFTP server. | MaxLen: 63
    tftp_server: str
    
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
class ServerOptionsObject:
    """Typed object for options table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # DHCP option code. | Default: 0 | Min: 0 | Max: 255
    code: int
    # DHCP option type. | Default: hex
    type: Literal["hex", "string", "ip", "fqdn"]
    # DHCP option value. | MaxLen: 312
    value: str
    # DHCP option IPs.
    ip: str
    # Enable/disable vendor class identifier (VCI) matching. When | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: str
    # Enable/disable user class identifier (UCI) matching. When en | Default: disable
    uci_match: Literal["disable", "enable"]
    # One or more UCI strings in quotes separated by spaces.
    uci_string: str
    
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
class ServerVcistringObject:
    """Typed object for vci-string table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VCI strings. | MaxLen: 255
    vci_string: str
    
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
class ServerExcluderangeObject:
    """Typed object for exclude-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of IP range. | Default: 0.0.0.0
    start_ip: str
    # End of IP range. | Default: 0.0.0.0
    end_ip: str
    # Enable/disable vendor class identifier (VCI) matching. When | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: str
    # Enable/disable user class identifier (UCI) matching. When en | Default: disable
    uci_match: Literal["disable", "enable"]
    # One or more UCI strings in quotes separated by spaces.
    uci_string: str
    # Lease time in seconds, 0 means default lease time. | Default: 0 | Min: 300 | Max: 8640000
    lease_time: int
    
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
class ServerReservedaddressObject:
    """Typed object for reserved-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # DHCP reserved-address type. | Default: mac
    type: Literal["mac", "option82"]
    # IP address to be reserved for the MAC address. | Default: 0.0.0.0
    ip: str
    # MAC address of the client that will get the reserved IP addr | Default: 00:00:00:00:00:00
    mac: str
    # Options for the DHCP server to configure the client with the | Default: reserved
    action: Literal["assign", "block", "reserved"]
    # DHCP option type. | Default: string
    circuit_id_type: Literal["hex", "string"]
    # Option 82 circuit-ID of the client that will get the reserve | MaxLen: 312
    circuit_id: str
    # DHCP option type. | Default: string
    remote_id_type: Literal["hex", "string"]
    # Option 82 remote-ID of the client that will get the reserved | MaxLen: 312
    remote_id: str
    # Description. | MaxLen: 255
    description: str
    
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
class ServerResponse(TypedDict):
    """
    Type hints for system/dhcp/server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["disable", "enable"]  # Enable/disable this DHCP configuration. | Default: enable
    lease_time: int  # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    mac_acl_default_action: Literal["assign", "block"]  # MAC access control default action | Default: assign
    forticlient_on_net_status: Literal["disable", "enable"]  # Enable/disable FortiClient-On-Net service for this | Default: enable
    dns_service: Literal["local", "default", "specify"]  # Options for assigning DNS servers to DHCP clients. | Default: specify
    dns_server1: str  # DNS server 1. | Default: 0.0.0.0
    dns_server2: str  # DNS server 2. | Default: 0.0.0.0
    dns_server3: str  # DNS server 3. | Default: 0.0.0.0
    dns_server4: str  # DNS server 4. | Default: 0.0.0.0
    wifi_ac_service: Literal["specify", "local"]  # Options for assigning WiFi access controllers to D | Default: specify
    wifi_ac1: str  # WiFi Access Controller 1 IP address | Default: 0.0.0.0
    wifi_ac2: str  # WiFi Access Controller 2 IP address | Default: 0.0.0.0
    wifi_ac3: str  # WiFi Access Controller 3 IP address | Default: 0.0.0.0
    ntp_service: Literal["local", "default", "specify"]  # Options for assigning Network Time Protocol (NTP) | Default: specify
    ntp_server1: str  # NTP server 1. | Default: 0.0.0.0
    ntp_server2: str  # NTP server 2. | Default: 0.0.0.0
    ntp_server3: str  # NTP server 3. | Default: 0.0.0.0
    domain: str  # Domain name suffix for the IP addresses that the D | MaxLen: 35
    wins_server1: str  # WINS server 1. | Default: 0.0.0.0
    wins_server2: str  # WINS server 2. | Default: 0.0.0.0
    default_gateway: str  # Default gateway IP address assigned by the DHCP se | Default: 0.0.0.0
    next_server: str  # IP address of a server (for example, a TFTP sever) | Default: 0.0.0.0
    netmask: str  # Netmask assigned by the DHCP server. | Default: 0.0.0.0
    interface: str  # DHCP server can assign IP configurations to client | MaxLen: 15
    ip_range: list[ServerIprangeItem]  # DHCP IP range configuration.
    timezone_option: Literal["disable", "default", "specify"]  # Options for the DHCP server to set the client's ti | Default: disable
    timezone: str  # Select the time zone to be assigned to DHCP client | MaxLen: 63
    tftp_server: list[ServerTftpserverItem]  # One or more hostnames or IP addresses of the TFTP
    filename: str  # Name of the boot file on the TFTP server. | MaxLen: 127
    options: list[ServerOptionsItem]  # DHCP options.
    server_type: Literal["regular", "ipsec"]  # DHCP server can be a normal DHCP server or an IPse | Default: regular
    ip_mode: Literal["range", "usrgrp"]  # Method used to assign client IP. | Default: range
    conflicted_ip_timeout: int  # Time in seconds to wait after a conflicted IP addr | Default: 1800 | Min: 60 | Max: 8640000
    ipsec_lease_hold: int  # DHCP over IPsec leases expire this many seconds af | Default: 60 | Min: 0 | Max: 8640000
    auto_configuration: Literal["disable", "enable"]  # Enable/disable auto configuration. | Default: enable
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]  # Enable/disable populating of DHCP server settings | Default: disable
    auto_managed_status: Literal["disable", "enable"]  # Enable/disable use of this DHCP server once this i | Default: enable
    ddns_update: Literal["disable", "enable"]  # Enable/disable DDNS update for DHCP. | Default: disable
    ddns_update_override: Literal["disable", "enable"]  # Enable/disable DDNS update override for DHCP. | Default: disable
    ddns_server_ip: str  # DDNS server IP. | Default: 0.0.0.0
    ddns_zone: str  # Zone of your domain name (ex. DDNS.com). | MaxLen: 64
    ddns_auth: Literal["disable", "tsig"]  # DDNS authentication mode. | Default: disable
    ddns_keyname: str  # DDNS update key name. | MaxLen: 64
    ddns_key: str  # DDNS update key (base 64 encoding).
    ddns_ttl: int  # TTL. | Default: 300 | Min: 60 | Max: 86400
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class identifier (VCI) match | Default: disable
    vci_string: list[ServerVcistringItem]  # One or more VCI strings in quotes separated by spa
    exclude_range: list[ServerExcluderangeItem]  # Exclude one or more ranges of IP addresses from be
    shared_subnet: Literal["disable", "enable"]  # Enable/disable shared subnet. | Default: disable
    relay_agent: str  # Relay agent IP. | Default: 0.0.0.0
    reserved_address: list[ServerReservedaddressItem]  # Options for the DHCP server to assign IP settings


@final
class ServerObject:
    """Typed FortiObject for system/dhcp/server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable this DHCP configuration. | Default: enable
    status: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    lease_time: int
    # MAC access control default action | Default: assign
    mac_acl_default_action: Literal["assign", "block"]
    # Enable/disable FortiClient-On-Net service for this DHCP serv | Default: enable
    forticlient_on_net_status: Literal["disable", "enable"]
    # Options for assigning DNS servers to DHCP clients. | Default: specify
    dns_service: Literal["local", "default", "specify"]
    # DNS server 1. | Default: 0.0.0.0
    dns_server1: str
    # DNS server 2. | Default: 0.0.0.0
    dns_server2: str
    # DNS server 3. | Default: 0.0.0.0
    dns_server3: str
    # DNS server 4. | Default: 0.0.0.0
    dns_server4: str
    # Options for assigning WiFi access controllers to DHCP client | Default: specify
    wifi_ac_service: Literal["specify", "local"]
    # WiFi Access Controller 1 IP address | Default: 0.0.0.0
    wifi_ac1: str
    # WiFi Access Controller 2 IP address | Default: 0.0.0.0
    wifi_ac2: str
    # WiFi Access Controller 3 IP address | Default: 0.0.0.0
    wifi_ac3: str
    # Options for assigning Network Time Protocol (NTP) servers to | Default: specify
    ntp_service: Literal["local", "default", "specify"]
    # NTP server 1. | Default: 0.0.0.0
    ntp_server1: str
    # NTP server 2. | Default: 0.0.0.0
    ntp_server2: str
    # NTP server 3. | Default: 0.0.0.0
    ntp_server3: str
    # Domain name suffix for the IP addresses that the DHCP server | MaxLen: 35
    domain: str
    # WINS server 1. | Default: 0.0.0.0
    wins_server1: str
    # WINS server 2. | Default: 0.0.0.0
    wins_server2: str
    # Default gateway IP address assigned by the DHCP server. | Default: 0.0.0.0
    default_gateway: str
    # IP address of a server (for example, a TFTP sever) that DHCP | Default: 0.0.0.0
    next_server: str
    # Netmask assigned by the DHCP server. | Default: 0.0.0.0
    netmask: str
    # DHCP server can assign IP configurations to clients connecte | MaxLen: 15
    interface: str
    # DHCP IP range configuration.
    ip_range: list[ServerIprangeObject]
    # Options for the DHCP server to set the client's time zone. | Default: disable
    timezone_option: Literal["disable", "default", "specify"]
    # Select the time zone to be assigned to DHCP clients. | MaxLen: 63
    timezone: str
    # One or more hostnames or IP addresses of the TFTP servers in
    tftp_server: list[ServerTftpserverObject]
    # Name of the boot file on the TFTP server. | MaxLen: 127
    filename: str
    # DHCP options.
    options: list[ServerOptionsObject]
    # DHCP server can be a normal DHCP server or an IPsec DHCP ser | Default: regular
    server_type: Literal["regular", "ipsec"]
    # Method used to assign client IP. | Default: range
    ip_mode: Literal["range", "usrgrp"]
    # Time in seconds to wait after a conflicted IP address is rem | Default: 1800 | Min: 60 | Max: 8640000
    conflicted_ip_timeout: int
    # DHCP over IPsec leases expire this many seconds after tunnel | Default: 60 | Min: 0 | Max: 8640000
    ipsec_lease_hold: int
    # Enable/disable auto configuration. | Default: enable
    auto_configuration: Literal["disable", "enable"]
    # Enable/disable populating of DHCP server settings from Forti | Default: disable
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]
    # Enable/disable use of this DHCP server once this interface h | Default: enable
    auto_managed_status: Literal["disable", "enable"]
    # Enable/disable DDNS update for DHCP. | Default: disable
    ddns_update: Literal["disable", "enable"]
    # Enable/disable DDNS update override for DHCP. | Default: disable
    ddns_update_override: Literal["disable", "enable"]
    # DDNS server IP. | Default: 0.0.0.0
    ddns_server_ip: str
    # Zone of your domain name (ex. DDNS.com). | MaxLen: 64
    ddns_zone: str
    # DDNS authentication mode. | Default: disable
    ddns_auth: Literal["disable", "tsig"]
    # DDNS update key name. | MaxLen: 64
    ddns_keyname: str
    # DDNS update key (base 64 encoding).
    ddns_key: str
    # TTL. | Default: 300 | Min: 60 | Max: 86400
    ddns_ttl: int
    # Enable/disable vendor class identifier (VCI) matching. When | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: list[ServerVcistringObject]
    # Exclude one or more ranges of IP addresses from being assign
    exclude_range: list[ServerExcluderangeObject]
    # Enable/disable shared subnet. | Default: disable
    shared_subnet: Literal["disable", "enable"]
    # Relay agent IP. | Default: 0.0.0.0
    relay_agent: str
    # Options for the DHCP server to assign IP settings to specifi
    reserved_address: list[ServerReservedaddressObject]
    
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
    def to_dict(self) -> ServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Server:
    """
    Configure DHCP servers.
    
    Path: system/dhcp/server
    Category: cmdb
    Primary Key: id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ServerObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ServerObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> list[ServerObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        id: int,
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
    ) -> ServerObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> ServerObject: ...
    
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
    ) -> list[ServerObject]: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
    ) -> ServerObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> ServerObject: ...
    
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
    ) -> list[ServerObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> ServerObject | list[ServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerResponse",
    "ServerObject",
]