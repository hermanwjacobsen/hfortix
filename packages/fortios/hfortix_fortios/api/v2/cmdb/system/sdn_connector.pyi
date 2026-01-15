from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SdnConnectorPayload(TypedDict, total=False):
    """
    Type hints for system/sdn_connector payload fields.
    
    Configure connection to SDN Connector.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: server-ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: oci-cert)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: server-ca-cert, server-cert)
        - :class:`~.system.sdn-proxy.SdnProxyEndpoint` (via: proxy)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: SdnConnectorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SDN connector name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable connection to the remote SDN connec | Default: enable
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]  # Type of SDN connector. | Default: aws
    proxy: str  # SDN proxy. | MaxLen: 35
    use_metadata_iam: Literal["disable", "enable"]  # Enable/disable use of IAM role from metadata to ca | Default: disable
    microsoft_365: Literal["disable", "enable"]  # Enable to use as Microsoft 365 connector. | Default: disable
    ha_status: Literal["disable", "enable"]  # Enable/disable use for FortiGate HA service. | Default: disable
    verify_certificate: Literal["disable", "enable"]  # Enable/disable server certificate verification. | Default: enable
    vdom: str  # Virtual domain name of the remote SDN connector. | MaxLen: 31
    server: str  # Server address of the remote SDN connector. | MaxLen: 127
    server_list: list[dict[str, Any]]  # Server address list of the remote SDN connector.
    server_port: int  # Port number of the remote SDN connector. | Default: 0 | Min: 0 | Max: 65535
    message_server_port: int  # HTTP port number of the SAP message server. | Default: 0 | Min: 0 | Max: 65535
    username: str  # Username of the remote SDN connector as login cred | MaxLen: 64
    password: str  # Password of the remote SDN connector as login cred
    vcenter_server: str  # vCenter server address for NSX quarantine. | MaxLen: 127
    vcenter_username: str  # vCenter server username for NSX quarantine. | MaxLen: 64
    vcenter_password: str  # vCenter server password for NSX quarantine.
    access_key: str  # AWS / ACS access key ID. | MaxLen: 31
    secret_key: str  # AWS / ACS secret access key. | MaxLen: 59
    region: str  # AWS / ACS region name. | MaxLen: 31
    vpc_id: str  # AWS VPC ID. | MaxLen: 31
    alt_resource_ip: Literal["disable", "enable"]  # Enable/disable AWS alternative resource IP. | Default: disable
    external_account_list: list[dict[str, Any]]  # Configure AWS external account list.
    tenant_id: str  # Tenant ID (directory ID). | MaxLen: 127
    client_id: str  # Azure client ID (application ID). | MaxLen: 63
    client_secret: str  # Azure client secret (application key). | MaxLen: 59
    subscription_id: str  # Azure subscription ID. | MaxLen: 63
    resource_group: str  # Azure resource group. | MaxLen: 63
    login_endpoint: str  # Azure Stack login endpoint. | MaxLen: 127
    resource_url: str  # Azure Stack resource URL. | MaxLen: 127
    azure_region: Literal["global", "china", "germany", "usgov", "local"]  # Azure server region. | Default: global
    nic: list[dict[str, Any]]  # Configure Azure network interface.
    route_table: list[dict[str, Any]]  # Configure Azure route table.
    user_id: str  # User ID. | MaxLen: 127
    compartment_list: list[dict[str, Any]]  # Configure OCI compartment list.
    oci_region_list: list[dict[str, Any]]  # Configure OCI region list.
    oci_region_type: Literal["commercial", "government"]  # OCI region type. | Default: commercial
    oci_cert: str  # OCI certificate. | MaxLen: 63
    oci_fingerprint: str  # OCI pubkey fingerprint. | MaxLen: 63
    external_ip: list[dict[str, Any]]  # Configure GCP external IP.
    route: list[dict[str, Any]]  # Configure GCP route.
    gcp_project_list: list[dict[str, Any]]  # Configure GCP project list.
    forwarding_rule: list[dict[str, Any]]  # Configure GCP forwarding rule.
    service_account: str  # GCP service account email. | MaxLen: 127
    private_key: str  # Private key of GCP service account.
    secret_token: str  # Secret token of Kubernetes service account.
    domain: str  # Domain name. | MaxLen: 127
    group_name: str  # Full path group name of computers. | MaxLen: 127
    server_cert: str  # Trust servers that contain this certificate only. | MaxLen: 127
    server_ca_cert: str  # Trust only those servers whose certificate is dire | MaxLen: 127
    api_key: str  # IBM cloud API key or service ID API key. | MaxLen: 59
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]  # IBM cloud region name. | Default: dallas
    par_id: str  # Public address range ID. | MaxLen: 63
    update_interval: int  # Dynamic object update interval | Default: 60 | Min: 0 | Max: 3600

# Nested TypedDicts for table field children (dict mode)

class SdnConnectorServerlistItem(TypedDict):
    """Type hints for server-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IPv4 address. | MaxLen: 15


