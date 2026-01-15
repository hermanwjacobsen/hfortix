from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/global_ payload fields.
    
    Configure FortiSwitch global settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: default-virtual-switch-vlan)

    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mac_aging_interval: int  # Time after which an inactive MAC is aged out | Default: 300 | Min: 10 | Max: 1000000
    https_image_push: Literal["enable", "disable"]  # Enable/disable image push to FortiSwitch using HTT | Default: enable
    vlan_all_mode: Literal["all", "defined"]  # VLAN configuration mode, user-defined-vlans or all | Default: defined
    vlan_optimization: Literal["prune", "configured", "none"]  # FortiLink VLAN optimization. | Default: configured
    vlan_identity: Literal["description", "name"]  # Identity of the VLAN. Commonly used for RADIUS Tun | Default: name
    disable_discovery: list[dict[str, Any]]  # Prevent this FortiSwitch from discovering.
    mac_retention_period: int  # Time in hours after which an inactive MAC is remov | Default: 24 | Min: 0 | Max: 168
    default_virtual_switch_vlan: str  # Default VLAN for ports when added to the virtual-s | MaxLen: 15
    dhcp_server_access_list: Literal["enable", "disable"]  # Enable/disable DHCP snooping server access list. | Default: disable
    dhcp_option82_format: Literal["ascii", "legacy"]  # DHCP option-82 format string. | Default: ascii
    dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"]  # List the parameters to be included to inform about | Default: intfname vlan mode
    dhcp_option82_remote_id: Literal["mac", "hostname", "ip"]  # List the parameters to be included to inform about | Default: mac
    dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"]  # Client DHCP packet broadcast mode. | Default: drop-untrusted
    dhcp_snoop_client_db_exp: int  # Expiry time for DHCP snooping server database entr | Default: 86400 | Min: 300 | Max: 259200
    dhcp_snoop_db_per_port_learn_limit: int  # Per Interface dhcp-server entries learn limit | Default: 64 | Min: 0 | Max: 2048
    log_mac_limit_violations: Literal["enable", "disable"]  # Enable/disable logs for Learning Limit Violations. | Default: disable
    mac_violation_timer: int  # Set timeout for Learning Limit Violations | Default: 0 | Min: 0 | Max: 4294967295
    sn_dns_resolution: Literal["enable", "disable"]  # Enable/disable DNS resolution of the FortiSwitch u | Default: enable
    mac_event_logging: Literal["enable", "disable"]  # Enable/disable MAC address event logging. | Default: disable
    bounce_quarantined_link: Literal["disable", "enable"]  # Enable/disable bouncing | Default: disable
    quarantine_mode: Literal["by-vlan", "by-redirect"]  # Quarantine mode. | Default: by-vlan
    update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]  # Control which sources update the device user list. | Default: mac-cache lldp dhcp-snooping l2-db l3-db
    custom_command: list[dict[str, Any]]  # List of custom commands to be pushed to all FortiS
    fips_enforce: Literal["disable", "enable"]  # Enable/disable enforcement of FIPS on managed Fort | Default: enable
    firmware_provision_on_authorization: Literal["enable", "disable"]  # Enable/disable automatic provisioning of latest fi | Default: disable
    switch_on_deauth: Literal["no-op", "factory-reset"]  # No-operation/Factory-reset the managed FortiSwitch | Default: no-op
    firewall_auth_user_hold_period: int  # Time period in minutes to hold firewall authentica | Default: 5 | Min: 5 | Max: 1440

# Nested TypedDicts for table field children (dict mode)

