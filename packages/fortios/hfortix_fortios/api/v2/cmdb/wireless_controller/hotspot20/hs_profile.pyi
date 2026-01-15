from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HsProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/hs_profile payload fields.
    
    Configure hotspot profile.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.wireless-controller.hotspot20.anqp-3gpp-cellular.Anqp3GppCellularEndpoint` (via: 3gpp-plmn)
        - :class:`~.wireless-controller.hotspot20.anqp-ip-address-type.AnqpIpAddressTypeEndpoint` (via: ip-addr-type)
        - :class:`~.wireless-controller.hotspot20.anqp-nai-realm.AnqpNaiRealmEndpoint` (via: nai-realm)
        - :class:`~.wireless-controller.hotspot20.anqp-network-auth-type.AnqpNetworkAuthTypeEndpoint` (via: network-auth)
        - :class:`~.wireless-controller.hotspot20.anqp-roaming-consortium.AnqpRoamingConsortiumEndpoint` (via: roaming-consortium)
        - :class:`~.wireless-controller.hotspot20.anqp-venue-name.AnqpVenueNameEndpoint` (via: venue-name)
        - :class:`~.wireless-controller.hotspot20.anqp-venue-url.AnqpVenueUrlEndpoint` (via: venue-url)
        - :class:`~.wireless-controller.hotspot20.h2qp-advice-of-charge.H2QpAdviceOfChargeEndpoint` (via: advice-of-charge)
        - :class:`~.wireless-controller.hotspot20.h2qp-conn-capability.H2QpConnCapabilityEndpoint` (via: conn-cap)
        - :class:`~.wireless-controller.hotspot20.h2qp-operator-name.H2QpOperatorNameEndpoint` (via: oper-friendly-name)
        - ... and 5 more dependencies

    **Usage:**
        payload: HsProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Hotspot profile name. | MaxLen: 35
    release: int  # Hotspot 2.0 Release number (1, 2, 3, default = 2). | Default: 2 | Min: 1 | Max: 3
    access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"]  # Access network type. | Default: private-network
    access_network_internet: Literal["enable", "disable"]  # Enable/disable connectivity to the Internet. | Default: disable
    access_network_asra: Literal["enable", "disable"]  # Enable/disable additional step required for access | Default: disable
    access_network_esr: Literal["enable", "disable"]  # Enable/disable emergency services reachable (ESR). | Default: disable
    access_network_uesa: Literal["enable", "disable"]  # Enable/disable unauthenticated emergency service a | Default: disable
    venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"]  # Venue group. | Default: unspecified
    venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"]  # Venue type. | Default: unspecified
    hessid: str  # Homogeneous extended service set identifier | Default: 00:00:00:00:00:00
    proxy_arp: Literal["enable", "disable"]  # Enable/disable Proxy ARP. | Default: enable
    l2tif: Literal["enable", "disable"]  # Enable/disable Layer 2 traffic inspection and filt | Default: disable
    pame_bi: Literal["disable", "enable"]  # Enable/disable Pre-Association Message Exchange BS | Default: enable
    anqp_domain_id: int  # ANQP Domain ID (0-65535). | Default: 0 | Min: 0 | Max: 65535
    domain_name: str  # Domain name. | MaxLen: 255
    osu_ssid: str  # Online sign up (OSU) SSID. | MaxLen: 255
    gas_comeback_delay: int  # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_fragmentation_limit: int  # GAS fragmentation limit | Default: 1024 | Min: 512 | Max: 4096
    dgaf: Literal["enable", "disable"]  # Enable/disable downstream group-addressed forwardi | Default: disable
    deauth_request_timeout: int  # Deauthentication request timeout (in seconds). | Default: 60 | Min: 30 | Max: 120
    wnm_sleep_mode: Literal["enable", "disable"]  # Enable/disable wireless network management (WNM) s | Default: disable
    bss_transition: Literal["enable", "disable"]  # Enable/disable basic service set (BSS) transition | Default: disable
    venue_name: str  # Venue name. | MaxLen: 35
    venue_url: str  # Venue name. | MaxLen: 35
    roaming_consortium: str  # Roaming consortium list name. | MaxLen: 35
    nai_realm: str  # NAI realm list name. | MaxLen: 35
    oper_friendly_name: str  # Operator friendly name. | MaxLen: 35
    oper_icon: str  # Operator icon. | MaxLen: 35
    advice_of_charge: str  # Advice of charge. | MaxLen: 35
    osu_provider_nai: str  # OSU Provider NAI. | MaxLen: 35
    terms_and_conditions: str  # Terms and conditions. | MaxLen: 35
    osu_provider: list[dict[str, Any]]  # Manually selected list of OSU provider(s).
    wan_metrics: str  # WAN metric name. | MaxLen: 35
    network_auth: str  # Network authentication name. | MaxLen: 35
    x3gpp_plmn: str  # 3GPP PLMN name. | MaxLen: 35
    conn_cap: str  # Connection capability name. | MaxLen: 35
    qos_map: str  # QoS MAP set ID. | MaxLen: 35
    ip_addr_type: str  # IP address type name. | MaxLen: 35
    wba_open_roaming: Literal["disable", "enable"]  # Enable/disable WBA open roaming support. | Default: disable
    wba_financial_clearing_provider: str  # WBA ID of financial clearing provider. | MaxLen: 127
    wba_data_clearing_provider: str  # WBA ID of data clearing provider. | MaxLen: 127
    wba_charging_currency: str  # Three letter currency code. | MaxLen: 3
    wba_charging_rate: int  # Number of currency units per kilobyte. | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

class HsProfileOsuproviderItem(TypedDict):
    """Type hints for osu-provider table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # OSU provider name. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class HsProfileOsuproviderObject:
    """Typed object for osu-provider table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # OSU provider name. | MaxLen: 35
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
class HsProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/hotspot20/hs_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Hotspot profile name. | MaxLen: 35
    release: int  # Hotspot 2.0 Release number (1, 2, 3, default = 2). | Default: 2 | Min: 1 | Max: 3
    access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"]  # Access network type. | Default: private-network
    access_network_internet: Literal["enable", "disable"]  # Enable/disable connectivity to the Internet. | Default: disable
    access_network_asra: Literal["enable", "disable"]  # Enable/disable additional step required for access | Default: disable
    access_network_esr: Literal["enable", "disable"]  # Enable/disable emergency services reachable (ESR). | Default: disable
    access_network_uesa: Literal["enable", "disable"]  # Enable/disable unauthenticated emergency service a | Default: disable
    venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"]  # Venue group. | Default: unspecified
    venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"]  # Venue type. | Default: unspecified
    hessid: str  # Homogeneous extended service set identifier | Default: 00:00:00:00:00:00
    proxy_arp: Literal["enable", "disable"]  # Enable/disable Proxy ARP. | Default: enable
    l2tif: Literal["enable", "disable"]  # Enable/disable Layer 2 traffic inspection and filt | Default: disable
    pame_bi: Literal["disable", "enable"]  # Enable/disable Pre-Association Message Exchange BS | Default: enable
    anqp_domain_id: int  # ANQP Domain ID (0-65535). | Default: 0 | Min: 0 | Max: 65535
    domain_name: str  # Domain name. | MaxLen: 255
    osu_ssid: str  # Online sign up (OSU) SSID. | MaxLen: 255
    gas_comeback_delay: int  # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_fragmentation_limit: int  # GAS fragmentation limit | Default: 1024 | Min: 512 | Max: 4096
    dgaf: Literal["enable", "disable"]  # Enable/disable downstream group-addressed forwardi | Default: disable
    deauth_request_timeout: int  # Deauthentication request timeout (in seconds). | Default: 60 | Min: 30 | Max: 120
    wnm_sleep_mode: Literal["enable", "disable"]  # Enable/disable wireless network management (WNM) s | Default: disable
    bss_transition: Literal["enable", "disable"]  # Enable/disable basic service set (BSS) transition | Default: disable
    venue_name: str  # Venue name. | MaxLen: 35
    venue_url: str  # Venue name. | MaxLen: 35
    roaming_consortium: str  # Roaming consortium list name. | MaxLen: 35
    nai_realm: str  # NAI realm list name. | MaxLen: 35
    oper_friendly_name: str  # Operator friendly name. | MaxLen: 35
    oper_icon: str  # Operator icon. | MaxLen: 35
    advice_of_charge: str  # Advice of charge. | MaxLen: 35
    osu_provider_nai: str  # OSU Provider NAI. | MaxLen: 35
    terms_and_conditions: str  # Terms and conditions. | MaxLen: 35
    osu_provider: list[HsProfileOsuproviderItem]  # Manually selected list of OSU provider(s).
    wan_metrics: str  # WAN metric name. | MaxLen: 35
    network_auth: str  # Network authentication name. | MaxLen: 35
    x3gpp_plmn: str  # 3GPP PLMN name. | MaxLen: 35
    conn_cap: str  # Connection capability name. | MaxLen: 35
    qos_map: str  # QoS MAP set ID. | MaxLen: 35
    ip_addr_type: str  # IP address type name. | MaxLen: 35
    wba_open_roaming: Literal["disable", "enable"]  # Enable/disable WBA open roaming support. | Default: disable
    wba_financial_clearing_provider: str  # WBA ID of financial clearing provider. | MaxLen: 127
    wba_data_clearing_provider: str  # WBA ID of data clearing provider. | MaxLen: 127
    wba_charging_currency: str  # Three letter currency code. | MaxLen: 3
    wba_charging_rate: int  # Number of currency units per kilobyte. | Default: 0 | Min: 0 | Max: 4294967295


@final
class HsProfileObject:
    """Typed FortiObject for wireless_controller/hotspot20/hs_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Hotspot profile name. | MaxLen: 35
    name: str
    # Hotspot 2.0 Release number (1, 2, 3, default = 2). | Default: 2 | Min: 1 | Max: 3
    release: int
    # Access network type. | Default: private-network
    access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"]
    # Enable/disable connectivity to the Internet. | Default: disable
    access_network_internet: Literal["enable", "disable"]
    # Enable/disable additional step required for access (ASRA). | Default: disable
    access_network_asra: Literal["enable", "disable"]
    # Enable/disable emergency services reachable (ESR). | Default: disable
    access_network_esr: Literal["enable", "disable"]
    # Enable/disable unauthenticated emergency service accessible | Default: disable
    access_network_uesa: Literal["enable", "disable"]
    # Venue group. | Default: unspecified
    venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"]
    # Venue type. | Default: unspecified
    venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"]
    # Homogeneous extended service set identifier (HESSID). | Default: 00:00:00:00:00:00
    hessid: str
    # Enable/disable Proxy ARP. | Default: enable
    proxy_arp: Literal["enable", "disable"]
    # Enable/disable Layer 2 traffic inspection and filtering. | Default: disable
    l2tif: Literal["enable", "disable"]
    # Enable/disable Pre-Association Message Exchange BSSID Indepe | Default: enable
    pame_bi: Literal["disable", "enable"]
    # ANQP Domain ID (0-65535). | Default: 0 | Min: 0 | Max: 65535
    anqp_domain_id: int
    # Domain name. | MaxLen: 255
    domain_name: str
    # Online sign up (OSU) SSID. | MaxLen: 255
    osu_ssid: str
    # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_comeback_delay: int
    # GAS fragmentation limit (512 - 4096, default = 1024). | Default: 1024 | Min: 512 | Max: 4096
    gas_fragmentation_limit: int
    # Enable/disable downstream group-addressed forwarding (DGAF). | Default: disable
    dgaf: Literal["enable", "disable"]
    # Deauthentication request timeout (in seconds). | Default: 60 | Min: 30 | Max: 120
    deauth_request_timeout: int
    # Enable/disable wireless network management (WNM) sleep mode. | Default: disable
    wnm_sleep_mode: Literal["enable", "disable"]
    # Enable/disable basic service set (BSS) transition Support. | Default: disable
    bss_transition: Literal["enable", "disable"]
    # Venue name. | MaxLen: 35
    venue_name: str
    # Venue name. | MaxLen: 35
    venue_url: str
    # Roaming consortium list name. | MaxLen: 35
    roaming_consortium: str
    # NAI realm list name. | MaxLen: 35
    nai_realm: str
    # Operator friendly name. | MaxLen: 35
    oper_friendly_name: str
    # Operator icon. | MaxLen: 35
    oper_icon: str
    # Advice of charge. | MaxLen: 35
    advice_of_charge: str
    # OSU Provider NAI. | MaxLen: 35
    osu_provider_nai: str
    # Terms and conditions. | MaxLen: 35
    terms_and_conditions: str
    # Manually selected list of OSU provider(s).
    osu_provider: list[HsProfileOsuproviderObject]
    # WAN metric name. | MaxLen: 35
    wan_metrics: str
    # Network authentication name. | MaxLen: 35
    network_auth: str
    # 3GPP PLMN name. | MaxLen: 35
    x3gpp_plmn: str
    # Connection capability name. | MaxLen: 35
    conn_cap: str
    # QoS MAP set ID. | MaxLen: 35
    qos_map: str
    # IP address type name. | MaxLen: 35
    ip_addr_type: str
    # Enable/disable WBA open roaming support. | Default: disable
    wba_open_roaming: Literal["disable", "enable"]
    # WBA ID of financial clearing provider. | MaxLen: 127
    wba_financial_clearing_provider: str
    # WBA ID of data clearing provider. | MaxLen: 127
    wba_data_clearing_provider: str
    # Three letter currency code. | MaxLen: 3
    wba_charging_currency: str
    # Number of currency units per kilobyte. | Default: 0 | Min: 0 | Max: 4294967295
    wba_charging_rate: int
    
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
    def to_dict(self) -> HsProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HsProfile:
    """
    Configure hotspot profile.
    
    Path: wireless_controller/hotspot20/hs_profile
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
    ) -> HsProfileObject: ...
    
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
    ) -> HsProfileObject: ...
    
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
    ) -> FortiObjectList[HsProfileObject]: ...
    
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
    ) -> HsProfileObject: ...
    
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
    ) -> HsProfileObject: ...
    
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
    ) -> FortiObjectList[HsProfileObject]: ...
    
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
    ) -> HsProfileObject: ...
    
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
    ) -> HsProfileObject: ...
    
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
    ) -> FortiObjectList[HsProfileObject]: ...
    
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
    ) -> HsProfileObject | list[HsProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> HsProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> HsProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HsProfileObject: ...
    
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
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
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
    "HsProfile",
    "HsProfilePayload",
    "HsProfileResponse",
    "HsProfileObject",
]