class SdnConnectorExternalaccountlistItem(TypedDict):
    """Type hints for external-account-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    role_arn: str  # AWS role ARN to assume. | MaxLen: 2047
    external_id: str  # AWS external ID. | MaxLen: 1399
    region_list: str  # AWS region name list.


class SdnConnectorNicItem(TypedDict):
    """Type hints for nic table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Network interface name. | MaxLen: 63
    peer_nic: str  # Peer network interface name. | MaxLen: 63
    ip: str  # Configure IP configuration.


class SdnConnectorRoutetableItem(TypedDict):
    """Type hints for route-table table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Route table name. | MaxLen: 63
    subscription_id: str  # Subscription ID of Azure route table. | MaxLen: 63
    resource_group: str  # Resource group of Azure route table. | MaxLen: 63
    route: str  # Configure Azure route.


class SdnConnectorCompartmentlistItem(TypedDict):
    """Type hints for compartment-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    compartment_id: str  # OCI compartment ID. | MaxLen: 127


class SdnConnectorOciregionlistItem(TypedDict):
    """Type hints for oci-region-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    region: str  # OCI region. | MaxLen: 31


class SdnConnectorExternalipItem(TypedDict):
    """Type hints for external-ip table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # External IP name. | MaxLen: 63


class SdnConnectorRouteItem(TypedDict):
    """Type hints for route table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Route name. | MaxLen: 63


class SdnConnectorGcpprojectlistItem(TypedDict):
    """Type hints for gcp-project-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: str  # GCP project ID. | MaxLen: 127
    gcp_zone_list: str  # Configure GCP zone list.