class GlobalDisablediscoveryItem(TypedDict):
    """Type hints for disable-discovery table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FortiSwitch Serial-number. | MaxLen: 79


class GlobalCustomcommandItem(TypedDict):
    """Type hints for custom-command table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    command_entry: str  # List of FortiSwitch commands. | MaxLen: 35
    command_name: str  # Name of custom command to push to all FortiSwitche | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class GlobalDisablediscoveryObject:
    """Typed object for disable-discovery table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiSwitch Serial-number. | MaxLen: 79
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
class GlobalCustomcommandObject:
    """Typed object for custom-command table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # List of FortiSwitch commands. | MaxLen: 35
    command_entry: str
    # Name of custom command to push to all FortiSwitches in VDOM. | MaxLen: 35
    command_name: str
    
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
class GlobalResponse(TypedDict):
    """
    Type hints for switch_controller/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    mac_aging_interval: int  # Time after which an inactive MAC is aged out | Default: 300 | Min: 10 | Max: 1000000
    https_image_push: Literal["enable", "disable"]  # Enable/disable image push to FortiSwitch using HTT | Default: enable
    vlan_all_mode: Literal["all", "defined"]  # VLAN configuration mode, user-defined-vlans or all | Default: defined
    vlan_optimization: Literal["prune", "configured", "none"]  # FortiLink VLAN optimization. | Default: configured
    vlan_identity: Literal["description", "name"]  # Identity of the VLAN. Commonly used for RADIUS Tun | Default: name
    disable_discovery: list[GlobalDisablediscoveryItem]  # Prevent this FortiSwitch from discovering.
    mac_retention_period: int  # Time in hours after which an inactive MAC is remov | Default: 24 | Min: 0 | Max: 168
    default_virtual_switch_vlan: str  # Default VLAN for ports when added to the virtual-s | MaxLen: 15
    dhcp_server_access_list: Literal["enable", "disable"]  # Enable/disable DHCP snooping server access list. | Default: disable
    dhcp_option82_format: Literal["ascii", "legacy"]  # DHCP option-82 format string. | Default: ascii
    dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"]  # List the parameters to be included to inform about | Default: intfname vlan mode
    dhcp_option82_remote_id: Literal["mac", "hostname", "ip"]  # List the parameters to be included to inform about | Default: mac
    dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"]  # Client DHCP packet broadcast mode. | Default: drop-untrusted
    dhcp_snoop_client_db_exp: int  # Expiry time for DHCP snooping server database entr | Default: 86400 | Min: 300 | Max: 259200
    dhcp_snoop_db_per_port_learn_limit: int  # Per Interface dhcp-server entries learn limit | Default: 64 | Min: 0 | Max: 2048
    log_mac_limit_violations: Literal["enable", "disable"]  # Enable/disable logs for Learning Limit Violations. | Default: disable
    mac_violation_timer: int  # Set timeout for Learning Limit Violations | Default: 0 | Min: 0 | Max: 4294967295
    sn_dns_resolution: Literal["enable", "disable"]  # Enable/disable DNS resolution of the FortiSwitch u | Default: enable
    mac_event_logging: Literal["enable", "disable"]  # Enable/disable MAC address event logging. | Default: disable
    bounce_quarantined_link: Literal["disable", "enable"]  # Enable/disable bouncing | Default: disable
    quarantine_mode: Literal["by-vlan", "by-redirect"]  # Quarantine mode. | Default: by-vlan
    update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]  # Control which sources update the device user list. | Default: mac-cache lldp dhcp-snooping l2-db l3-db
    custom_command: list[GlobalCustomcommandItem]  # List of custom commands to be pushed to all FortiS
    fips_enforce: Literal["disable", "enable"]  # Enable/disable enforcement of FIPS on managed Fort | Default: enable
    firmware_provision_on_authorization: Literal["enable", "disable"]  # Enable/disable automatic provisioning of latest fi | Default: disable
    switch_on_deauth: Literal["no-op", "factory-reset"]  # No-operation/Factory-reset the managed FortiSwitch | Default: no-op
    firewall_auth_user_hold_period: int  # Time period in minutes to hold firewall authentica | Default: 5 | Min: 5 | Max: 1440


@final
class GlobalObject:
    """Typed FortiObject for switch_controller/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Time after which an inactive MAC is aged out | Default: 300 | Min: 10 | Max: 1000000
    mac_aging_interval: int
    # Enable/disable image push to FortiSwitch using HTTPS. | Default: enable
    https_image_push: Literal["enable", "disable"]
    # VLAN configuration mode, user-defined-vlans or all-possible- | Default: defined
    vlan_all_mode: Literal["all", "defined"]
    # FortiLink VLAN optimization. | Default: configured
    vlan_optimization: Literal["prune", "configured", "none"]
    # Identity of the VLAN. Commonly used for RADIUS Tunnel-Privat | Default: name
    vlan_identity: Literal["description", "name"]
    # Prevent this FortiSwitch from discovering.
    disable_discovery: list[GlobalDisablediscoveryObject]
    # Time in hours after which an inactive MAC is removed from cl | Default: 24 | Min: 0 | Max: 168
    mac_retention_period: int
    # Default VLAN for ports when added to the virtual-switch. | MaxLen: 15
    default_virtual_switch_vlan: str
    # Enable/disable DHCP snooping server access list. | Default: disable
    dhcp_server_access_list: Literal["enable", "disable"]
    # DHCP option-82 format string. | Default: ascii
    dhcp_option82_format: Literal["ascii", "legacy"]
    # List the parameters to be included to inform about client id | Default: intfname vlan mode
    dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"]
    # List the parameters to be included to inform about client id | Default: mac
    dhcp_option82_remote_id: Literal["mac", "hostname", "ip"]
    # Client DHCP packet broadcast mode. | Default: drop-untrusted
    dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"]
    # Expiry time for DHCP snooping server database entries | Default: 86400 | Min: 300 | Max: 259200
    dhcp_snoop_client_db_exp: int
    # Per Interface dhcp-server entries learn limit | Default: 64 | Min: 0 | Max: 2048
    dhcp_snoop_db_per_port_learn_limit: int
    # Enable/disable logs for Learning Limit Violations. | Default: disable
    log_mac_limit_violations: Literal["enable", "disable"]
    # Set timeout for Learning Limit Violations (0 = disabled). | Default: 0 | Min: 0 | Max: 4294967295
    mac_violation_timer: int
    # Enable/disable DNS resolution of the FortiSwitch unit's IP a | Default: enable
    sn_dns_resolution: Literal["enable", "disable"]
    # Enable/disable MAC address event logging. | Default: disable
    mac_event_logging: Literal["enable", "disable"]
    # Enable/disable bouncing | Default: disable
    bounce_quarantined_link: Literal["disable", "enable"]
    # Quarantine mode. | Default: by-vlan
    quarantine_mode: Literal["by-vlan", "by-redirect"]
    # Control which sources update the device user list. | Default: mac-cache lldp dhcp-snooping l2-db l3-db
    update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]
    # List of custom commands to be pushed to all FortiSwitches in
    custom_command: list[GlobalCustomcommandObject]
    # Enable/disable enforcement of FIPS on managed FortiSwitch de | Default: enable
    fips_enforce: Literal["disable", "enable"]
    # Enable/disable automatic provisioning of latest firmware on | Default: disable
    firmware_provision_on_authorization: Literal["enable", "disable"]
    # No-operation/Factory-reset the managed FortiSwitch on deauth | Default: no-op
    switch_on_deauth: Literal["no-op", "factory-reset"]
    # Time period in minutes to hold firewall authenticated MAC us | Default: 5 | Min: 5 | Max: 1440
    firewall_auth_user_hold_period: int
    
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
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure FortiSwitch global settings.
    
    Path: switch_controller/global_
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalResponse",
    "GlobalObject",
]