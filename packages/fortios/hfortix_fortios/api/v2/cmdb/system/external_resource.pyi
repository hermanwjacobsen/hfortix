from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExternalResourcePayload(TypedDict, total=False):
    """
    Type hints for system/external_resource payload fields.
    
    Configure external resource.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: client-cert)

    **Usage:**
        payload: ExternalResourcePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # External resource name. | MaxLen: 35
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable user resource. | Default: enable
    type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"]  # User resource type. | Default: category
    namespace: str  # Generic external connector address namespace. | MaxLen: 15
    object_array_path: str  # JSON Path to array of generic addresses in resourc | Default: $.addresses | MaxLen: 511
    address_name_field: str  # JSON Path to address name in generic address entry | Default: $.name | MaxLen: 511
    address_data_field: str  # JSON Path to address data in generic address entry | Default: $.value | MaxLen: 511
    address_comment_field: str  # JSON Path to address description in generic addres | Default: $.description | MaxLen: 511
    update_method: Literal["feed", "push"]  # External resource update method. | Default: feed
    category: int  # User resource category. | Default: 0 | Min: 192 | Max: 221
    username: str  # HTTP basic authentication user name. | MaxLen: 64
    password: str  # HTTP basic authentication password.
    client_cert_auth: Literal["enable", "disable"]  # Enable/disable using client certificate for TLS au | Default: disable
    client_cert: str  # Client certificate name. | MaxLen: 79
    comments: str  # Comment. | MaxLen: 255
    resource: str  # URL of external resource. | MaxLen: 511
    user_agent: str  # HTTP User-Agent header (default = 'curl/7.58.0'). | MaxLen: 255
    server_identity_check: Literal["none", "basic", "full"]  # Certificate verification option. | Default: none
    refresh_rate: int  # Time interval to refresh external resource | Default: 5 | Min: 1 | Max: 43200
    source_ip: str  # Source IPv4 address used to communicate with serve | Default: 0.0.0.0
    source_ip_interface: str  # IPv4 Source interface for communication with the s | MaxLen: 15
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ExternalResourceResponse(TypedDict):
    """
    Type hints for system/external_resource API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # External resource name. | MaxLen: 35
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable user resource. | Default: enable
    type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"]  # User resource type. | Default: category
    namespace: str  # Generic external connector address namespace. | MaxLen: 15
    object_array_path: str  # JSON Path to array of generic addresses in resourc | Default: $.addresses | MaxLen: 511
    address_name_field: str  # JSON Path to address name in generic address entry | Default: $.name | MaxLen: 511
    address_data_field: str  # JSON Path to address data in generic address entry | Default: $.value | MaxLen: 511
    address_comment_field: str  # JSON Path to address description in generic addres | Default: $.description | MaxLen: 511
    update_method: Literal["feed", "push"]  # External resource update method. | Default: feed
    category: int  # User resource category. | Default: 0 | Min: 192 | Max: 221
    username: str  # HTTP basic authentication user name. | MaxLen: 64
    password: str  # HTTP basic authentication password.
    client_cert_auth: Literal["enable", "disable"]  # Enable/disable using client certificate for TLS au | Default: disable
    client_cert: str  # Client certificate name. | MaxLen: 79
    comments: str  # Comment. | MaxLen: 255
    resource: str  # URL of external resource. | MaxLen: 511
    user_agent: str  # HTTP User-Agent header (default = 'curl/7.58.0'). | MaxLen: 255
    server_identity_check: Literal["none", "basic", "full"]  # Certificate verification option. | Default: none
    refresh_rate: int  # Time interval to refresh external resource | Default: 5 | Min: 1 | Max: 43200
    source_ip: str  # Source IPv4 address used to communicate with serve | Default: 0.0.0.0
    source_ip_interface: str  # IPv4 Source interface for communication with the s | MaxLen: 15
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class ExternalResourceObject:
    """Typed FortiObject for system/external_resource with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # External resource name. | MaxLen: 35
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Enable/disable user resource. | Default: enable
    status: Literal["enable", "disable"]
    # User resource type. | Default: category
    type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"]
    # Generic external connector address namespace. | MaxLen: 15
    namespace: str
    # JSON Path to array of generic addresses in resource. | Default: $.addresses | MaxLen: 511
    object_array_path: str
    # JSON Path to address name in generic address entry. | Default: $.name | MaxLen: 511
    address_name_field: str
    # JSON Path to address data in generic address entry. | Default: $.value | MaxLen: 511
    address_data_field: str
    # JSON Path to address description in generic address entry. | Default: $.description | MaxLen: 511
    address_comment_field: str
    # External resource update method. | Default: feed
    update_method: Literal["feed", "push"]
    # User resource category. | Default: 0 | Min: 192 | Max: 221
    category: int
    # HTTP basic authentication user name. | MaxLen: 64
    username: str
    # HTTP basic authentication password.
    password: str
    # Enable/disable using client certificate for TLS authenticati | Default: disable
    client_cert_auth: Literal["enable", "disable"]
    # Client certificate name. | MaxLen: 79
    client_cert: str
    # Comment. | MaxLen: 255
    comments: str
    # URL of external resource. | MaxLen: 511
    resource: str
    # HTTP User-Agent header (default = 'curl/7.58.0'). | MaxLen: 255
    user_agent: str
    # Certificate verification option. | Default: none
    server_identity_check: Literal["none", "basic", "full"]
    # Time interval to refresh external resource | Default: 5 | Min: 1 | Max: 43200
    refresh_rate: int
    # Source IPv4 address used to communicate with server. | Default: 0.0.0.0
    source_ip: str
    # IPv4 Source interface for communication with the server. | MaxLen: 15
    source_ip_interface: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
    def to_dict(self) -> ExternalResourcePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExternalResource:
    """
    Configure external resource.
    
    Path: system/external_resource
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> FortiObjectList[ExternalResourceObject]: ...
    
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> FortiObjectList[ExternalResourceObject]: ...
    
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> ExternalResourceObject: ...
    
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
    ) -> FortiObjectList[ExternalResourceObject]: ...
    
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
    ) -> ExternalResourceObject | list[ExternalResourceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalResourceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalResourceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ExternalResourceObject: ...
    
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
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "ExternalResource",
    "ExternalResourcePayload",
    "ExternalResourceResponse",
    "ExternalResourceObject",
]