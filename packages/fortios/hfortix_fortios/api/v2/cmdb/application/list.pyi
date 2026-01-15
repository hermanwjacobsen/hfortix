from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ListPayload(TypedDict, total=False):
    """
    Type hints for application/list payload fields.
    
    Configure application control lists.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # List name. | MaxLen: 47
    comment: str  # Comments. | MaxLen: 255
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging. | Default: disable
    other_application_action: Literal["pass", "block"]  # Action for other applications. | Default: pass
    app_replacemsg: Literal["disable", "enable"]  # Enable/disable replacement messages for blocked ap | Default: enable
    other_application_log: Literal["disable", "enable"]  # Enable/disable logging for other applications. | Default: disable
    enforce_default_app_port: Literal["disable", "enable"]  # Enable/disable default application port enforcemen | Default: disable
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]  # Enable/disable forced inclusion of SSL deep inspec | Default: disable
    unknown_application_action: Literal["pass", "block"]  # Pass or block traffic from unknown applications. | Default: pass
    unknown_application_log: Literal["disable", "enable"]  # Enable/disable logging for unknown applications. | Default: disable
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]  # P2P applications to be block listed.
    deep_app_inspection: Literal["disable", "enable"]  # Enable/disable deep application inspection. | Default: enable
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]  # Basic application protocol signatures allowed by d | Default: allow-dns
    entries: list[dict[str, Any]]  # Application list entries.
    control_default_network_services: Literal["disable", "enable"]  # Enable/disable enforcement of protocols over selec | Default: disable
    default_network_services: list[dict[str, Any]]  # Default network service entries.

# Nested TypedDicts for table field children (dict mode)

class ListEntriesItem(TypedDict):
    """Type hints for entries table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    risk: str  # Risk, or impact, of allowing traffic from this app
    category: str  # Category ID list.
    application: str  # ID of allowed applications.
    protocols: str  # Application protocol filter. | Default: all
    vendor: str  # Application vendor filter. | Default: all
    technology: str  # Application technology filter. | Default: all
    behavior: str  # Application behavior filter. | Default: all
    popularity: Literal["1", "2", "3", "4", "5"]  # Application popularity filter | Default: 1 2 3 4 5
    exclusion: str  # ID of excluded applications.
    parameters: str  # Application parameters.
    action: Literal["pass", "block", "reset"]  # Pass or block traffic, or reset connection for tra | Default: block
    log: Literal["disable", "enable"]  # Enable/disable logging for this application list. | Default: enable
    log_packet: Literal["disable", "enable"]  # Enable/disable packet logging. | Default: disable
    rate_count: int  # Count of the rate. | Default: 0 | Min: 0 | Max: 65535
    rate_duration: int  # Duration (sec) of the rate. | Default: 60 | Min: 1 | Max: 65535
    rate_mode: Literal["periodical", "continuous"]  # Rate limit mode. | Default: continuous
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]  # Track the packet protocol field. | Default: none
    session_ttl: int  # Session TTL (0 = default). | Default: 0 | Min: 0 | Max: 4294967295
    shaper: str  # Traffic shaper. | MaxLen: 35
    shaper_reverse: str  # Reverse traffic shaper. | MaxLen: 35
    per_ip_shaper: str  # Per-IP traffic shaper. | MaxLen: 35
    quarantine: Literal["none", "attacker"]  # Quarantine method. | Default: none
    quarantine_expiry: str  # Duration of quarantine. | Default: 5m
    quarantine_log: Literal["disable", "enable"]  # Enable/disable quarantine logging. | Default: enable


