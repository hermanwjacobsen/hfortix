from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class InterfacePolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/interface_policy6 payload fields.
    
    Configure IPv6 interface policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: interface)
        - :class:`~.system.zone.ZoneEndpoint` (via: interface)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: webfilter-profile)

    **Usage:**
        payload: InterfacePolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: int  # Policy ID (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable this policy. | Default: enable
    comments: str  # Comments. | MaxLen: 1023
    logtraffic: Literal["all", "utm", "disable"]  # Logging type to be used in this policy | Default: utm
    interface: str  # Monitored interface name from available interfaces | MaxLen: 35
    srcaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to
    dstaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to
    service6: list[dict[str, Any]]  # Service name.
    application_list_status: Literal["enable", "disable"]  # Enable/disable application control. | Default: disable
    application_list: str  # Application list name. | MaxLen: 47
    ips_sensor_status: Literal["enable", "disable"]  # Enable/disable IPS. | Default: disable
    ips_sensor: str  # IPS sensor name. | MaxLen: 47
    dsri: Literal["enable", "disable"]  # Enable/disable DSRI. | Default: disable
    av_profile_status: Literal["enable", "disable"]  # Enable/disable antivirus. | Default: disable
    av_profile: str  # Antivirus profile. | MaxLen: 47
    webfilter_profile_status: Literal["enable", "disable"]  # Enable/disable web filtering. | Default: disable
    webfilter_profile: str  # Web filter profile. | MaxLen: 47
    casb_profile_status: Literal["enable", "disable"]  # Enable/disable CASB. | Default: disable
    casb_profile: str  # CASB profile. | MaxLen: 47
    emailfilter_profile_status: Literal["enable", "disable"]  # Enable/disable email filter. | Default: disable
    emailfilter_profile: str  # Email filter profile. | MaxLen: 47
    dlp_profile_status: Literal["enable", "disable"]  # Enable/disable DLP. | Default: disable
    dlp_profile: str  # DLP profile name. | MaxLen: 47

# Nested TypedDicts for table field children (dict mode)

class InterfacePolicy6Srcaddr6Item(TypedDict):
    """Type hints for srcaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class InterfacePolicy6Dstaddr6Item(TypedDict):
    """Type hints for dstaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class InterfacePolicy6Service6Item(TypedDict):
    """Type hints for service6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Service name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class InterfacePolicy6Srcaddr6Object:
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
class InterfacePolicy6Dstaddr6Object:
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
class InterfacePolicy6Service6Object:
    """Typed object for service6 table items.
    
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



# Response TypedDict for GET returns (all fields present in API response)
class InterfacePolicy6Response(TypedDict):
    """
    Type hints for firewall/interface_policy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int  # Policy ID (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable this policy. | Default: enable
    comments: str  # Comments. | MaxLen: 1023
    logtraffic: Literal["all", "utm", "disable"]  # Logging type to be used in this policy | Default: utm
    interface: str  # Monitored interface name from available interfaces | MaxLen: 35
    srcaddr6: list[InterfacePolicy6Srcaddr6Item]  # IPv6 address object to limit traffic monitoring to
    dstaddr6: list[InterfacePolicy6Dstaddr6Item]  # IPv6 address object to limit traffic monitoring to
    service6: list[InterfacePolicy6Service6Item]  # Service name.
    application_list_status: Literal["enable", "disable"]  # Enable/disable application control. | Default: disable
    application_list: str  # Application list name. | MaxLen: 47
    ips_sensor_status: Literal["enable", "disable"]  # Enable/disable IPS. | Default: disable
    ips_sensor: str  # IPS sensor name. | MaxLen: 47
    dsri: Literal["enable", "disable"]  # Enable/disable DSRI. | Default: disable
    av_profile_status: Literal["enable", "disable"]  # Enable/disable antivirus. | Default: disable
    av_profile: str  # Antivirus profile. | MaxLen: 47
    webfilter_profile_status: Literal["enable", "disable"]  # Enable/disable web filtering. | Default: disable
    webfilter_profile: str  # Web filter profile. | MaxLen: 47
    casb_profile_status: Literal["enable", "disable"]  # Enable/disable CASB. | Default: disable
    casb_profile: str  # CASB profile. | MaxLen: 47
    emailfilter_profile_status: Literal["enable", "disable"]  # Enable/disable email filter. | Default: disable
    emailfilter_profile: str  # Email filter profile. | MaxLen: 47
    dlp_profile_status: Literal["enable", "disable"]  # Enable/disable DLP. | Default: disable
    dlp_profile: str  # DLP profile name. | MaxLen: 47


@final
class InterfacePolicy6Object:
    """Typed FortiObject for firewall/interface_policy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy ID (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    policyid: int
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Enable/disable this policy. | Default: enable
    status: Literal["enable", "disable"]
    # Comments. | MaxLen: 1023
    comments: str
    # Logging type to be used in this policy | Default: utm
    logtraffic: Literal["all", "utm", "disable"]
    # Monitored interface name from available interfaces. | MaxLen: 35
    interface: str
    # IPv6 address object to limit traffic monitoring to network t
    srcaddr6: list[InterfacePolicy6Srcaddr6Object]
    # IPv6 address object to limit traffic monitoring to network t
    dstaddr6: list[InterfacePolicy6Dstaddr6Object]
    # Service name.
    service6: list[InterfacePolicy6Service6Object]
    # Enable/disable application control. | Default: disable
    application_list_status: Literal["enable", "disable"]
    # Application list name. | MaxLen: 47
    application_list: str
    # Enable/disable IPS. | Default: disable
    ips_sensor_status: Literal["enable", "disable"]
    # IPS sensor name. | MaxLen: 47
    ips_sensor: str
    # Enable/disable DSRI. | Default: disable
    dsri: Literal["enable", "disable"]
    # Enable/disable antivirus. | Default: disable
    av_profile_status: Literal["enable", "disable"]
    # Antivirus profile. | MaxLen: 47
    av_profile: str
    # Enable/disable web filtering. | Default: disable
    webfilter_profile_status: Literal["enable", "disable"]
    # Web filter profile. | MaxLen: 47
    webfilter_profile: str
    # Enable/disable CASB. | Default: disable
    casb_profile_status: Literal["enable", "disable"]
    # CASB profile. | MaxLen: 47
    casb_profile: str
    # Enable/disable email filter. | Default: disable
    emailfilter_profile_status: Literal["enable", "disable"]
    # Email filter profile. | MaxLen: 47
    emailfilter_profile: str
    # Enable/disable DLP. | Default: disable
    dlp_profile_status: Literal["enable", "disable"]
    # DLP profile name. | MaxLen: 47
    dlp_profile: str
    
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
    def to_dict(self) -> InterfacePolicy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InterfacePolicy6:
    """
    Configure IPv6 interface policies.
    
    Path: firewall/interface_policy6
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> FortiObjectList[InterfacePolicy6Object]: ...
    
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> FortiObjectList[InterfacePolicy6Object]: ...
    
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> FortiObjectList[InterfacePolicy6Object]: ...
    
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
    ) -> InterfacePolicy6Object | list[InterfacePolicy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
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
    "InterfacePolicy6",
    "InterfacePolicy6Payload",
    "InterfacePolicy6Response",
    "InterfacePolicy6Object",
]