from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Phase2Payload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec/phase2 payload fields.
    
    Configure VPN autokey tunnel.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: dst-name, src-name)
        - :class:`~.firewall.address6.Address6Endpoint` (via: dst-name6, src-name6)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: dst-name, src-name)
        - :class:`~.firewall.addrgrp6.Addrgrp6Endpoint` (via: dst-name6, src-name6)
        - :class:`~.vpn.ipsec.phase1.Phase1Endpoint` (via: phase1name)

    **Usage:**
        payload: Phase2Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPsec tunnel name. | MaxLen: 35
    phase1name: str  # Phase 1 determines the options required for phase | MaxLen: 35
    dhcp_ipsec: Literal["enable", "disable"]  # Enable/disable DHCP-IPsec. | Default: disable
    use_natip: Literal["enable", "disable"]  # Enable to use the FortiGate public IP as the sourc | Default: enable
    selector_match: Literal["exact", "subset", "auto"]  # Match type to use when comparing selectors. | Default: auto
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase2 proposal.
    pfs: Literal["enable", "disable"]  # Enable/disable PFS feature. | Default: enable
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]  # Phase2 DH group. | Default: 20
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE1 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE2 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE3 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE4 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE5 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE6 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE7 group.
    replay: Literal["enable", "disable"]  # Enable/disable replay detection. | Default: enable
    keepalive: Literal["enable", "disable"]  # Enable/disable keep alive. | Default: disable
    auto_negotiate: Literal["enable", "disable"]  # Enable/disable IPsec SA auto-negotiation. | Default: disable
    add_route: Literal["phase1", "enable", "disable"]  # Enable/disable automatic route addition. | Default: phase1
    inbound_dscp_copy: Literal["phase1", "enable", "disable"]  # Enable/disable copying of the DSCP in the ESP head | Default: phase1
    keylifeseconds: int  # Phase2 key life in time in seconds (120 - 172800). | Default: 43200 | Min: 120 | Max: 172800
    keylifekbs: int  # Phase2 key life in number of kilobytes of traffic | Default: 5120 | Min: 5120 | Max: 4294967295
    keylife_type: Literal["seconds", "kbs", "both"]  # Keylife type. | Default: seconds
    single_source: Literal["enable", "disable"]  # Enable/disable single source IP restriction. | Default: disable
    route_overlap: Literal["use-old", "use-new", "allow"]  # Action for overlapping routes. | Default: use-new
    encapsulation: Literal["tunnel-mode", "transport-mode"]  # ESP encapsulation mode. | Default: tunnel-mode
    l2tp: Literal["enable", "disable"]  # Enable/disable L2TP over IPsec. | Default: disable
    comments: str  # Comment. | MaxLen: 255
    initiator_ts_narrow: Literal["enable", "disable"]  # Enable/disable traffic selector narrowing for IKEv | Default: disable
    diffserv: Literal["enable", "disable"]  # Enable/disable applying DSCP value to the IPsec tu | Default: disable
    diffservcode: str  # DSCP value to be applied to the IPsec tunnel outer
    protocol: int  # Quick mode protocol selector | Default: 0 | Min: 0 | Max: 255
    src_name: str  # Local proxy ID name. | MaxLen: 79
    src_name6: str  # Local proxy ID name. | MaxLen: 79
    src_addr_type: Literal["subnet", "range", "ip", "name"]  # Local proxy ID type. | Default: subnet
    src_start_ip: str  # Local proxy ID start. | Default: 0.0.0.0
    src_start_ip6: str  # Local proxy ID IPv6 start. | Default: ::
    src_end_ip: str  # Local proxy ID end. | Default: 0.0.0.0
    src_end_ip6: str  # Local proxy ID IPv6 end. | Default: ::
    src_subnet: str  # Local proxy ID subnet. | Default: 0.0.0.0 0.0.0.0
    src_subnet6: str  # Local proxy ID IPv6 subnet. | Default: ::/0
    src_port: int  # Quick mode source port (1 - 65535 or 0 for all). | Default: 0 | Min: 0 | Max: 65535
    dst_name: str  # Remote proxy ID name. | MaxLen: 79
    dst_name6: str  # Remote proxy ID name. | MaxLen: 79
    dst_addr_type: Literal["subnet", "range", "ip", "name"]  # Remote proxy ID type. | Default: subnet
    dst_start_ip: str  # Remote proxy ID IPv4 start. | Default: 0.0.0.0
    dst_start_ip6: str  # Remote proxy ID IPv6 start. | Default: ::
    dst_end_ip: str  # Remote proxy ID IPv4 end. | Default: 0.0.0.0
    dst_end_ip6: str  # Remote proxy ID IPv6 end. | Default: ::
    dst_subnet: str  # Remote proxy ID IPv4 subnet. | Default: 0.0.0.0 0.0.0.0
    dst_subnet6: str  # Remote proxy ID IPv6 subnet. | Default: ::/0
    dst_port: int  # Quick mode destination port | Default: 0 | Min: 0 | Max: 65535

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class Phase2Response(TypedDict):
    """
    Type hints for vpn/ipsec/phase2 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPsec tunnel name. | MaxLen: 35
    phase1name: str  # Phase 1 determines the options required for phase | MaxLen: 35
    dhcp_ipsec: Literal["enable", "disable"]  # Enable/disable DHCP-IPsec. | Default: disable
    use_natip: Literal["enable", "disable"]  # Enable to use the FortiGate public IP as the sourc | Default: enable
    selector_match: Literal["exact", "subset", "auto"]  # Match type to use when comparing selectors. | Default: auto
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase2 proposal.
    pfs: Literal["enable", "disable"]  # Enable/disable PFS feature. | Default: enable
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]  # Phase2 DH group. | Default: 20
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE1 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE2 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE3 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE4 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE5 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE6 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # phase2 ADDKE7 group.
    replay: Literal["enable", "disable"]  # Enable/disable replay detection. | Default: enable
    keepalive: Literal["enable", "disable"]  # Enable/disable keep alive. | Default: disable
    auto_negotiate: Literal["enable", "disable"]  # Enable/disable IPsec SA auto-negotiation. | Default: disable
    add_route: Literal["phase1", "enable", "disable"]  # Enable/disable automatic route addition. | Default: phase1
    inbound_dscp_copy: Literal["phase1", "enable", "disable"]  # Enable/disable copying of the DSCP in the ESP head | Default: phase1
    keylifeseconds: int  # Phase2 key life in time in seconds (120 - 172800). | Default: 43200 | Min: 120 | Max: 172800
    keylifekbs: int  # Phase2 key life in number of kilobytes of traffic | Default: 5120 | Min: 5120 | Max: 4294967295
    keylife_type: Literal["seconds", "kbs", "both"]  # Keylife type. | Default: seconds
    single_source: Literal["enable", "disable"]  # Enable/disable single source IP restriction. | Default: disable
    route_overlap: Literal["use-old", "use-new", "allow"]  # Action for overlapping routes. | Default: use-new
    encapsulation: Literal["tunnel-mode", "transport-mode"]  # ESP encapsulation mode. | Default: tunnel-mode
    l2tp: Literal["enable", "disable"]  # Enable/disable L2TP over IPsec. | Default: disable
    comments: str  # Comment. | MaxLen: 255
    initiator_ts_narrow: Literal["enable", "disable"]  # Enable/disable traffic selector narrowing for IKEv | Default: disable
    diffserv: Literal["enable", "disable"]  # Enable/disable applying DSCP value to the IPsec tu | Default: disable
    diffservcode: str  # DSCP value to be applied to the IPsec tunnel outer
    protocol: int  # Quick mode protocol selector | Default: 0 | Min: 0 | Max: 255
    src_name: str  # Local proxy ID name. | MaxLen: 79
    src_name6: str  # Local proxy ID name. | MaxLen: 79
    src_addr_type: Literal["subnet", "range", "ip", "name"]  # Local proxy ID type. | Default: subnet
    src_start_ip: str  # Local proxy ID start. | Default: 0.0.0.0
    src_start_ip6: str  # Local proxy ID IPv6 start. | Default: ::
    src_end_ip: str  # Local proxy ID end. | Default: 0.0.0.0
    src_end_ip6: str  # Local proxy ID IPv6 end. | Default: ::
    src_subnet: str  # Local proxy ID subnet. | Default: 0.0.0.0 0.0.0.0
    src_subnet6: str  # Local proxy ID IPv6 subnet. | Default: ::/0
    src_port: int  # Quick mode source port (1 - 65535 or 0 for all). | Default: 0 | Min: 0 | Max: 65535
    dst_name: str  # Remote proxy ID name. | MaxLen: 79
    dst_name6: str  # Remote proxy ID name. | MaxLen: 79
    dst_addr_type: Literal["subnet", "range", "ip", "name"]  # Remote proxy ID type. | Default: subnet
    dst_start_ip: str  # Remote proxy ID IPv4 start. | Default: 0.0.0.0
    dst_start_ip6: str  # Remote proxy ID IPv6 start. | Default: ::
    dst_end_ip: str  # Remote proxy ID IPv4 end. | Default: 0.0.0.0
    dst_end_ip6: str  # Remote proxy ID IPv6 end. | Default: ::
    dst_subnet: str  # Remote proxy ID IPv4 subnet. | Default: 0.0.0.0 0.0.0.0
    dst_subnet6: str  # Remote proxy ID IPv6 subnet. | Default: ::/0
    dst_port: int  # Quick mode destination port | Default: 0 | Min: 0 | Max: 65535


@final
class Phase2Object:
    """Typed FortiObject for vpn/ipsec/phase2 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPsec tunnel name. | MaxLen: 35
    name: str
    # Phase 1 determines the options required for phase 2. | MaxLen: 35
    phase1name: str
    # Enable/disable DHCP-IPsec. | Default: disable
    dhcp_ipsec: Literal["enable", "disable"]
    # Enable to use the FortiGate public IP as the source selector | Default: enable
    use_natip: Literal["enable", "disable"]
    # Match type to use when comparing selectors. | Default: auto
    selector_match: Literal["exact", "subset", "auto"]
    # Phase2 proposal.
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]
    # Enable/disable PFS feature. | Default: enable
    pfs: Literal["enable", "disable"]
    # Phase2 DH group. | Default: 20
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]
    # phase2 ADDKE1 group.
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE2 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE3 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE4 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE5 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE6 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE7 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # Enable/disable replay detection. | Default: enable
    replay: Literal["enable", "disable"]
    # Enable/disable keep alive. | Default: disable
    keepalive: Literal["enable", "disable"]
    # Enable/disable IPsec SA auto-negotiation. | Default: disable
    auto_negotiate: Literal["enable", "disable"]
    # Enable/disable automatic route addition. | Default: phase1
    add_route: Literal["phase1", "enable", "disable"]
    # Enable/disable copying of the DSCP in the ESP header to the | Default: phase1
    inbound_dscp_copy: Literal["phase1", "enable", "disable"]
    # Phase2 key life in time in seconds (120 - 172800). | Default: 43200 | Min: 120 | Max: 172800
    keylifeseconds: int
    # Phase2 key life in number of kilobytes of traffic | Default: 5120 | Min: 5120 | Max: 4294967295
    keylifekbs: int
    # Keylife type. | Default: seconds
    keylife_type: Literal["seconds", "kbs", "both"]
    # Enable/disable single source IP restriction. | Default: disable
    single_source: Literal["enable", "disable"]
    # Action for overlapping routes. | Default: use-new
    route_overlap: Literal["use-old", "use-new", "allow"]
    # ESP encapsulation mode. | Default: tunnel-mode
    encapsulation: Literal["tunnel-mode", "transport-mode"]
    # Enable/disable L2TP over IPsec. | Default: disable
    l2tp: Literal["enable", "disable"]
    # Comment. | MaxLen: 255
    comments: str
    # Enable/disable traffic selector narrowing for IKEv2 initiato | Default: disable
    initiator_ts_narrow: Literal["enable", "disable"]
    # Enable/disable applying DSCP value to the IPsec tunnel outer | Default: disable
    diffserv: Literal["enable", "disable"]
    # DSCP value to be applied to the IPsec tunnel outer IP header
    diffservcode: str
    # Quick mode protocol selector (1 - 255 or 0 for all). | Default: 0 | Min: 0 | Max: 255
    protocol: int
    # Local proxy ID name. | MaxLen: 79
    src_name: str
    # Local proxy ID name. | MaxLen: 79
    src_name6: str
    # Local proxy ID type. | Default: subnet
    src_addr_type: Literal["subnet", "range", "ip", "name"]
    # Local proxy ID start. | Default: 0.0.0.0
    src_start_ip: str
    # Local proxy ID IPv6 start. | Default: ::
    src_start_ip6: str
    # Local proxy ID end. | Default: 0.0.0.0
    src_end_ip: str
    # Local proxy ID IPv6 end. | Default: ::
    src_end_ip6: str
    # Local proxy ID subnet. | Default: 0.0.0.0 0.0.0.0
    src_subnet: str
    # Local proxy ID IPv6 subnet. | Default: ::/0
    src_subnet6: str
    # Quick mode source port (1 - 65535 or 0 for all). | Default: 0 | Min: 0 | Max: 65535
    src_port: int
    # Remote proxy ID name. | MaxLen: 79
    dst_name: str
    # Remote proxy ID name. | MaxLen: 79
    dst_name6: str
    # Remote proxy ID type. | Default: subnet
    dst_addr_type: Literal["subnet", "range", "ip", "name"]
    # Remote proxy ID IPv4 start. | Default: 0.0.0.0
    dst_start_ip: str
    # Remote proxy ID IPv6 start. | Default: ::
    dst_start_ip6: str
    # Remote proxy ID IPv4 end. | Default: 0.0.0.0
    dst_end_ip: str
    # Remote proxy ID IPv6 end. | Default: ::
    dst_end_ip6: str
    # Remote proxy ID IPv4 subnet. | Default: 0.0.0.0 0.0.0.0
    dst_subnet: str
    # Remote proxy ID IPv6 subnet. | Default: ::/0
    dst_subnet6: str
    # Quick mode destination port (1 - 65535 or 0 for all). | Default: 0 | Min: 0 | Max: 65535
    dst_port: int
    
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
    def to_dict(self) -> Phase2Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Phase2:
    """
    Configure VPN autokey tunnel.
    
    Path: vpn/ipsec/phase2
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
    ) -> Phase2Object: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> FortiObjectList[Phase2Object]: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> FortiObjectList[Phase2Object]: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> FortiObjectList[Phase2Object]: ...
    
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
    ) -> Phase2Object | list[Phase2Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase2Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase2Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase2Object: ...
    
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
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
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
    "Phase2",
    "Phase2Payload",
    "Phase2Response",
    "Phase2Object",
]