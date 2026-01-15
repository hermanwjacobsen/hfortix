from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FctemsPayload(TypedDict, total=False):
    """
    Type hints for endpoint_control/fctems payload fields.
    
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: verifying-ca)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: verifying-ca)

    **Usage:**
        payload: FctemsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ems_id: int  # EMS ID in order (1 - 7). | Default: 0 | Min: 1 | Max: 7
    status: Literal["enable", "disable"]  # Enable or disable this EMS configuration. | Default: disable
    name: str  # FortiClient Enterprise Management Server (EMS) nam | MaxLen: 35
    dirty_reason: Literal["none", "mismatched-ems-sn"]  # Dirty Reason for FortiClient EMS. | Default: none
    fortinetone_cloud_authentication: Literal["enable", "disable"]  # Enable/disable authentication of FortiClient EMS C | Default: disable
    cloud_authentication_access_key: str  # FortiClient EMS Cloud multitenancy access key | MaxLen: 20
    server: str  # FortiClient EMS FQDN or IPv4 address. | MaxLen: 255
    https_port: int  # FortiClient EMS HTTPS access port number. | Default: 443 | Min: 1 | Max: 65535
    serial_number: str  # EMS Serial Number. | MaxLen: 16
    tenant_id: str  # EMS Tenant ID. | MaxLen: 32
    source_ip: str  # REST API call source IP. | Default: 0.0.0.0
    pull_sysinfo: Literal["enable", "disable"]  # Enable/disable pulling SysInfo from EMS. | Default: enable
    pull_vulnerabilities: Literal["enable", "disable"]  # Enable/disable pulling vulnerabilities from EMS. | Default: enable
    pull_tags: Literal["enable", "disable"]  # Enable/disable pulling FortiClient user tags from | Default: enable
    pull_malware_hash: Literal["enable", "disable"]  # Enable/disable pulling FortiClient malware hash fr | Default: enable
    capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"]  # List of EMS capabilities.
    call_timeout: int  # FortiClient EMS call timeout in seconds | Default: 30 | Min: 1 | Max: 180
    out_of_sync_threshold: int  # Outdated resource threshold in seconds | Default: 180 | Min: 10 | Max: 3600
    send_tags_to_all_vdoms: Literal["enable", "disable"]  # Relax restrictions on tags to send all EMS tags to | Default: disable
    websocket_override: Literal["enable", "disable"]  # Enable/disable override behavior for how this Fort | Default: disable
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    trust_ca_cn: Literal["enable", "disable"]  # Enable/disable trust of the EMS certificate issuer | Default: enable
    verifying_ca: str  # Lowest CA cert on Fortigate in verified EMS cert c | MaxLen: 79

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FctemsResponse(TypedDict):
    """
    Type hints for endpoint_control/fctems API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ems_id: int  # EMS ID in order (1 - 7). | Default: 0 | Min: 1 | Max: 7
    status: Literal["enable", "disable"]  # Enable or disable this EMS configuration. | Default: disable
    name: str  # FortiClient Enterprise Management Server (EMS) nam | MaxLen: 35
    dirty_reason: Literal["none", "mismatched-ems-sn"]  # Dirty Reason for FortiClient EMS. | Default: none
    fortinetone_cloud_authentication: Literal["enable", "disable"]  # Enable/disable authentication of FortiClient EMS C | Default: disable
    cloud_authentication_access_key: str  # FortiClient EMS Cloud multitenancy access key | MaxLen: 20
    server: str  # FortiClient EMS FQDN or IPv4 address. | MaxLen: 255
    https_port: int  # FortiClient EMS HTTPS access port number. | Default: 443 | Min: 1 | Max: 65535
    serial_number: str  # EMS Serial Number. | MaxLen: 16
    tenant_id: str  # EMS Tenant ID. | MaxLen: 32
    source_ip: str  # REST API call source IP. | Default: 0.0.0.0
    pull_sysinfo: Literal["enable", "disable"]  # Enable/disable pulling SysInfo from EMS. | Default: enable
    pull_vulnerabilities: Literal["enable", "disable"]  # Enable/disable pulling vulnerabilities from EMS. | Default: enable
    pull_tags: Literal["enable", "disable"]  # Enable/disable pulling FortiClient user tags from | Default: enable
    pull_malware_hash: Literal["enable", "disable"]  # Enable/disable pulling FortiClient malware hash fr | Default: enable
    capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"]  # List of EMS capabilities.
    call_timeout: int  # FortiClient EMS call timeout in seconds | Default: 30 | Min: 1 | Max: 180
    out_of_sync_threshold: int  # Outdated resource threshold in seconds | Default: 180 | Min: 10 | Max: 3600
    send_tags_to_all_vdoms: Literal["enable", "disable"]  # Relax restrictions on tags to send all EMS tags to | Default: disable
    websocket_override: Literal["enable", "disable"]  # Enable/disable override behavior for how this Fort | Default: disable
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    trust_ca_cn: Literal["enable", "disable"]  # Enable/disable trust of the EMS certificate issuer | Default: enable
    verifying_ca: str  # Lowest CA cert on Fortigate in verified EMS cert c | MaxLen: 79


