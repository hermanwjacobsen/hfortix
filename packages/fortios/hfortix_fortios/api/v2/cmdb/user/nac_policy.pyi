from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NacPolicyPayload(TypedDict, total=False):
    """
    Type hints for user/nac_policy payload fields.
    
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: ems-tag, firewall-address, fortivoice-tag)
        - :class:`~.switch-controller.mac-policy.MacPolicyEndpoint` (via: switch-mac-policy)
        - :class:`~.system.interface.InterfaceEndpoint` (via: switch-fortilink)
        - :class:`~.user.group.GroupEndpoint` (via: user-group)
        - :class:`~.wireless-controller.ssid-policy.SsidPolicyEndpoint` (via: ssid-policy)

    **Usage:**
        payload: NacPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # NAC policy name. | MaxLen: 63
    description: str  # Description for the NAC policy matching pattern. | MaxLen: 63
    category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]  # Category of NAC policy. | Default: device
    status: Literal["enable", "disable"]  # Enable/disable NAC policy. | Default: enable
    match_type: Literal["dynamic", "override"]  # Match and retain the devices based on the type. | Default: dynamic
    match_period: int  # Number of days the matched devices will be retaine | Default: 0 | Min: 0 | Max: 120
    match_remove: Literal["default", "link-down"]  # Options to remove the matched override devices. | Default: default
    mac: str  # NAC policy matching MAC address. | MaxLen: 17
    hw_vendor: str  # NAC policy matching hardware vendor. | MaxLen: 15
    type: str  # NAC policy matching type. | MaxLen: 15
    family: str  # NAC policy matching family. | MaxLen: 31
    os: str  # NAC policy matching operating system. | MaxLen: 31
    hw_version: str  # NAC policy matching hardware version. | MaxLen: 15
    sw_version: str  # NAC policy matching software version. | MaxLen: 15
    host: str  # NAC policy matching host. | MaxLen: 64
    user: str  # NAC policy matching user. | MaxLen: 64
    src: str  # NAC policy matching source. | MaxLen: 15
    user_group: str  # NAC policy matching user group. | MaxLen: 35
    ems_tag: str  # NAC policy matching EMS tag. | MaxLen: 79
    fortivoice_tag: str  # NAC policy matching FortiVoice tag. | MaxLen: 79
    severity: list[dict[str, Any]]  # NAC policy matching devices vulnerability severity
    switch_fortilink: str  # FortiLink interface for which this NAC policy belo | MaxLen: 15
    switch_group: list[dict[str, Any]]  # List of managed FortiSwitch groups on which NAC po
    switch_mac_policy: str  # Switch MAC policy action to be applied on the matc | MaxLen: 63
    firewall_address: str  # Dynamic firewall address to associate MAC which ma | MaxLen: 79
    ssid_policy: str  # SSID policy to be applied on the matched NAC polic | MaxLen: 35

# Nested TypedDicts for table field children (dict mode)

class NacPolicySeverityItem(TypedDict):
    """Type hints for severity table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    severity_num: int  # Enter multiple severity levels, where 0 = Info, 1 | Default: 0 | Min: 0 | Max: 4


