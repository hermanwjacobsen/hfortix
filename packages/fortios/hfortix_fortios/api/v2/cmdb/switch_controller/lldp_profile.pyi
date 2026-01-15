from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LldpProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/lldp_profile payload fields.
    
    Configure FortiSwitch LLDP profiles.
    
    **Usage:**
        payload: LldpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 63
    med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"]  # Transmitted LLDP-MED TLVs
    x802_1_tlvs: Literal["port-vlan-id"]  # Transmitted IEEE 802.1 TLVs.
    x802_3_tlvs: Literal["max-frame-size", "power-negotiation"]  # Transmitted IEEE 802.3 TLVs.
    auto_isl: Literal["disable", "enable"]  # Enable/disable auto inter-switch LAG. | Default: enable
    auto_isl_hello_timer: int  # Auto inter-switch LAG hello timer duration | Default: 3 | Min: 1 | Max: 30
    auto_isl_receive_timeout: int  # Auto inter-switch LAG timeout if no response is re | Default: 60 | Min: 0 | Max: 90
    auto_isl_port_group: int  # Auto inter-switch LAG port group ID (0 - 9). | Default: 0 | Min: 0 | Max: 9
    auto_mclag_icl: Literal["disable", "enable"]  # Enable/disable MCLAG inter chassis link. | Default: disable
    auto_isl_auth: Literal["legacy", "strict", "relax"]  # Auto inter-switch LAG authentication mode. | Default: legacy
    auto_isl_auth_user: str  # Auto inter-switch LAG authentication user certific | MaxLen: 63
    auto_isl_auth_identity: str  # Auto inter-switch LAG authentication identity. | MaxLen: 63
    auto_isl_auth_reauth: int  # Auto inter-switch LAG authentication reauth period | Default: 3600 | Min: 180 | Max: 3600
    auto_isl_auth_encrypt: Literal["none", "mixed", "must"]  # Auto inter-switch LAG encryption mode. | Default: none
    auto_isl_auth_macsec_profile: str  # Auto inter-switch LAG macsec profile for encryptio | MaxLen: 63
    med_network_policy: list[dict[str, Any]]  # Configuration method to edit Media Endpoint Discov
    med_location_service: list[dict[str, Any]]  # Configuration method to edit Media Endpoint Discov
    custom_tlvs: list[dict[str, Any]]  # Configuration method to edit custom TLV entries.

# Nested TypedDicts for table field children (dict mode)

class LldpProfileMednetworkpolicyItem(TypedDict):
    """Type hints for med-network-policy table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Policy type name. | MaxLen: 63
    status: Literal["disable", "enable"]  # Enable or disable this TLV. | Default: disable
    vlan_intf: str  # VLAN interface to advertise; if configured on port | MaxLen: 15
    assign_vlan: Literal["disable", "enable"]  # Enable/disable VLAN assignment when this profile i | Default: disable
    priority: int  # Advertised Layer 2 priority | Default: 0 | Min: 0 | Max: 7
    dscp: int  # Advertised Differentiated Services Code Point | Default: 0 | Min: 0 | Max: 63


class LldpProfileMedlocationserviceItem(TypedDict):
    """Type hints for med-location-service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Location service type name. | MaxLen: 63
    status: Literal["disable", "enable"]  # Enable or disable this TLV. | Default: disable
    sys_location_id: str  # Location service ID. | MaxLen: 63