@final
class FctemsObject:
    """Typed FortiObject for endpoint_control/fctems with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # EMS ID in order (1 - 7). | Default: 0 | Min: 1 | Max: 7
    ems_id: int
    # Enable or disable this EMS configuration. | Default: disable
    status: Literal["enable", "disable"]
    # FortiClient Enterprise Management Server (EMS) name. | MaxLen: 35
    name: str
    # Dirty Reason for FortiClient EMS. | Default: none
    dirty_reason: Literal["none", "mismatched-ems-sn"]
    # Enable/disable authentication of FortiClient EMS Cloud throu | Default: disable
    fortinetone_cloud_authentication: Literal["enable", "disable"]
    # FortiClient EMS Cloud multitenancy access key | MaxLen: 20
    cloud_authentication_access_key: str
    # FortiClient EMS FQDN or IPv4 address. | MaxLen: 255
    server: str
    # FortiClient EMS HTTPS access port number. | Default: 443 | Min: 1 | Max: 65535
    https_port: int
    # EMS Serial Number. | MaxLen: 16
    serial_number: str
    # EMS Tenant ID. | MaxLen: 32
    tenant_id: str
    # REST API call source IP. | Default: 0.0.0.0
    source_ip: str
    # Enable/disable pulling SysInfo from EMS. | Default: enable
    pull_sysinfo: Literal["enable", "disable"]
    # Enable/disable pulling vulnerabilities from EMS. | Default: enable
    pull_vulnerabilities: Literal["enable", "disable"]
    # Enable/disable pulling FortiClient user tags from EMS. | Default: enable
    pull_tags: Literal["enable", "disable"]
    # Enable/disable pulling FortiClient malware hash from EMS. | Default: enable
    pull_malware_hash: Literal["enable", "disable"]
    # List of EMS capabilities.
    capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"]
    # FortiClient EMS call timeout in seconds | Default: 30 | Min: 1 | Max: 180
    call_timeout: int
    # Outdated resource threshold in seconds | Default: 180 | Min: 10 | Max: 3600
    out_of_sync_threshold: int
    # Relax restrictions on tags to send all EMS tags to all VDOMs | Default: disable
    send_tags_to_all_vdoms: Literal["enable", "disable"]
    # Enable/disable override behavior for how this FortiGate unit | Default: disable
    websocket_override: Literal["enable", "disable"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # Enable/disable trust of the EMS certificate issuer(CA) and c | Default: enable
    trust_ca_cn: Literal["enable", "disable"]
    # Lowest CA cert on Fortigate in verified EMS cert chain. | MaxLen: 79
    verifying_ca: str
    
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
    def to_dict(self) -> FctemsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fctems:
    """
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    Path: endpoint_control/fctems
    Category: cmdb
    Primary Key: ems-id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        ems_id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[FctemsObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
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
    ) -> FortiObjectList[FctemsObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        ems_id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
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
    ) -> FortiObjectList[FctemsObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        ems_id: int | None = ...,
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
        ems_id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject | list[FctemsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FctemsObject: ...
    
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        ems_id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FctemsPayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
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
    "Fctems",
    "FctemsPayload",
    "FctemsResponse",
    "FctemsObject",
]