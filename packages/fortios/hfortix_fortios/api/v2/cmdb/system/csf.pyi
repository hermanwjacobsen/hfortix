from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CsfPayload(TypedDict, total=False):
    """
    Type hints for system/csf payload fields.
    
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: downstream-accprofile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: upstream-interface)

    **Usage:**
        payload: CsfPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable Security Fabric. | Default: disable
    uid: str  # Unique ID of the current CSF node | MaxLen: 35
    upstream: str  # IP/FQDN of the FortiGate upstream from this FortiG | MaxLen: 255
    source_ip: str  # Source IP address for communication with the upstr | Default: 0.0.0.0
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    upstream_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    upstream_port: int  # The port number to use to communicate with the For | Default: 8013 | Min: 1 | Max: 65535
    group_name: str  # Security Fabric group name. All FortiGates in a Se | MaxLen: 35
    group_password: str  # Security Fabric group password. For legacy authent | MaxLen: 128
    accept_auth_by_cert: Literal["disable", "enable"]  # Accept connections with unknown certificates and a | Default: enable
    log_unification: Literal["disable", "enable"]  # Enable/disable broadcast of discovery messages for | Default: enable
    authorization_request_type: Literal["serial", "certificate"]  # Authorization request type. | Default: serial
    certificate: str  # Certificate. | MaxLen: 35
    fabric_workers: int  # Number of worker processes for Security Fabric dae | Default: 2 | Min: 1 | Max: 4
    downstream_access: Literal["enable", "disable"]  # Enable/disable downstream device access to this de | Default: disable
    legacy_authentication: Literal["disable", "enable"]  # Enable/disable legacy authentication. | Default: disable
    downstream_accprofile: str  # Default access profile for requests from downstrea | MaxLen: 35
    configuration_sync: Literal["default", "local"]  # Configuration sync mode. | Default: default
    fabric_object_unification: Literal["default", "local"]  # Fabric CMDB Object Unification. | Default: default
    saml_configuration_sync: Literal["default", "local"]  # SAML setting configuration synchronization. | Default: default
    trusted_list: list[dict[str, Any]]  # Pre-authorized and blocked security fabric nodes.
    fabric_connector: list[dict[str, Any]]  # Fabric connector configuration.
    forticloud_account_enforcement: Literal["enable", "disable"]  # Fabric FortiCloud account unification. | Default: enable
    file_mgmt: Literal["enable", "disable"]  # Enable/disable Security Fabric daemon file managem | Default: enable
    file_quota: int  # Maximum amount of memory that can be used by the d | Default: 0 | Min: 0 | Max: 4294967295
    file_quota_warning: int  # Warn when the set percentage of quota has been use | Default: 90 | Min: 1 | Max: 99

# Nested TypedDicts for table field children (dict mode)

class CsfTrustedlistItem(TypedDict):
    """Type hints for trusted-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name. | MaxLen: 35
    authorization_type: Literal["serial", "certificate"]  # Authorization type. | Default: serial
    serial: str  # Serial. | MaxLen: 19
    certificate: str  # Certificate. | MaxLen: 32767
    action: Literal["accept", "deny"]  # Security fabric authorization action. | Default: accept
    ha_members: str  # HA members. | MaxLen: 19
    downstream_authorization: Literal["enable", "disable"]  # Trust authorizations by this node's administrator. | Default: disable
    index: int  # Index of the downstream in tree. | Default: 0 | Min: 1 | Max: 1024