class SdnConnectorForwardingruleItem(TypedDict):
    """Type hints for forwarding-rule table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    rule_name: str  # Forwarding rule name. | MaxLen: 63
    target: str  # Target instance name. | MaxLen: 63


# Nested classes for table field children (object mode)

@final
class SdnConnectorServerlistObject:
    """Typed object for server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv4 address. | MaxLen: 15
    ip: str
    
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
class SdnConnectorExternalaccountlistObject:
    """Typed object for external-account-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # AWS role ARN to assume. | MaxLen: 2047
    role_arn: str
    # AWS external ID. | MaxLen: 1399
    external_id: str
    # AWS region name list.
    region_list: str
    
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
class SdnConnectorNicObject:
    """Typed object for nic table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network interface name. | MaxLen: 63
    name: str
    # Peer network interface name. | MaxLen: 63
    peer_nic: str
    # Configure IP configuration.
    ip: str
    
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
class SdnConnectorRoutetableObject:
    """Typed object for route-table table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route table name. | MaxLen: 63
    name: str
    # Subscription ID of Azure route table. | MaxLen: 63
    subscription_id: str
    # Resource group of Azure route table. | MaxLen: 63
    resource_group: str
    # Configure Azure route.
    route: str
    
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
class SdnConnectorCompartmentlistObject:
    """Typed object for compartment-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # OCI compartment ID. | MaxLen: 127
    compartment_id: str
    
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
class SdnConnectorOciregionlistObject:
    """Typed object for oci-region-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # OCI region. | MaxLen: 31
    region: str
    
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
class SdnConnectorExternalipObject:
    """Typed object for external-ip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # External IP name. | MaxLen: 63
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
class SdnConnectorRouteObject:
    """Typed object for route table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route name. | MaxLen: 63
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
class SdnConnectorGcpprojectlistObject:
    """Typed object for gcp-project-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # GCP project ID. | MaxLen: 127
    id: str
    # Configure GCP zone list.
    gcp_zone_list: str
    
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
class SdnConnectorForwardingruleObject:
    """Typed object for forwarding-rule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Forwarding rule name. | MaxLen: 63
    rule_name: str
    # Target instance name. | MaxLen: 63
    target: str
    
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
class SdnConnectorResponse(TypedDict):
    """
    Type hints for system/sdn_connector API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # SDN connector name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable connection to the remote SDN connec | Default: enable
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]  # Type of SDN connector. | Default: aws
    proxy: str  # SDN proxy. | MaxLen: 35
    use_metadata_iam: Literal["disable", "enable"]  # Enable/disable use of IAM role from metadata to ca | Default: disable
    microsoft_365: Literal["disable", "enable"]  # Enable to use as Microsoft 365 connector. | Default: disable
    ha_status: Literal["disable", "enable"]  # Enable/disable use for FortiGate HA service. | Default: disable
    verify_certificate: Literal["disable", "enable"]  # Enable/disable server certificate verification. | Default: enable
    vdom: str  # Virtual domain name of the remote SDN connector. | MaxLen: 31
    server: str  # Server address of the remote SDN connector. | MaxLen: 127
    server_list: list[SdnConnectorServerlistItem]  # Server address list of the remote SDN connector.
    server_port: int  # Port number of the remote SDN connector. | Default: 0 | Min: 0 | Max: 65535
    message_server_port: int  # HTTP port number of the SAP message server. | Default: 0 | Min: 0 | Max: 65535
    username: str  # Username of the remote SDN connector as login cred | MaxLen: 64
    password: str  # Password of the remote SDN connector as login cred
    vcenter_server: str  # vCenter server address for NSX quarantine. | MaxLen: 127
    vcenter_username: str  # vCenter server username for NSX quarantine. | MaxLen: 64
    vcenter_password: str  # vCenter server password for NSX quarantine.
    access_key: str  # AWS / ACS access key ID. | MaxLen: 31
    secret_key: str  # AWS / ACS secret access key. | MaxLen: 59
    region: str  # AWS / ACS region name. | MaxLen: 31
    vpc_id: str  # AWS VPC ID. | MaxLen: 31
    alt_resource_ip: Literal["disable", "enable"]  # Enable/disable AWS alternative resource IP. | Default: disable
    external_account_list: list[SdnConnectorExternalaccountlistItem]  # Configure AWS external account list.
    tenant_id: str  # Tenant ID (directory ID). | MaxLen: 127
    client_id: str  # Azure client ID (application ID). | MaxLen: 63
    client_secret: str  # Azure client secret (application key). | MaxLen: 59
    subscription_id: str  # Azure subscription ID. | MaxLen: 63
    resource_group: str  # Azure resource group. | MaxLen: 63
    login_endpoint: str  # Azure Stack login endpoint. | MaxLen: 127
    resource_url: str  # Azure Stack resource URL. | MaxLen: 127
    azure_region: Literal["global", "china", "germany", "usgov", "local"]  # Azure server region. | Default: global
    nic: list[SdnConnectorNicItem]  # Configure Azure network interface.
    route_table: list[SdnConnectorRoutetableItem]  # Configure Azure route table.
    user_id: str  # User ID. | MaxLen: 127
    compartment_list: list[SdnConnectorCompartmentlistItem]  # Configure OCI compartment list.
    oci_region_list: list[SdnConnectorOciregionlistItem]  # Configure OCI region list.
    oci_region_type: Literal["commercial", "government"]  # OCI region type. | Default: commercial
    oci_cert: str  # OCI certificate. | MaxLen: 63
    oci_fingerprint: str  # OCI pubkey fingerprint. | MaxLen: 63
    external_ip: list[SdnConnectorExternalipItem]  # Configure GCP external IP.
    route: list[SdnConnectorRouteItem]  # Configure GCP route.
    gcp_project_list: list[SdnConnectorGcpprojectlistItem]  # Configure GCP project list.
    forwarding_rule: list[SdnConnectorForwardingruleItem]  # Configure GCP forwarding rule.
    service_account: str  # GCP service account email. | MaxLen: 127
    private_key: str  # Private key of GCP service account.
    secret_token: str  # Secret token of Kubernetes service account.
    domain: str  # Domain name. | MaxLen: 127
    group_name: str  # Full path group name of computers. | MaxLen: 127
    server_cert: str  # Trust servers that contain this certificate only. | MaxLen: 127
    server_ca_cert: str  # Trust only those servers whose certificate is dire | MaxLen: 127
    api_key: str  # IBM cloud API key or service ID API key. | MaxLen: 59
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]  # IBM cloud region name. | Default: dallas
    par_id: str  # Public address range ID. | MaxLen: 63
    update_interval: int  # Dynamic object update interval | Default: 60 | Min: 0 | Max: 3600