class LldpProfileCustomtlvsItem(TypedDict):
    """Type hints for custom-tlvs table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # TLV name (not sent). | MaxLen: 63
    oui: str  # Organizationally unique identifier (OUI), a 3-byte | Default: 000000
    subtype: int  # Organizationally defined subtype (0 - 255). | Default: 0 | Min: 0 | Max: 255
    information_string: str  # Organizationally defined information string


# Nested classes for table field children (object mode)

@final
class LldpProfileMednetworkpolicyObject:
    """Typed object for med-network-policy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Policy type name. | MaxLen: 63
    name: str
    # Enable or disable this TLV. | Default: disable
    status: Literal["disable", "enable"]
    # VLAN interface to advertise; if configured on port. | MaxLen: 15
    vlan_intf: str
    # Enable/disable VLAN assignment when this profile is applied | Default: disable
    assign_vlan: Literal["disable", "enable"]
    # Advertised Layer 2 priority | Default: 0 | Min: 0 | Max: 7
    priority: int
    # Advertised Differentiated Services Code Point (DSCP) value, | Default: 0 | Min: 0 | Max: 63
    dscp: int
    
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
class LldpProfileMedlocationserviceObject:
    """Typed object for med-location-service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Location service type name. | MaxLen: 63
    name: str
    # Enable or disable this TLV. | Default: disable
    status: Literal["disable", "enable"]
    # Location service ID. | MaxLen: 63
    sys_location_id: str
    
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
class LldpProfileCustomtlvsObject:
    """Typed object for custom-tlvs table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # TLV name (not sent). | MaxLen: 63
    name: str
    # Organizationally unique identifier (OUI), a 3-byte hexadecim | Default: 000000
    oui: str
    # Organizationally defined subtype (0 - 255). | Default: 0 | Min: 0 | Max: 255
    subtype: int
    # Organizationally defined information string
    information_string: str
    
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
class LldpProfileResponse(TypedDict):
    """
    Type hints for switch_controller/lldp_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 63
    med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"]  # Transmitted LLDP-MED TLVs
    x802_1_tlvs: Literal["port-vlan-id"]  # Transmitted IEEE 802.1 TLVs.
    x802_3_tlvs: Literal["max-frame-size", "power-negotiation"]  # Transmitted IEEE 802.3 TLVs.
    auto_isl: Literal["disable", "enable"]  # Enable/disable auto inter-switch LAG. | Default: enable
    auto_isl_hello_timer: int  # Auto inter-switch LAG hello timer duration | Default: 3 | Min: 1 | Max: 30
    auto_isl_receive_timeout: int  # Auto inter-switch LAG timeout if no response is re | Default: 60 | Min: 0 | Max: 90
    auto_isl_port_group: int  # Auto inter-switch LAG port group ID (0 - 9). | Default: 0 | Min: 0 | Max: 9
    auto_mclag_icl: Literal["disable", "enable"]  # Enable/disable MCLAG inter chassis link. | Default: disable
    auto_isl_auth: Literal["legacy", "strict", "relax"]  # Auto inter-switch LAG authentication mode. | Default: legacy
    auto_isl_auth_user: str  # Auto inter-switch LAG authentication user certific | MaxLen: 63
    auto_isl_auth_identity: str  # Auto inter-switch LAG authentication identity. | MaxLen: 63
    auto_isl_auth_reauth: int  # Auto inter-switch LAG authentication reauth period | Default: 3600 | Min: 180 | Max: 3600
    auto_isl_auth_encrypt: Literal["none", "mixed", "must"]  # Auto inter-switch LAG encryption mode. | Default: none
    auto_isl_auth_macsec_profile: str  # Auto inter-switch LAG macsec profile for encryptio | MaxLen: 63
    med_network_policy: list[LldpProfileMednetworkpolicyItem]  # Configuration method to edit Media Endpoint Discov
    med_location_service: list[LldpProfileMedlocationserviceItem]  # Configuration method to edit Media Endpoint Discov
    custom_tlvs: list[LldpProfileCustomtlvsItem]  # Configuration method to edit custom TLV entries.


@final
class LldpProfileObject:
    """Typed FortiObject for switch_controller/lldp_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 63
    name: str
    # Transmitted LLDP-MED TLVs (type-length-value descriptions).
    med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"]
    # Transmitted IEEE 802.1 TLVs.
    x802_1_tlvs: Literal["port-vlan-id"]
    # Transmitted IEEE 802.3 TLVs.
    x802_3_tlvs: Literal["max-frame-size", "power-negotiation"]
    # Enable/disable auto inter-switch LAG. | Default: enable
    auto_isl: Literal["disable", "enable"]
    # Auto inter-switch LAG hello timer duration | Default: 3 | Min: 1 | Max: 30
    auto_isl_hello_timer: int
    # Auto inter-switch LAG timeout if no response is received | Default: 60 | Min: 0 | Max: 90
    auto_isl_receive_timeout: int
    # Auto inter-switch LAG port group ID (0 - 9). | Default: 0 | Min: 0 | Max: 9
    auto_isl_port_group: int
    # Enable/disable MCLAG inter chassis link. | Default: disable
    auto_mclag_icl: Literal["disable", "enable"]
    # Auto inter-switch LAG authentication mode. | Default: legacy
    auto_isl_auth: Literal["legacy", "strict", "relax"]
    # Auto inter-switch LAG authentication user certificate. | MaxLen: 63
    auto_isl_auth_user: str
    # Auto inter-switch LAG authentication identity. | MaxLen: 63
    auto_isl_auth_identity: str
    # Auto inter-switch LAG authentication reauth period in second | Default: 3600 | Min: 180 | Max: 3600
    auto_isl_auth_reauth: int
    # Auto inter-switch LAG encryption mode. | Default: none
    auto_isl_auth_encrypt: Literal["none", "mixed", "must"]
    # Auto inter-switch LAG macsec profile for encryption. | MaxLen: 63
    auto_isl_auth_macsec_profile: str
    # Configuration method to edit Media Endpoint Discovery (MED)
    med_network_policy: list[LldpProfileMednetworkpolicyObject]
    # Configuration method to edit Media Endpoint Discovery (MED)
    med_location_service: list[LldpProfileMedlocationserviceObject]
    # Configuration method to edit custom TLV entries.
    custom_tlvs: list[LldpProfileCustomtlvsObject]
    
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
    def to_dict(self) -> LldpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LldpProfile:
    """
    Configure FortiSwitch LLDP profiles.
    
    Path: switch_controller/lldp_profile
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
    ) -> LldpProfileObject: ...
    
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
    ) -> LldpProfileObject: ...
    
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
    ) -> FortiObjectList[LldpProfileObject]: ...
    
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
    ) -> LldpProfileObject: ...
    
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
    ) -> LldpProfileObject: ...
    
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
    ) -> FortiObjectList[LldpProfileObject]: ...
    
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
    ) -> LldpProfileObject: ...
    
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
    ) -> LldpProfileObject: ...
    
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
    ) -> FortiObjectList[LldpProfileObject]: ...
    
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
    ) -> LldpProfileObject | list[LldpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> LldpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> LldpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LldpProfileObject: ...
    
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
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "LldpProfile",
    "LldpProfilePayload",
    "LldpProfileResponse",
    "LldpProfileObject",
]