class CsfFabricconnectorItem(TypedDict):
    """Type hints for fabric-connector table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    serial: str  # Serial. | MaxLen: 19
    accprofile: str  # Override access profile. | MaxLen: 35
    configuration_write_access: Literal["enable", "disable"]  # Enable/disable downstream device write access to c | Default: disable
    vdom: str  # Virtual domains that the connector has access to.


# Nested classes for table field children (object mode)

@final
class CsfTrustedlistObject:
    """Typed object for trusted-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Authorization type. | Default: serial
    authorization_type: Literal["serial", "certificate"]
    # Serial. | MaxLen: 19
    serial: str
    # Certificate. | MaxLen: 32767
    certificate: str
    # Security fabric authorization action. | Default: accept
    action: Literal["accept", "deny"]
    # HA members. | MaxLen: 19
    ha_members: str
    # Trust authorizations by this node's administrator. | Default: disable
    downstream_authorization: Literal["enable", "disable"]
    # Index of the downstream in tree. | Default: 0 | Min: 1 | Max: 1024
    index: int
    
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
class CsfFabricconnectorObject:
    """Typed object for fabric-connector table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial. | MaxLen: 19
    serial: str
    # Override access profile. | MaxLen: 35
    accprofile: str
    # Enable/disable downstream device write access to configurati | Default: disable
    configuration_write_access: Literal["enable", "disable"]
    # Virtual domains that the connector has access to. If none ar
    vdom: str
    
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
class CsfResponse(TypedDict):
    """
    Type hints for system/csf API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable Security Fabric. | Default: disable
    uid: str  # Unique ID of the current CSF node | MaxLen: 35
    upstream: str  # IP/FQDN of the FortiGate upstream from this FortiG | MaxLen: 255
    source_ip: str  # Source IP address for communication with the upstr | Default: 0.0.0.0
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    upstream_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    upstream_port: int  # The port number to use to communicate with the For | Default: 8013 | Min: 1 | Max: 65535
    group_name: str  # Security Fabric group name. All FortiGates in a Se | MaxLen: 35
    group_password: str  # Security Fabric group password. For legacy authent | MaxLen: 128
    accept_auth_by_cert: Literal["disable", "enable"]  # Accept connections with unknown certificates and a | Default: enable
    log_unification: Literal["disable", "enable"]  # Enable/disable broadcast of discovery messages for | Default: enable
    authorization_request_type: Literal["serial", "certificate"]  # Authorization request type. | Default: serial
    certificate: str  # Certificate. | MaxLen: 35
    fabric_workers: int  # Number of worker processes for Security Fabric dae | Default: 2 | Min: 1 | Max: 4
    downstream_access: Literal["enable", "disable"]  # Enable/disable downstream device access to this de | Default: disable
    legacy_authentication: Literal["disable", "enable"]  # Enable/disable legacy authentication. | Default: disable
    downstream_accprofile: str  # Default access profile for requests from downstrea | MaxLen: 35
    configuration_sync: Literal["default", "local"]  # Configuration sync mode. | Default: default
    fabric_object_unification: Literal["default", "local"]  # Fabric CMDB Object Unification. | Default: default
    saml_configuration_sync: Literal["default", "local"]  # SAML setting configuration synchronization. | Default: default
    trusted_list: list[CsfTrustedlistItem]  # Pre-authorized and blocked security fabric nodes.
    fabric_connector: list[CsfFabricconnectorItem]  # Fabric connector configuration.
    forticloud_account_enforcement: Literal["enable", "disable"]  # Fabric FortiCloud account unification. | Default: enable
    file_mgmt: Literal["enable", "disable"]  # Enable/disable Security Fabric daemon file managem | Default: enable
    file_quota: int  # Maximum amount of memory that can be used by the d | Default: 0 | Min: 0 | Max: 4294967295
    file_quota_warning: int  # Warn when the set percentage of quota has been use | Default: 90 | Min: 1 | Max: 99


@final
class CsfObject:
    """Typed FortiObject for system/csf with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable Security Fabric. | Default: disable
    status: Literal["enable", "disable"]
    # Unique ID of the current CSF node | MaxLen: 35
    uid: str
    # IP/FQDN of the FortiGate upstream from this FortiGate in the | MaxLen: 255
    upstream: str
    # Source IP address for communication with the upstream FortiG | Default: 0.0.0.0
    source_ip: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    upstream_interface: str
    # The port number to use to communicate with the FortiGate ups | Default: 8013 | Min: 1 | Max: 65535
    upstream_port: int
    # Security Fabric group name. All FortiGates in a Security Fab | MaxLen: 35
    group_name: str
    # Security Fabric group password. For legacy authentication, f | MaxLen: 128
    group_password: str
    # Accept connections with unknown certificates and ask admin f | Default: enable
    accept_auth_by_cert: Literal["disable", "enable"]
    # Enable/disable broadcast of discovery messages for log unifi | Default: enable
    log_unification: Literal["disable", "enable"]
    # Authorization request type. | Default: serial
    authorization_request_type: Literal["serial", "certificate"]
    # Certificate. | MaxLen: 35
    certificate: str
    # Number of worker processes for Security Fabric daemon. | Default: 2 | Min: 1 | Max: 4
    fabric_workers: int
    # Enable/disable downstream device access to this device's con | Default: disable
    downstream_access: Literal["enable", "disable"]
    # Enable/disable legacy authentication. | Default: disable
    legacy_authentication: Literal["disable", "enable"]
    # Default access profile for requests from downstream devices. | MaxLen: 35
    downstream_accprofile: str
    # Configuration sync mode. | Default: default
    configuration_sync: Literal["default", "local"]
    # Fabric CMDB Object Unification. | Default: default
    fabric_object_unification: Literal["default", "local"]
    # SAML setting configuration synchronization. | Default: default
    saml_configuration_sync: Literal["default", "local"]
    # Pre-authorized and blocked security fabric nodes.
    trusted_list: list[CsfTrustedlistObject]
    # Fabric connector configuration.
    fabric_connector: list[CsfFabricconnectorObject]
    # Fabric FortiCloud account unification. | Default: enable
    forticloud_account_enforcement: Literal["enable", "disable"]
    # Enable/disable Security Fabric daemon file management. | Default: enable
    file_mgmt: Literal["enable", "disable"]
    # Maximum amount of memory that can be used by the daemon file | Default: 0 | Min: 0 | Max: 4294967295
    file_quota: int
    # Warn when the set percentage of quota has been used. | Default: 90 | Min: 1 | Max: 99
    file_quota_warning: int
    
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
    def to_dict(self) -> CsfPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Csf:
    """
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Path: system/csf
    Category: cmdb
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> CsfObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> CsfObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
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
    "Csf",
    "CsfPayload",
    "CsfResponse",
    "CsfObject",
]