@final
class SdnConnectorObject:
    """Typed FortiObject for system/sdn_connector with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SDN connector name. | MaxLen: 35
    name: str
    # Enable/disable connection to the remote SDN connector. | Default: enable
    status: Literal["disable", "enable"]
    # Type of SDN connector. | Default: aws
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]
    # SDN proxy. | MaxLen: 35
    proxy: str
    # Enable/disable use of IAM role from metadata to call API. | Default: disable
    use_metadata_iam: Literal["disable", "enable"]
    # Enable to use as Microsoft 365 connector. | Default: disable
    microsoft_365: Literal["disable", "enable"]
    # Enable/disable use for FortiGate HA service. | Default: disable
    ha_status: Literal["disable", "enable"]
    # Enable/disable server certificate verification. | Default: enable
    verify_certificate: Literal["disable", "enable"]
    # Virtual domain name of the remote SDN connector. | MaxLen: 31
    vdom: str
    # Server address of the remote SDN connector. | MaxLen: 127
    server: str
    # Server address list of the remote SDN connector.
    server_list: list[SdnConnectorServerlistObject]
    # Port number of the remote SDN connector. | Default: 0 | Min: 0 | Max: 65535
    server_port: int
    # HTTP port number of the SAP message server. | Default: 0 | Min: 0 | Max: 65535
    message_server_port: int
    # Username of the remote SDN connector as login credentials. | MaxLen: 64
    username: str
    # Password of the remote SDN connector as login credentials.
    password: str
    # vCenter server address for NSX quarantine. | MaxLen: 127
    vcenter_server: str
    # vCenter server username for NSX quarantine. | MaxLen: 64
    vcenter_username: str
    # vCenter server password for NSX quarantine.
    vcenter_password: str
    # AWS / ACS access key ID. | MaxLen: 31
    access_key: str
    # AWS / ACS secret access key. | MaxLen: 59
    secret_key: str
    # AWS / ACS region name. | MaxLen: 31
    region: str
    # AWS VPC ID. | MaxLen: 31
    vpc_id: str
    # Enable/disable AWS alternative resource IP. | Default: disable
    alt_resource_ip: Literal["disable", "enable"]
    # Configure AWS external account list.
    external_account_list: list[SdnConnectorExternalaccountlistObject]
    # Tenant ID (directory ID). | MaxLen: 127
    tenant_id: str
    # Azure client ID (application ID). | MaxLen: 63
    client_id: str
    # Azure client secret (application key). | MaxLen: 59
    client_secret: str
    # Azure subscription ID. | MaxLen: 63
    subscription_id: str
    # Azure resource group. | MaxLen: 63
    resource_group: str
    # Azure Stack login endpoint. | MaxLen: 127
    login_endpoint: str
    # Azure Stack resource URL. | MaxLen: 127
    resource_url: str
    # Azure server region. | Default: global
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    # Configure Azure network interface.
    nic: list[SdnConnectorNicObject]
    # Configure Azure route table.
    route_table: list[SdnConnectorRoutetableObject]
    # User ID. | MaxLen: 127
    user_id: str
    # Configure OCI compartment list.
    compartment_list: list[SdnConnectorCompartmentlistObject]
    # Configure OCI region list.
    oci_region_list: list[SdnConnectorOciregionlistObject]
    # OCI region type. | Default: commercial
    oci_region_type: Literal["commercial", "government"]
    # OCI certificate. | MaxLen: 63
    oci_cert: str
    # OCI pubkey fingerprint. | MaxLen: 63
    oci_fingerprint: str
    # Configure GCP external IP.
    external_ip: list[SdnConnectorExternalipObject]
    # Configure GCP route.
    route: list[SdnConnectorRouteObject]
    # Configure GCP project list.
    gcp_project_list: list[SdnConnectorGcpprojectlistObject]
    # Configure GCP forwarding rule.
    forwarding_rule: list[SdnConnectorForwardingruleObject]
    # GCP service account email. | MaxLen: 127
    service_account: str
    # Private key of GCP service account.
    private_key: str
    # Secret token of Kubernetes service account.
    secret_token: str
    # Domain name. | MaxLen: 127
    domain: str
    # Full path group name of computers. | MaxLen: 127
    group_name: str
    # Trust servers that contain this certificate only. | MaxLen: 127
    server_cert: str
    # Trust only those servers whose certificate is directly/indir | MaxLen: 127
    server_ca_cert: str
    # IBM cloud API key or service ID API key. | MaxLen: 59
    api_key: str
    # IBM cloud region name. | Default: dallas
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]
    # Public address range ID. | MaxLen: 63
    par_id: str
    # Dynamic object update interval | Default: 60 | Min: 0 | Max: 3600
    update_interval: int
    
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
    def to_dict(self) -> SdnConnectorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SdnConnector:
    """
    Configure connection to SDN Connector.
    
    Path: system/sdn_connector
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
    ) -> SdnConnectorObject: ...
    
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
    ) -> SdnConnectorObject: ...
    
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
    ) -> list[SdnConnectorObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
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
    ) -> list[SdnConnectorObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
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
    ) -> list[SdnConnectorObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject | list[SdnConnectorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
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
    "SdnConnector",
    "SdnConnectorPayload",
    "SdnConnectorResponse",
    "SdnConnectorObject",
]