class NacPolicySwitchgroupItem(TypedDict):
    """Type hints for switch-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Managed FortiSwitch group name from available opti | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class NacPolicySeverityObject:
    """Typed object for severity table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Enter multiple severity levels, where 0 = Info, 1 = Low, ... | Default: 0 | Min: 0 | Max: 4
    severity_num: int
    
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
class NacPolicySwitchgroupObject:
    """Typed object for switch-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Managed FortiSwitch group name from available options. | MaxLen: 79
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
class NacPolicyResponse(TypedDict):
    """
    Type hints for user/nac_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # NAC policy name. | MaxLen: 63
    description: str  # Description for the NAC policy matching pattern. | MaxLen: 63
    category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]  # Category of NAC policy. | Default: device
    status: Literal["enable", "disable"]  # Enable/disable NAC policy. | Default: enable
    match_type: Literal["dynamic", "override"]  # Match and retain the devices based on the type. | Default: dynamic
    match_period: int  # Number of days the matched devices will be retaine | Default: 0 | Min: 0 | Max: 120
    match_remove: Literal["default", "link-down"]  # Options to remove the matched override devices. | Default: default
    mac: str  # NAC policy matching MAC address. | MaxLen: 17
    hw_vendor: str  # NAC policy matching hardware vendor. | MaxLen: 15
    type: str  # NAC policy matching type. | MaxLen: 15
    family: str  # NAC policy matching family. | MaxLen: 31
    os: str  # NAC policy matching operating system. | MaxLen: 31
    hw_version: str  # NAC policy matching hardware version. | MaxLen: 15
    sw_version: str  # NAC policy matching software version. | MaxLen: 15
    host: str  # NAC policy matching host. | MaxLen: 64
    user: str  # NAC policy matching user. | MaxLen: 64
    src: str  # NAC policy matching source. | MaxLen: 15
    user_group: str  # NAC policy matching user group. | MaxLen: 35
    ems_tag: str  # NAC policy matching EMS tag. | MaxLen: 79
    fortivoice_tag: str  # NAC policy matching FortiVoice tag. | MaxLen: 79
    severity: list[NacPolicySeverityItem]  # NAC policy matching devices vulnerability severity
    switch_fortilink: str  # FortiLink interface for which this NAC policy belo | MaxLen: 15
    switch_group: list[NacPolicySwitchgroupItem]  # List of managed FortiSwitch groups on which NAC po
    switch_mac_policy: str  # Switch MAC policy action to be applied on the matc | MaxLen: 63
    firewall_address: str  # Dynamic firewall address to associate MAC which ma | MaxLen: 79
    ssid_policy: str  # SSID policy to be applied on the matched NAC polic | MaxLen: 35


@final
class NacPolicyObject:
    """Typed FortiObject for user/nac_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # NAC policy name. | MaxLen: 63
    name: str
    # Description for the NAC policy matching pattern. | MaxLen: 63
    description: str
    # Category of NAC policy. | Default: device
    category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]
    # Enable/disable NAC policy. | Default: enable
    status: Literal["enable", "disable"]
    # Match and retain the devices based on the type. | Default: dynamic
    match_type: Literal["dynamic", "override"]
    # Number of days the matched devices will be retained | Default: 0 | Min: 0 | Max: 120
    match_period: int
    # Options to remove the matched override devices. | Default: default
    match_remove: Literal["default", "link-down"]
    # NAC policy matching MAC address. | MaxLen: 17
    mac: str
    # NAC policy matching hardware vendor. | MaxLen: 15
    hw_vendor: str
    # NAC policy matching type. | MaxLen: 15
    type: str
    # NAC policy matching family. | MaxLen: 31
    family: str
    # NAC policy matching operating system. | MaxLen: 31
    os: str
    # NAC policy matching hardware version. | MaxLen: 15
    hw_version: str
    # NAC policy matching software version. | MaxLen: 15
    sw_version: str
    # NAC policy matching host. | MaxLen: 64
    host: str
    # NAC policy matching user. | MaxLen: 64
    user: str
    # NAC policy matching source. | MaxLen: 15
    src: str
    # NAC policy matching user group. | MaxLen: 35
    user_group: str
    # NAC policy matching EMS tag. | MaxLen: 79
    ems_tag: str
    # NAC policy matching FortiVoice tag. | MaxLen: 79
    fortivoice_tag: str
    # NAC policy matching devices vulnerability severity lists.
    severity: list[NacPolicySeverityObject]
    # FortiLink interface for which this NAC policy belongs to. | MaxLen: 15
    switch_fortilink: str
    # List of managed FortiSwitch groups on which NAC policy can b
    switch_group: list[NacPolicySwitchgroupObject]
    # Switch MAC policy action to be applied on the matched NAC po | MaxLen: 63
    switch_mac_policy: str
    # Dynamic firewall address to associate MAC which match this p | MaxLen: 79
    firewall_address: str
    # SSID policy to be applied on the matched NAC policy. | MaxLen: 35
    ssid_policy: str
    
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
    def to_dict(self) -> NacPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class NacPolicy:
    """
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Path: user/nac_policy
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
    ) -> NacPolicyObject: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> FortiObjectList[NacPolicyObject]: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> FortiObjectList[NacPolicyObject]: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> FortiObjectList[NacPolicyObject]: ...
    
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
    ) -> NacPolicyObject | list[NacPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacPolicyObject: ...
    
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
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
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
    "NacPolicy",
    "NacPolicyPayload",
    "NacPolicyResponse",
    "NacPolicyObject",
]