class ListDefaultnetworkservicesItem(TypedDict):
    """Type hints for default-network-services table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    port: int  # Port number. | Default: 0 | Min: 0 | Max: 65535
    services: Literal["http", "ssh", "telnet", "ftp", "dns", "smtp", "pop3", "imap", "snmp", "nntp", "https"]  # Network protocols.
    violation_action: Literal["pass", "monitor", "block"]  # Action for protocols not in the allowlist for sele | Default: block


# Nested classes for table field children (object mode)

@final
class ListEntriesObject:
    """Typed object for entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Risk, or impact, of allowing traffic from this application t
    risk: str
    # Category ID list.
    category: str
    # ID of allowed applications.
    application: str
    # Application protocol filter. | Default: all
    protocols: str
    # Application vendor filter. | Default: all
    vendor: str
    # Application technology filter. | Default: all
    technology: str
    # Application behavior filter. | Default: all
    behavior: str
    # Application popularity filter | Default: 1 2 3 4 5
    popularity: Literal["1", "2", "3", "4", "5"]
    # ID of excluded applications.
    exclusion: str
    # Application parameters.
    parameters: str
    # Pass or block traffic, or reset connection for traffic from | Default: block
    action: Literal["pass", "block", "reset"]
    # Enable/disable logging for this application list. | Default: enable
    log: Literal["disable", "enable"]
    # Enable/disable packet logging. | Default: disable
    log_packet: Literal["disable", "enable"]
    # Count of the rate. | Default: 0 | Min: 0 | Max: 65535
    rate_count: int
    # Duration (sec) of the rate. | Default: 60 | Min: 1 | Max: 65535
    rate_duration: int
    # Rate limit mode. | Default: continuous
    rate_mode: Literal["periodical", "continuous"]
    # Track the packet protocol field. | Default: none
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]
    # Session TTL (0 = default). | Default: 0 | Min: 0 | Max: 4294967295
    session_ttl: int
    # Traffic shaper. | MaxLen: 35
    shaper: str
    # Reverse traffic shaper. | MaxLen: 35
    shaper_reverse: str
    # Per-IP traffic shaper. | MaxLen: 35
    per_ip_shaper: str
    # Quarantine method. | Default: none
    quarantine: Literal["none", "attacker"]
    # Duration of quarantine. | Default: 5m
    quarantine_expiry: str
    # Enable/disable quarantine logging. | Default: enable
    quarantine_log: Literal["disable", "enable"]
    
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
class ListDefaultnetworkservicesObject:
    """Typed object for default-network-services table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Port number. | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Network protocols.
    services: Literal["http", "ssh", "telnet", "ftp", "dns", "smtp", "pop3", "imap", "snmp", "nntp", "https"]
    # Action for protocols not in the allowlist for selected port. | Default: block
    violation_action: Literal["pass", "monitor", "block"]
    
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
class ListResponse(TypedDict):
    """
    Type hints for application/list API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # List name. | MaxLen: 47
    comment: str  # Comments. | MaxLen: 255
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging. | Default: disable
    other_application_action: Literal["pass", "block"]  # Action for other applications. | Default: pass
    app_replacemsg: Literal["disable", "enable"]  # Enable/disable replacement messages for blocked ap | Default: enable
    other_application_log: Literal["disable", "enable"]  # Enable/disable logging for other applications. | Default: disable
    enforce_default_app_port: Literal["disable", "enable"]  # Enable/disable default application port enforcemen | Default: disable
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]  # Enable/disable forced inclusion of SSL deep inspec | Default: disable
    unknown_application_action: Literal["pass", "block"]  # Pass or block traffic from unknown applications. | Default: pass
    unknown_application_log: Literal["disable", "enable"]  # Enable/disable logging for unknown applications. | Default: disable
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]  # P2P applications to be block listed.
    deep_app_inspection: Literal["disable", "enable"]  # Enable/disable deep application inspection. | Default: enable
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]  # Basic application protocol signatures allowed by d | Default: allow-dns
    entries: list[ListEntriesItem]  # Application list entries.
    control_default_network_services: Literal["disable", "enable"]  # Enable/disable enforcement of protocols over selec | Default: disable
    default_network_services: list[ListDefaultnetworkservicesItem]  # Default network service entries.


@final
class ListObject:
    """Typed FortiObject for application/list with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # List name. | MaxLen: 47
    name: str
    # Comments. | MaxLen: 255
    comment: str
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # Enable/disable extended logging. | Default: disable
    extended_log: Literal["enable", "disable"]
    # Action for other applications. | Default: pass
    other_application_action: Literal["pass", "block"]
    # Enable/disable replacement messages for blocked applications | Default: enable
    app_replacemsg: Literal["disable", "enable"]
    # Enable/disable logging for other applications. | Default: disable
    other_application_log: Literal["disable", "enable"]
    # Enable/disable default application port enforcement for allo | Default: disable
    enforce_default_app_port: Literal["disable", "enable"]
    # Enable/disable forced inclusion of SSL deep inspection signa | Default: disable
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]
    # Pass or block traffic from unknown applications. | Default: pass
    unknown_application_action: Literal["pass", "block"]
    # Enable/disable logging for unknown applications. | Default: disable
    unknown_application_log: Literal["disable", "enable"]
    # P2P applications to be block listed.
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]
    # Enable/disable deep application inspection. | Default: enable
    deep_app_inspection: Literal["disable", "enable"]
    # Basic application protocol signatures allowed by default. | Default: allow-dns
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
    # Application list entries.
    entries: list[ListEntriesObject]
    # Enable/disable enforcement of protocols over selected ports. | Default: disable
    control_default_network_services: Literal["disable", "enable"]
    # Default network service entries.
    default_network_services: list[ListDefaultnetworkservicesObject]
    
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
    def to_dict(self) -> ListPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class List:
    """
    Configure application control lists.
    
    Path: application/list
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
    ) -> ListObject: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> FortiObjectList[ListObject]: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> FortiObjectList[ListObject]: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> FortiObjectList[ListObject]: ...
    
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
    ) -> ListObject | list[ListObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ListObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ListObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ListObject: ...
    
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
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "List",
    "ListPayload",
    "ListResponse",
    "ListObject",
]