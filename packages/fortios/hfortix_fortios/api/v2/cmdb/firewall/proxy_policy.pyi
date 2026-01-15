from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProxyPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_policy payload fields.
    
    Configure proxy policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.profile-group.ProfileGroupEndpoint` (via: profile-group)
        - :class:`~.firewall.profile-protocol-options.ProfileProtocolOptionsEndpoint` (via: profile-protocol-options)
        - ... and 17 more dependencies

    **Usage:**
        payload: ProxyPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    policyid: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Policy name. | MaxLen: 35
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]  # Type of explicit proxy.
    access_proxy: list[dict[str, Any]]  # IPv4 access proxy.
    access_proxy6: list[dict[str, Any]]  # IPv6 access proxy.
    ztna_proxy: list[dict[str, Any]]  # ZTNA proxies.
    srcintf: list[dict[str, Any]]  # Source interface names.
    dstintf: list[dict[str, Any]]  # Destination interface names.
    srcaddr: list[dict[str, Any]]  # Source address objects.
    poolname: list[dict[str, Any]]  # Name of IP pool object.
    poolname6: list[dict[str, Any]]  # Name of IPv6 pool object.
    dstaddr: list[dict[str, Any]]  # Destination address objects.
    ztna_ems_tag: list[dict[str, Any]]  # ZTNA EMS Tag names.
    ztna_tags_match_logic: Literal["or", "and"]  # ZTNA tag matching logic. | Default: or
    device_ownership: Literal["enable", "disable"]  # When enabled, the ownership enforcement will be do | Default: disable
    url_risk: list[dict[str, Any]]  # URL risk level name.
    internet_service: Literal["enable", "disable"]  # Enable/disable use of Internet Services for this p | Default: disable
    internet_service_negate: Literal["enable", "disable"]  # When enabled, Internet Services match against any | Default: disable
    internet_service_name: list[dict[str, Any]]  # Internet Service name.
    internet_service_group: list[dict[str, Any]]  # Internet Service group name.
    internet_service_custom: list[dict[str, Any]]  # Custom Internet Service name.
    internet_service_custom_group: list[dict[str, Any]]  # Custom Internet Service group name.
    internet_service_fortiguard: list[dict[str, Any]]  # FortiGuard Internet Service name.
    internet_service6: Literal["enable", "disable"]  # Enable/disable use of Internet Services IPv6 for t | Default: disable
    internet_service6_negate: Literal["enable", "disable"]  # When enabled, Internet Services match against any | Default: disable
    internet_service6_name: list[dict[str, Any]]  # Internet Service IPv6 name.
    internet_service6_group: list[dict[str, Any]]  # Internet Service IPv6 group name.
    internet_service6_custom: list[dict[str, Any]]  # Custom Internet Service IPv6 name.
    internet_service6_custom_group: list[dict[str, Any]]  # Custom Internet Service IPv6 group name.
    internet_service6_fortiguard: list[dict[str, Any]]  # FortiGuard Internet Service IPv6 name.
    service: list[dict[str, Any]]  # Name of service objects.
    srcaddr_negate: Literal["enable", "disable"]  # When enabled, source addresses match against any a | Default: disable
    dstaddr_negate: Literal["enable", "disable"]  # When enabled, destination addresses match against | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]  # When enabled, ZTNA EMS tags match against any tag | Default: disable
    service_negate: Literal["enable", "disable"]  # When enabled, services match against any service E | Default: disable
    action: Literal["accept", "deny", "redirect", "isolate"]  # Accept or deny traffic matching the policy paramet | Default: deny
    status: Literal["enable", "disable"]  # Enable/disable the active status of the policy. | Default: enable
    schedule: str  # Name of schedule object. | MaxLen: 35
    logtraffic: Literal["all", "utm", "disable"]  # Enable/disable logging traffic through the policy. | Default: utm
    session_ttl: int  # TTL in seconds for sessions accepted by this polic | Default: 0 | Min: 300 | Max: 2764800
    srcaddr6: list[dict[str, Any]]  # IPv6 source address objects.
    dstaddr6: list[dict[str, Any]]  # IPv6 destination address objects.
    groups: list[dict[str, Any]]  # Names of group objects.
    users: list[dict[str, Any]]  # Names of user objects.
    http_tunnel_auth: Literal["enable", "disable"]  # Enable/disable HTTP tunnel authentication. | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]  # Redirect SSH traffic to matching transparent proxy | Default: disable
    webproxy_forward_server: str  # Web proxy forward server name. | MaxLen: 63
    isolator_server: str  # Isolator server name. | MaxLen: 63
    webproxy_profile: str  # Name of web proxy profile. | MaxLen: 63
    transparent: Literal["enable", "disable"]  # Enable to use the IP address of the client to conn | Default: disable
    webcache: Literal["enable", "disable"]  # Enable/disable web caching. | Default: disable
    webcache_https: Literal["disable", "enable"]  # Enable/disable web caching for HTTPS | Default: disable
    disclaimer: Literal["disable", "domain", "policy", "user"]  # Web proxy disclaimer setting: by domain, policy, o | Default: disable
    utm_status: Literal["enable", "disable"]  # Enable the use of UTM profiles/sensors/lists. | Default: disable
    profile_type: Literal["single", "group"]  # Determine whether the firewall policy allows secur | Default: single
    profile_group: str  # Name of profile group. | MaxLen: 47
    profile_protocol_options: str  # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    ssl_ssh_profile: str  # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    av_profile: str  # Name of an existing Antivirus profile. | MaxLen: 47
    webfilter_profile: str  # Name of an existing Web filter profile. | MaxLen: 47
    dnsfilter_profile: str  # Name of an existing DNS filter profile. | MaxLen: 47
    emailfilter_profile: str  # Name of an existing email filter profile. | MaxLen: 47
    dlp_profile: str  # Name of an existing DLP profile. | MaxLen: 47
    file_filter_profile: str  # Name of an existing file-filter profile. | MaxLen: 47
    ips_sensor: str  # Name of an existing IPS sensor. | MaxLen: 47
    application_list: str  # Name of an existing Application list. | MaxLen: 47
    ips_voip_filter: str  # Name of an existing VoIP (ips) profile. | MaxLen: 47
    sctp_filter_profile: str  # Name of an existing SCTP filter profile. | MaxLen: 47
    icap_profile: str  # Name of an existing ICAP profile. | MaxLen: 47
    videofilter_profile: str  # Name of an existing VideoFilter profile. | MaxLen: 47
    waf_profile: str  # Name of an existing Web application firewall profi | MaxLen: 47
    ssh_filter_profile: str  # Name of an existing SSH filter profile. | MaxLen: 47
    casb_profile: str  # Name of an existing CASB profile. | MaxLen: 47
    replacemsg_override_group: str  # Authentication replacement message override group. | MaxLen: 35
    logtraffic_start: Literal["enable", "disable"]  # Enable/disable policy log traffic start. | Default: disable
    log_http_transaction: Literal["enable", "disable"]  # Enable/disable HTTP transaction log. | Default: disable
    comments: str  # Optional comments. | MaxLen: 1023
    block_notification: Literal["enable", "disable"]  # Enable/disable block notification. | Default: disable
    redirect_url: str  # Redirect URL for further explicit web proxy proces | MaxLen: 1023
    https_sub_category: Literal["enable", "disable"]  # Enable/disable HTTPS sub-category policy matching. | Default: disable
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    detect_https_in_http_request: Literal["enable", "disable"]  # Enable/disable detection of HTTPS in HTTP request. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class ProxyPolicyAccessproxyItem(TypedDict):
    """Type hints for access-proxy table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Access Proxy name. | MaxLen: 79


class ProxyPolicyAccessproxy6Item(TypedDict):
    """Type hints for access-proxy6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Access proxy name. | MaxLen: 79


class ProxyPolicyZtnaproxyItem(TypedDict):
    """Type hints for ztna-proxy table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # ZTNA proxy name. | MaxLen: 79


class ProxyPolicySrcintfItem(TypedDict):
    """Type hints for srcintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class ProxyPolicyDstintfItem(TypedDict):
    """Type hints for dstintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class ProxyPolicySrcaddrItem(TypedDict):
    """Type hints for srcaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class ProxyPolicyPoolnameItem(TypedDict):
    """Type hints for poolname table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IP pool name. | MaxLen: 79


class ProxyPolicyPoolname6Item(TypedDict):
    """Type hints for poolname6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IPv6 pool name. | MaxLen: 79


class ProxyPolicyDstaddrItem(TypedDict):
    """Type hints for dstaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class ProxyPolicyZtnaemstagItem(TypedDict):
    """Type hints for ztna-ems-tag table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # EMS Tag name. | MaxLen: 79


class ProxyPolicyUrlriskItem(TypedDict):
    """Type hints for url-risk table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Risk level name. | MaxLen: 79


class ProxyPolicyInternetservicenameItem(TypedDict):
    """Type hints for internet-service-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service name. | MaxLen: 79


class ProxyPolicyInternetservicegroupItem(TypedDict):
    """Type hints for internet-service-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service group name. | MaxLen: 79


class ProxyPolicyInternetservicecustomItem(TypedDict):
    """Type hints for internet-service-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service name. | MaxLen: 79


class ProxyPolicyInternetservicecustomgroupItem(TypedDict):
    """Type hints for internet-service-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service group name. | MaxLen: 79


class ProxyPolicyInternetservicefortiguardItem(TypedDict):
    """Type hints for internet-service-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service name. | MaxLen: 79


class ProxyPolicyInternetservice6nameItem(TypedDict):
    """Type hints for internet-service6-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service IPv6 name. | MaxLen: 79


class ProxyPolicyInternetservice6groupItem(TypedDict):
    """Type hints for internet-service6-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Internet Service IPv6 group name. | MaxLen: 79


class ProxyPolicyInternetservice6customItem(TypedDict):
    """Type hints for internet-service6-custom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service IPv6 name. | MaxLen: 79


class ProxyPolicyInternetservice6customgroupItem(TypedDict):
    """Type hints for internet-service6-custom-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Custom Internet Service IPv6 group name. | MaxLen: 79


class ProxyPolicyInternetservice6fortiguardItem(TypedDict):
    """Type hints for internet-service6-fortiguard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiGuard Internet Service IPv6 name. | MaxLen: 79


class ProxyPolicyServiceItem(TypedDict):
    """Type hints for service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Service name. | MaxLen: 79


class ProxyPolicySrcaddr6Item(TypedDict):
    """Type hints for srcaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class ProxyPolicyDstaddr6Item(TypedDict):
    """Type hints for dstaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class ProxyPolicyGroupsItem(TypedDict):
    """Type hints for groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Group name. | MaxLen: 79


class ProxyPolicyUsersItem(TypedDict):
    """Type hints for users table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Group name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class ProxyPolicyAccessproxyObject:
    """Typed object for access-proxy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Access Proxy name. | MaxLen: 79
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
class ProxyPolicyAccessproxy6Object:
    """Typed object for access-proxy6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Access proxy name. | MaxLen: 79
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
class ProxyPolicyZtnaproxyObject:
    """Typed object for ztna-proxy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ZTNA proxy name. | MaxLen: 79
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
class ProxyPolicySrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
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
class ProxyPolicyDstintfObject:
    """Typed object for dstintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
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
class ProxyPolicySrcaddrObject:
    """Typed object for srcaddr table items.
    
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
class ProxyPolicyPoolnameObject:
    """Typed object for poolname table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP pool name. | MaxLen: 79
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
class ProxyPolicyPoolname6Object:
    """Typed object for poolname6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 pool name. | MaxLen: 79
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
class ProxyPolicyDstaddrObject:
    """Typed object for dstaddr table items.
    
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
class ProxyPolicyZtnaemstagObject:
    """Typed object for ztna-ems-tag table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # EMS Tag name. | MaxLen: 79
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
class ProxyPolicyUrlriskObject:
    """Typed object for url-risk table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Risk level name. | MaxLen: 79
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
class ProxyPolicyInternetservicenameObject:
    """Typed object for internet-service-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 79
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
class ProxyPolicyInternetservicegroupObject:
    """Typed object for internet-service-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name. | MaxLen: 79
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
class ProxyPolicyInternetservicecustomObject:
    """Typed object for internet-service-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name. | MaxLen: 79
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
class ProxyPolicyInternetservicecustomgroupObject:
    """Typed object for internet-service-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name. | MaxLen: 79
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
class ProxyPolicyInternetservicefortiguardObject:
    """Typed object for internet-service-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name. | MaxLen: 79
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
class ProxyPolicyInternetservice6nameObject:
    """Typed object for internet-service6-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service IPv6 name. | MaxLen: 79
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
class ProxyPolicyInternetservice6groupObject:
    """Typed object for internet-service6-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service IPv6 group name. | MaxLen: 79
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
class ProxyPolicyInternetservice6customObject:
    """Typed object for internet-service6-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service IPv6 name. | MaxLen: 79
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
class ProxyPolicyInternetservice6customgroupObject:
    """Typed object for internet-service6-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service IPv6 group name. | MaxLen: 79
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
class ProxyPolicyInternetservice6fortiguardObject:
    """Typed object for internet-service6-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service IPv6 name. | MaxLen: 79
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
class ProxyPolicyServiceObject:
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
class ProxyPolicySrcaddr6Object:
    """Typed object for srcaddr6 table items.
    
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
class ProxyPolicyDstaddr6Object:
    """Typed object for dstaddr6 table items.
    
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
class ProxyPolicyGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name. | MaxLen: 79
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
class ProxyPolicyUsersObject:
    """Typed object for users table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name. | MaxLen: 79
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



# Response TypedDict for GET returns (all fields present in API response)
class ProxyPolicyResponse(TypedDict):
    """
    Type hints for firewall/proxy_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    policyid: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Policy name. | MaxLen: 35
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]  # Type of explicit proxy.
    access_proxy: list[ProxyPolicyAccessproxyItem]  # IPv4 access proxy.
    access_proxy6: list[ProxyPolicyAccessproxy6Item]  # IPv6 access proxy.
    ztna_proxy: list[ProxyPolicyZtnaproxyItem]  # ZTNA proxies.
    srcintf: list[ProxyPolicySrcintfItem]  # Source interface names.
    dstintf: list[ProxyPolicyDstintfItem]  # Destination interface names.
    srcaddr: list[ProxyPolicySrcaddrItem]  # Source address objects.
    poolname: list[ProxyPolicyPoolnameItem]  # Name of IP pool object.
    poolname6: list[ProxyPolicyPoolname6Item]  # Name of IPv6 pool object.
    dstaddr: list[ProxyPolicyDstaddrItem]  # Destination address objects.
    ztna_ems_tag: list[ProxyPolicyZtnaemstagItem]  # ZTNA EMS Tag names.
    ztna_tags_match_logic: Literal["or", "and"]  # ZTNA tag matching logic. | Default: or
    device_ownership: Literal["enable", "disable"]  # When enabled, the ownership enforcement will be do | Default: disable
    url_risk: list[ProxyPolicyUrlriskItem]  # URL risk level name.
    internet_service: Literal["enable", "disable"]  # Enable/disable use of Internet Services for this p | Default: disable
    internet_service_negate: Literal["enable", "disable"]  # When enabled, Internet Services match against any | Default: disable
    internet_service_name: list[ProxyPolicyInternetservicenameItem]  # Internet Service name.
    internet_service_group: list[ProxyPolicyInternetservicegroupItem]  # Internet Service group name.
    internet_service_custom: list[ProxyPolicyInternetservicecustomItem]  # Custom Internet Service name.
    internet_service_custom_group: list[ProxyPolicyInternetservicecustomgroupItem]  # Custom Internet Service group name.
    internet_service_fortiguard: list[ProxyPolicyInternetservicefortiguardItem]  # FortiGuard Internet Service name.
    internet_service6: Literal["enable", "disable"]  # Enable/disable use of Internet Services IPv6 for t | Default: disable
    internet_service6_negate: Literal["enable", "disable"]  # When enabled, Internet Services match against any | Default: disable
    internet_service6_name: list[ProxyPolicyInternetservice6nameItem]  # Internet Service IPv6 name.
    internet_service6_group: list[ProxyPolicyInternetservice6groupItem]  # Internet Service IPv6 group name.
    internet_service6_custom: list[ProxyPolicyInternetservice6customItem]  # Custom Internet Service IPv6 name.
    internet_service6_custom_group: list[ProxyPolicyInternetservice6customgroupItem]  # Custom Internet Service IPv6 group name.
    internet_service6_fortiguard: list[ProxyPolicyInternetservice6fortiguardItem]  # FortiGuard Internet Service IPv6 name.
    service: list[ProxyPolicyServiceItem]  # Name of service objects.
    srcaddr_negate: Literal["enable", "disable"]  # When enabled, source addresses match against any a | Default: disable
    dstaddr_negate: Literal["enable", "disable"]  # When enabled, destination addresses match against | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]  # When enabled, ZTNA EMS tags match against any tag | Default: disable
    service_negate: Literal["enable", "disable"]  # When enabled, services match against any service E | Default: disable
    action: Literal["accept", "deny", "redirect", "isolate"]  # Accept or deny traffic matching the policy paramet | Default: deny
    status: Literal["enable", "disable"]  # Enable/disable the active status of the policy. | Default: enable
    schedule: str  # Name of schedule object. | MaxLen: 35
    logtraffic: Literal["all", "utm", "disable"]  # Enable/disable logging traffic through the policy. | Default: utm
    session_ttl: int  # TTL in seconds for sessions accepted by this polic | Default: 0 | Min: 300 | Max: 2764800
    srcaddr6: list[ProxyPolicySrcaddr6Item]  # IPv6 source address objects.
    dstaddr6: list[ProxyPolicyDstaddr6Item]  # IPv6 destination address objects.
    groups: list[ProxyPolicyGroupsItem]  # Names of group objects.
    users: list[ProxyPolicyUsersItem]  # Names of user objects.
    http_tunnel_auth: Literal["enable", "disable"]  # Enable/disable HTTP tunnel authentication. | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]  # Redirect SSH traffic to matching transparent proxy | Default: disable
    webproxy_forward_server: str  # Web proxy forward server name. | MaxLen: 63
    isolator_server: str  # Isolator server name. | MaxLen: 63
    webproxy_profile: str  # Name of web proxy profile. | MaxLen: 63
    transparent: Literal["enable", "disable"]  # Enable to use the IP address of the client to conn | Default: disable
    webcache: Literal["enable", "disable"]  # Enable/disable web caching. | Default: disable
    webcache_https: Literal["disable", "enable"]  # Enable/disable web caching for HTTPS | Default: disable
    disclaimer: Literal["disable", "domain", "policy", "user"]  # Web proxy disclaimer setting: by domain, policy, o | Default: disable
    utm_status: Literal["enable", "disable"]  # Enable the use of UTM profiles/sensors/lists. | Default: disable
    profile_type: Literal["single", "group"]  # Determine whether the firewall policy allows secur | Default: single
    profile_group: str  # Name of profile group. | MaxLen: 47
    profile_protocol_options: str  # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    ssl_ssh_profile: str  # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    av_profile: str  # Name of an existing Antivirus profile. | MaxLen: 47
    webfilter_profile: str  # Name of an existing Web filter profile. | MaxLen: 47
    dnsfilter_profile: str  # Name of an existing DNS filter profile. | MaxLen: 47
    emailfilter_profile: str  # Name of an existing email filter profile. | MaxLen: 47
    dlp_profile: str  # Name of an existing DLP profile. | MaxLen: 47
    file_filter_profile: str  # Name of an existing file-filter profile. | MaxLen: 47
    ips_sensor: str  # Name of an existing IPS sensor. | MaxLen: 47
    application_list: str  # Name of an existing Application list. | MaxLen: 47
    ips_voip_filter: str  # Name of an existing VoIP (ips) profile. | MaxLen: 47
    sctp_filter_profile: str  # Name of an existing SCTP filter profile. | MaxLen: 47
    icap_profile: str  # Name of an existing ICAP profile. | MaxLen: 47
    videofilter_profile: str  # Name of an existing VideoFilter profile. | MaxLen: 47
    waf_profile: str  # Name of an existing Web application firewall profi | MaxLen: 47
    ssh_filter_profile: str  # Name of an existing SSH filter profile. | MaxLen: 47
    casb_profile: str  # Name of an existing CASB profile. | MaxLen: 47
    replacemsg_override_group: str  # Authentication replacement message override group. | MaxLen: 35
    logtraffic_start: Literal["enable", "disable"]  # Enable/disable policy log traffic start. | Default: disable
    log_http_transaction: Literal["enable", "disable"]  # Enable/disable HTTP transaction log. | Default: disable
    comments: str  # Optional comments. | MaxLen: 1023
    block_notification: Literal["enable", "disable"]  # Enable/disable block notification. | Default: disable
    redirect_url: str  # Redirect URL for further explicit web proxy proces | MaxLen: 1023
    https_sub_category: Literal["enable", "disable"]  # Enable/disable HTTPS sub-category policy matching. | Default: disable
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    detect_https_in_http_request: Literal["enable", "disable"]  # Enable/disable detection of HTTPS in HTTP request. | Default: disable


@final
class ProxyPolicyObject:
    """Typed FortiObject for firewall/proxy_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    policyid: int
    # Policy name. | MaxLen: 35
    name: str
    # Type of explicit proxy.
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
    # IPv4 access proxy.
    access_proxy: list[ProxyPolicyAccessproxyObject]
    # IPv6 access proxy.
    access_proxy6: list[ProxyPolicyAccessproxy6Object]
    # ZTNA proxies.
    ztna_proxy: list[ProxyPolicyZtnaproxyObject]
    # Source interface names.
    srcintf: list[ProxyPolicySrcintfObject]
    # Destination interface names.
    dstintf: list[ProxyPolicyDstintfObject]
    # Source address objects.
    srcaddr: list[ProxyPolicySrcaddrObject]
    # Name of IP pool object.
    poolname: list[ProxyPolicyPoolnameObject]
    # Name of IPv6 pool object.
    poolname6: list[ProxyPolicyPoolname6Object]
    # Destination address objects.
    dstaddr: list[ProxyPolicyDstaddrObject]
    # ZTNA EMS Tag names.
    ztna_ems_tag: list[ProxyPolicyZtnaemstagObject]
    # ZTNA tag matching logic. | Default: or
    ztna_tags_match_logic: Literal["or", "and"]
    # When enabled, the ownership enforcement will be done at poli | Default: disable
    device_ownership: Literal["enable", "disable"]
    # URL risk level name.
    url_risk: list[ProxyPolicyUrlriskObject]
    # Enable/disable use of Internet Services for this policy. If | Default: disable
    internet_service: Literal["enable", "disable"]
    # When enabled, Internet Services match against any internet s | Default: disable
    internet_service_negate: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[ProxyPolicyInternetservicenameObject]
    # Internet Service group name.
    internet_service_group: list[ProxyPolicyInternetservicegroupObject]
    # Custom Internet Service name.
    internet_service_custom: list[ProxyPolicyInternetservicecustomObject]
    # Custom Internet Service group name.
    internet_service_custom_group: list[ProxyPolicyInternetservicecustomgroupObject]
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[ProxyPolicyInternetservicefortiguardObject]
    # Enable/disable use of Internet Services IPv6 for this policy | Default: disable
    internet_service6: Literal["enable", "disable"]
    # When enabled, Internet Services match against any internet s | Default: disable
    internet_service6_negate: Literal["enable", "disable"]
    # Internet Service IPv6 name.
    internet_service6_name: list[ProxyPolicyInternetservice6nameObject]
    # Internet Service IPv6 group name.
    internet_service6_group: list[ProxyPolicyInternetservice6groupObject]
    # Custom Internet Service IPv6 name.
    internet_service6_custom: list[ProxyPolicyInternetservice6customObject]
    # Custom Internet Service IPv6 group name.
    internet_service6_custom_group: list[ProxyPolicyInternetservice6customgroupObject]
    # FortiGuard Internet Service IPv6 name.
    internet_service6_fortiguard: list[ProxyPolicyInternetservice6fortiguardObject]
    # Name of service objects.
    service: list[ProxyPolicyServiceObject]
    # When enabled, source addresses match against any address EXC | Default: disable
    srcaddr_negate: Literal["enable", "disable"]
    # When enabled, destination addresses match against any addres | Default: disable
    dstaddr_negate: Literal["enable", "disable"]
    # When enabled, ZTNA EMS tags match against any tag EXCEPT the | Default: disable
    ztna_ems_tag_negate: Literal["enable", "disable"]
    # When enabled, services match against any service EXCEPT the | Default: disable
    service_negate: Literal["enable", "disable"]
    # Accept or deny traffic matching the policy parameters. | Default: deny
    action: Literal["accept", "deny", "redirect", "isolate"]
    # Enable/disable the active status of the policy. | Default: enable
    status: Literal["enable", "disable"]
    # Name of schedule object. | MaxLen: 35
    schedule: str
    # Enable/disable logging traffic through the policy. | Default: utm
    logtraffic: Literal["all", "utm", "disable"]
    # TTL in seconds for sessions accepted by this policy | Default: 0 | Min: 300 | Max: 2764800
    session_ttl: int
    # IPv6 source address objects.
    srcaddr6: list[ProxyPolicySrcaddr6Object]
    # IPv6 destination address objects.
    dstaddr6: list[ProxyPolicyDstaddr6Object]
    # Names of group objects.
    groups: list[ProxyPolicyGroupsObject]
    # Names of user objects.
    users: list[ProxyPolicyUsersObject]
    # Enable/disable HTTP tunnel authentication. | Default: disable
    http_tunnel_auth: Literal["enable", "disable"]
    # Redirect SSH traffic to matching transparent proxy policy. | Default: disable
    ssh_policy_redirect: Literal["enable", "disable"]
    # Web proxy forward server name. | MaxLen: 63
    webproxy_forward_server: str
    # Isolator server name. | MaxLen: 63
    isolator_server: str
    # Name of web proxy profile. | MaxLen: 63
    webproxy_profile: str
    # Enable to use the IP address of the client to connect to the | Default: disable
    transparent: Literal["enable", "disable"]
    # Enable/disable web caching. | Default: disable
    webcache: Literal["enable", "disable"]
    # Enable/disable web caching for HTTPS | Default: disable
    webcache_https: Literal["disable", "enable"]
    # Web proxy disclaimer setting: by domain, policy, or user. | Default: disable
    disclaimer: Literal["disable", "domain", "policy", "user"]
    # Enable the use of UTM profiles/sensors/lists. | Default: disable
    utm_status: Literal["enable", "disable"]
    # Determine whether the firewall policy allows security profil | Default: single
    profile_type: Literal["single", "group"]
    # Name of profile group. | MaxLen: 47
    profile_group: str
    # Name of an existing Protocol options profile. | Default: default | MaxLen: 47
    profile_protocol_options: str
    # Name of an existing SSL SSH profile. | Default: no-inspection | MaxLen: 47
    ssl_ssh_profile: str
    # Name of an existing Antivirus profile. | MaxLen: 47
    av_profile: str
    # Name of an existing Web filter profile. | MaxLen: 47
    webfilter_profile: str
    # Name of an existing DNS filter profile. | MaxLen: 47
    dnsfilter_profile: str
    # Name of an existing email filter profile. | MaxLen: 47
    emailfilter_profile: str
    # Name of an existing DLP profile. | MaxLen: 47
    dlp_profile: str
    # Name of an existing file-filter profile. | MaxLen: 47
    file_filter_profile: str
    # Name of an existing IPS sensor. | MaxLen: 47
    ips_sensor: str
    # Name of an existing Application list. | MaxLen: 47
    application_list: str
    # Name of an existing VoIP (ips) profile. | MaxLen: 47
    ips_voip_filter: str
    # Name of an existing SCTP filter profile. | MaxLen: 47
    sctp_filter_profile: str
    # Name of an existing ICAP profile. | MaxLen: 47
    icap_profile: str
    # Name of an existing VideoFilter profile. | MaxLen: 47
    videofilter_profile: str
    # Name of an existing Web application firewall profile. | MaxLen: 47
    waf_profile: str
    # Name of an existing SSH filter profile. | MaxLen: 47
    ssh_filter_profile: str
    # Name of an existing CASB profile. | MaxLen: 47
    casb_profile: str
    # Authentication replacement message override group. | MaxLen: 35
    replacemsg_override_group: str
    # Enable/disable policy log traffic start. | Default: disable
    logtraffic_start: Literal["enable", "disable"]
    # Enable/disable HTTP transaction log. | Default: disable
    log_http_transaction: Literal["enable", "disable"]
    # Optional comments. | MaxLen: 1023
    comments: str
    # Enable/disable block notification. | Default: disable
    block_notification: Literal["enable", "disable"]
    # Redirect URL for further explicit web proxy processing. | MaxLen: 1023
    redirect_url: str
    # Enable/disable HTTPS sub-category policy matching. | Default: disable
    https_sub_category: Literal["enable", "disable"]
    # Decrypted traffic mirror. | MaxLen: 35
    decrypted_traffic_mirror: str
    # Enable/disable detection of HTTPS in HTTP request. | Default: disable
    detect_https_in_http_request: Literal["enable", "disable"]
    
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
    def to_dict(self) -> ProxyPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProxyPolicy:
    """
    Configure proxy policies.
    
    Path: firewall/proxy_policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProxyPolicyObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProxyPolicyObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        policyid: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> list[ProxyPolicyObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> ProxyPolicyObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> ProxyPolicyObject: ...
    
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
    ) -> list[ProxyPolicyObject]: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
    ) -> ProxyPolicyObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> ProxyPolicyObject: ...
    
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
    ) -> list[ProxyPolicyObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> ProxyPolicyObject | list[ProxyPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ProxyPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ProxyPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ProxyPolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
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
    "ProxyPolicy",
    "ProxyPolicyPayload",
    "ProxyPolicyResponse",
    "ProxyPolicyObject",
]