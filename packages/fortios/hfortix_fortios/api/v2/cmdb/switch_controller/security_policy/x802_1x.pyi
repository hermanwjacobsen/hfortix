from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class X8021xPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/security_policy/x802_1x payload fields.
    
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: auth-fail-vlan-id, authserver-timeout-tagged-vlanid, authserver-timeout-vlanid, +1 more)

    **Usage:**
        payload: X8021xPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Policy name. | MaxLen: 31
    security_mode: Literal["802.1X", "802.1X-mac-based"]  # Port or MAC based 802.1X security mode. | Default: 802.1X
    user_group: list[dict[str, Any]]  # Name of user-group to assign to this MAC Authentic
    mac_auth_bypass: Literal["disable", "enable"]  # Enable/disable MAB for this policy. | Default: disable
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"]  # Configure authentication order. | Default: mab-dot1x
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"]  # Configure authentication priority. | Default: legacy
    open_auth: Literal["disable", "enable"]  # Enable/disable open authentication for this policy | Default: disable
    eap_passthru: Literal["disable", "enable"]  # Enable/disable EAP pass-through mode, allowing pro | Default: enable
    eap_auto_untagged_vlans: Literal["disable", "enable"]  # Enable/disable automatic inclusion of untagged VLA | Default: enable
    guest_vlan: Literal["disable", "enable"]  # Enable the guest VLAN feature to allow limited acc | Default: disable
    guest_vlan_id: str  # Guest VLAN name. | MaxLen: 15
    guest_auth_delay: int  # Guest authentication delay | Default: 30 | Min: 1 | Max: 900
    auth_fail_vlan: Literal["disable", "enable"]  # Enable to allow limited access to clients that can | Default: disable
    auth_fail_vlan_id: str  # VLAN ID on which authentication failed. | MaxLen: 15
    framevid_apply: Literal["disable", "enable"]  # Enable/disable the capability to apply the EAP/MAB | Default: enable
    radius_timeout_overwrite: Literal["disable", "enable"]  # Enable to override the global RADIUS session timeo | Default: disable
    policy_type: Literal["802.1X"]  # Policy type. | Default: 802.1X
    authserver_timeout_period: int  # Authentication server timeout period | Default: 3 | Min: 3 | Max: 15
    authserver_timeout_vlan: Literal["disable", "enable"]  # Enable/disable the authentication server timeout V | Default: disable
    authserver_timeout_vlanid: str  # Authentication server timeout VLAN name. | MaxLen: 15
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"]  # Configure timeout option for the tagged VLAN which | Default: disable
    authserver_timeout_tagged_vlanid: str  # Tagged VLAN name for which the timeout option is a | MaxLen: 15
    dacl: Literal["disable", "enable"]  # Enable/disable dynamic access control list on this | Default: disable

# Nested TypedDicts for table field children (dict mode)

class X8021xUsergroupItem(TypedDict):
    """Type hints for user-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Group name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class X8021xUsergroupObject:
    """Typed object for user-group table items.
    
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
class X8021xResponse(TypedDict):
    """
    Type hints for switch_controller/security_policy/x802_1x API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Policy name. | MaxLen: 31
    security_mode: Literal["802.1X", "802.1X-mac-based"]  # Port or MAC based 802.1X security mode. | Default: 802.1X
    user_group: list[X8021xUsergroupItem]  # Name of user-group to assign to this MAC Authentic
    mac_auth_bypass: Literal["disable", "enable"]  # Enable/disable MAB for this policy. | Default: disable
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"]  # Configure authentication order. | Default: mab-dot1x
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"]  # Configure authentication priority. | Default: legacy
    open_auth: Literal["disable", "enable"]  # Enable/disable open authentication for this policy | Default: disable
    eap_passthru: Literal["disable", "enable"]  # Enable/disable EAP pass-through mode, allowing pro | Default: enable
    eap_auto_untagged_vlans: Literal["disable", "enable"]  # Enable/disable automatic inclusion of untagged VLA | Default: enable
    guest_vlan: Literal["disable", "enable"]  # Enable the guest VLAN feature to allow limited acc | Default: disable
    guest_vlan_id: str  # Guest VLAN name. | MaxLen: 15
    guest_auth_delay: int  # Guest authentication delay | Default: 30 | Min: 1 | Max: 900
    auth_fail_vlan: Literal["disable", "enable"]  # Enable to allow limited access to clients that can | Default: disable
    auth_fail_vlan_id: str  # VLAN ID on which authentication failed. | MaxLen: 15
    framevid_apply: Literal["disable", "enable"]  # Enable/disable the capability to apply the EAP/MAB | Default: enable
    radius_timeout_overwrite: Literal["disable", "enable"]  # Enable to override the global RADIUS session timeo | Default: disable
    policy_type: Literal["802.1X"]  # Policy type. | Default: 802.1X
    authserver_timeout_period: int  # Authentication server timeout period | Default: 3 | Min: 3 | Max: 15
    authserver_timeout_vlan: Literal["disable", "enable"]  # Enable/disable the authentication server timeout V | Default: disable
    authserver_timeout_vlanid: str  # Authentication server timeout VLAN name. | MaxLen: 15
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"]  # Configure timeout option for the tagged VLAN which | Default: disable
    authserver_timeout_tagged_vlanid: str  # Tagged VLAN name for which the timeout option is a | MaxLen: 15
    dacl: Literal["disable", "enable"]  # Enable/disable dynamic access control list on this | Default: disable


@final
class X8021xObject:
    """Typed FortiObject for switch_controller/security_policy/x802_1x with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy name. | MaxLen: 31
    name: str
    # Port or MAC based 802.1X security mode. | Default: 802.1X
    security_mode: Literal["802.1X", "802.1X-mac-based"]
    # Name of user-group to assign to this MAC Authentication Bypa
    user_group: list[X8021xUsergroupObject]
    # Enable/disable MAB for this policy. | Default: disable
    mac_auth_bypass: Literal["disable", "enable"]
    # Configure authentication order. | Default: mab-dot1x
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"]
    # Configure authentication priority. | Default: legacy
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"]
    # Enable/disable open authentication for this policy. | Default: disable
    open_auth: Literal["disable", "enable"]
    # Enable/disable EAP pass-through mode, allowing protocols | Default: enable
    eap_passthru: Literal["disable", "enable"]
    # Enable/disable automatic inclusion of untagged VLANs. | Default: enable
    eap_auto_untagged_vlans: Literal["disable", "enable"]
    # Enable the guest VLAN feature to allow limited access to non | Default: disable
    guest_vlan: Literal["disable", "enable"]
    # Guest VLAN name. | MaxLen: 15
    guest_vlan_id: str
    # Guest authentication delay (1 - 900  sec, default = 30). | Default: 30 | Min: 1 | Max: 900
    guest_auth_delay: int
    # Enable to allow limited access to clients that cannot authen | Default: disable
    auth_fail_vlan: Literal["disable", "enable"]
    # VLAN ID on which authentication failed. | MaxLen: 15
    auth_fail_vlan_id: str
    # Enable/disable the capability to apply the EAP/MAB frame VLA | Default: enable
    framevid_apply: Literal["disable", "enable"]
    # Enable to override the global RADIUS session timeout. | Default: disable
    radius_timeout_overwrite: Literal["disable", "enable"]
    # Policy type. | Default: 802.1X
    policy_type: Literal["802.1X"]
    # Authentication server timeout period | Default: 3 | Min: 3 | Max: 15
    authserver_timeout_period: int
    # Enable/disable the authentication server timeout VLAN to all | Default: disable
    authserver_timeout_vlan: Literal["disable", "enable"]
    # Authentication server timeout VLAN name. | MaxLen: 15
    authserver_timeout_vlanid: str
    # Configure timeout option for the tagged VLAN which allows li | Default: disable
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"]
    # Tagged VLAN name for which the timeout option is applied to | MaxLen: 15
    authserver_timeout_tagged_vlanid: str
    # Enable/disable dynamic access control list on this interface | Default: disable
    dacl: Literal["disable", "enable"]
    
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
    def to_dict(self) -> X8021xPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class X8021x:
    """
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    Path: switch_controller/security_policy/x802_1x
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
    ) -> X8021xObject: ...
    
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
    ) -> X8021xObject: ...
    
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
    ) -> FortiObjectList[X8021xObject]: ...
    
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
    ) -> X8021xObject: ...
    
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
    ) -> X8021xObject: ...
    
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
    ) -> FortiObjectList[X8021xObject]: ...
    
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
    ) -> X8021xObject: ...
    
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
    ) -> X8021xObject: ...
    
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
    ) -> FortiObjectList[X8021xObject]: ...
    
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
    ) -> X8021xObject | list[X8021xObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> X8021xObject: ...
    
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> X8021xObject: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> X8021xObject: ...
    
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
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
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
    "X8021x",
    "X8021xPayload",
    "X8021xResponse",
    "X8021xObject",
]