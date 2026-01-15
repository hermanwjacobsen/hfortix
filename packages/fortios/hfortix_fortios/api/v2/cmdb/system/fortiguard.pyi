from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/fortiguard payload fields.
    
    Configure FortiGuard services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: FortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    fortiguard_anycast: Literal["enable", "disable"]  # Enable/disable use of FortiGuard's Anycast network | Default: enable
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"]  # Configure which of Fortinet's servers to provide F | Default: fortinet
    protocol: Literal["udp", "http", "https"]  # Protocol used to communicate with the FortiGuard s | Default: https
    port: Literal["8888", "53", "80", "443"]  # Port used to communicate with the FortiGuard serve | Default: 443
    load_balance_servers: int  # Number of servers to alternate between as first Fo | Default: 1 | Min: 1 | Max: 266
    auto_join_forticloud: Literal["enable", "disable"]  # Automatically connect to and login to FortiCloud. | Default: enable
    update_server_location: Literal["automatic", "usa", "eu"]  # Location from which to receive FortiGuard updates. | Default: automatic
    sandbox_region: str  # FortiCloud Sandbox region. | MaxLen: 63
    sandbox_inline_scan: Literal["enable", "disable"]  # Enable/disable FortiCloud Sandbox inline-scan. | Default: disable
    update_ffdb: Literal["enable", "disable"]  # Enable/disable Internet Service Database update. | Default: enable
    update_uwdb: Literal["enable", "disable"]  # Enable/disable allowlist update. | Default: enable
    update_dldb: Literal["enable", "disable"]  # Enable/disable DLP signature update. | Default: enable
    update_extdb: Literal["enable", "disable"]  # Enable/disable external resource update. | Default: enable
    update_build_proxy: Literal["enable", "disable"]  # Enable/disable proxy dictionary rebuild. | Default: enable
    persistent_connection: Literal["enable", "disable"]  # Enable/disable use of persistent connection to rec | Default: disable
    vdom: str  # FortiGuard Service virtual domain name. | MaxLen: 31
    auto_firmware_upgrade: Literal["enable", "disable"]  # Enable/disable automatic patch-level firmware upgr | Default: enable
    auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Allowed day(s) of the week to install an automatic
    auto_firmware_upgrade_delay: int  # Delay of day(s) before installing an automatic pat | Default: 3 | Min: 0 | Max: 14
    auto_firmware_upgrade_start_hour: int  # Start time in the designated time window for autom | Default: 1 | Min: 0 | Max: 23
    auto_firmware_upgrade_end_hour: int  # End time in the designated time window for automat | Default: 4 | Min: 0 | Max: 23
    FDS_license_expiring_days: int  # Threshold for number of days before FortiGuard lic | Default: 15 | Min: 1 | Max: 100
    subscribe_update_notification: Literal["enable", "disable"]  # Enable/disable subscription to receive update noti | Default: disable
    antispam_force_off: Literal["enable", "disable"]  # Enable/disable turning off the FortiGuard antispam | Default: disable
    antispam_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard antispam request caching | Default: enable
    antispam_cache_ttl: int  # Time-to-live for antispam cache entries in seconds | Default: 1800 | Min: 300 | Max: 86400
    antispam_cache_mpermille: int  # Maximum permille of FortiGate memory the antispam | Default: 1 | Min: 1 | Max: 150
    antispam_license: int  # Interval of time between license checks for the Fo | Default: 4294967295 | Min: 0 | Max: 4294967295
    antispam_expiration: int  # Expiration date of the FortiGuard antispam contrac | Default: 0 | Min: 0 | Max: 4294967295
    antispam_timeout: int  # Antispam query time out (1 - 30 sec, default = 7). | Default: 7 | Min: 1 | Max: 30
    outbreak_prevention_force_off: Literal["enable", "disable"]  # Turn off FortiGuard Virus Outbreak Prevention serv | Default: disable
    outbreak_prevention_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard Virus Outbreak Preventio | Default: enable
    outbreak_prevention_cache_ttl: int  # Time-to-live for FortiGuard Virus Outbreak Prevent | Default: 300 | Min: 300 | Max: 86400
    outbreak_prevention_cache_mpermille: int  # Maximum permille of memory FortiGuard Virus Outbre | Default: 1 | Min: 1 | Max: 150
    outbreak_prevention_license: int  # Interval of time between license checks for FortiG | Default: 4294967295 | Min: 0 | Max: 4294967295
    outbreak_prevention_expiration: int  # Expiration date of FortiGuard Virus Outbreak Preve | Default: 0 | Min: 0 | Max: 4294967295
    outbreak_prevention_timeout: int  # FortiGuard Virus Outbreak Prevention time out | Default: 7 | Min: 1 | Max: 30
    webfilter_force_off: Literal["enable", "disable"]  # Enable/disable turning off the FortiGuard web filt | Default: disable
    webfilter_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard web filter caching. | Default: enable
    webfilter_cache_ttl: int  # Time-to-live for web filter cache entries in secon | Default: 3600 | Min: 300 | Max: 86400
    webfilter_license: int  # Interval of time between license checks for the Fo | Default: 4294967295 | Min: 0 | Max: 4294967295
    webfilter_expiration: int  # Expiration date of the FortiGuard web filter contr | Default: 0 | Min: 0 | Max: 4294967295
    webfilter_timeout: int  # Web filter query time out | Default: 15 | Min: 1 | Max: 30
    sdns_server_ip: list[dict[str, Any]]  # IP address of the FortiGuard DNS rating server.
    sdns_server_port: int  # Port to connect to on the FortiGuard DNS rating se | Default: 53 | Min: 1 | Max: 65535
    anycast_sdns_server_ip: str  # IP address of the FortiGuard anycast DNS rating se | Default: 0.0.0.0
    anycast_sdns_server_port: int  # Port to connect to on the FortiGuard anycast DNS r | Default: 853 | Min: 1 | Max: 65535
    sdns_options: Literal["include-question-section"]  # Customization options for the FortiGuard DNS servi
    source_ip: str  # Source IPv4 address used to communicate with Forti | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used to communicate with Forti | Default: ::
    proxy_server_ip: str  # Hostname or IPv4 address of the proxy server. | MaxLen: 63
    proxy_server_port: int  # Port used to communicate with the proxy server. | Default: 0 | Min: 0 | Max: 65535
    proxy_username: str  # Proxy user name. | MaxLen: 64
    proxy_password: str  # Proxy user password. | MaxLen: 128
    ddns_server_ip: str  # IP address of the FortiDDNS server. | Default: 0.0.0.0
    ddns_server_ip6: str  # IPv6 address of the FortiDDNS server. | Default: ::
    ddns_server_port: int  # Port used to communicate with FortiDDNS servers. | Default: 443 | Min: 1 | Max: 65535
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FortiguardResponse(TypedDict):
    """
    Type hints for system/fortiguard API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    fortiguard_anycast: Literal["enable", "disable"]  # Enable/disable use of FortiGuard's Anycast network | Default: enable
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"]  # Configure which of Fortinet's servers to provide F | Default: fortinet
    protocol: Literal["udp", "http", "https"]  # Protocol used to communicate with the FortiGuard s | Default: https
    port: Literal["8888", "53", "80", "443"]  # Port used to communicate with the FortiGuard serve | Default: 443
    load_balance_servers: int  # Number of servers to alternate between as first Fo | Default: 1 | Min: 1 | Max: 266
    auto_join_forticloud: Literal["enable", "disable"]  # Automatically connect to and login to FortiCloud. | Default: enable
    update_server_location: Literal["automatic", "usa", "eu"]  # Location from which to receive FortiGuard updates. | Default: automatic
    sandbox_region: str  # FortiCloud Sandbox region. | MaxLen: 63
    sandbox_inline_scan: Literal["enable", "disable"]  # Enable/disable FortiCloud Sandbox inline-scan. | Default: disable
    update_ffdb: Literal["enable", "disable"]  # Enable/disable Internet Service Database update. | Default: enable
    update_uwdb: Literal["enable", "disable"]  # Enable/disable allowlist update. | Default: enable
    update_dldb: Literal["enable", "disable"]  # Enable/disable DLP signature update. | Default: enable
    update_extdb: Literal["enable", "disable"]  # Enable/disable external resource update. | Default: enable
    update_build_proxy: Literal["enable", "disable"]  # Enable/disable proxy dictionary rebuild. | Default: enable
    persistent_connection: Literal["enable", "disable"]  # Enable/disable use of persistent connection to rec | Default: disable
    vdom: str  # FortiGuard Service virtual domain name. | MaxLen: 31
    auto_firmware_upgrade: Literal["enable", "disable"]  # Enable/disable automatic patch-level firmware upgr | Default: enable
    auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Allowed day(s) of the week to install an automatic
    auto_firmware_upgrade_delay: int  # Delay of day(s) before installing an automatic pat | Default: 3 | Min: 0 | Max: 14
    auto_firmware_upgrade_start_hour: int  # Start time in the designated time window for autom | Default: 1 | Min: 0 | Max: 23
    auto_firmware_upgrade_end_hour: int  # End time in the designated time window for automat | Default: 4 | Min: 0 | Max: 23
    FDS_license_expiring_days: int  # Threshold for number of days before FortiGuard lic | Default: 15 | Min: 1 | Max: 100
    subscribe_update_notification: Literal["enable", "disable"]  # Enable/disable subscription to receive update noti | Default: disable
    antispam_force_off: Literal["enable", "disable"]  # Enable/disable turning off the FortiGuard antispam | Default: disable
    antispam_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard antispam request caching | Default: enable
    antispam_cache_ttl: int  # Time-to-live for antispam cache entries in seconds | Default: 1800 | Min: 300 | Max: 86400
    antispam_cache_mpermille: int  # Maximum permille of FortiGate memory the antispam | Default: 1 | Min: 1 | Max: 150
    antispam_license: int  # Interval of time between license checks for the Fo | Default: 4294967295 | Min: 0 | Max: 4294967295
    antispam_expiration: int  # Expiration date of the FortiGuard antispam contrac | Default: 0 | Min: 0 | Max: 4294967295
    antispam_timeout: int  # Antispam query time out (1 - 30 sec, default = 7). | Default: 7 | Min: 1 | Max: 30
    outbreak_prevention_force_off: Literal["enable", "disable"]  # Turn off FortiGuard Virus Outbreak Prevention serv | Default: disable
    outbreak_prevention_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard Virus Outbreak Preventio | Default: enable
    outbreak_prevention_cache_ttl: int  # Time-to-live for FortiGuard Virus Outbreak Prevent | Default: 300 | Min: 300 | Max: 86400
    outbreak_prevention_cache_mpermille: int  # Maximum permille of memory FortiGuard Virus Outbre | Default: 1 | Min: 1 | Max: 150
    outbreak_prevention_license: int  # Interval of time between license checks for FortiG | Default: 4294967295 | Min: 0 | Max: 4294967295
    outbreak_prevention_expiration: int  # Expiration date of FortiGuard Virus Outbreak Preve | Default: 0 | Min: 0 | Max: 4294967295
    outbreak_prevention_timeout: int  # FortiGuard Virus Outbreak Prevention time out | Default: 7 | Min: 1 | Max: 30
    webfilter_force_off: Literal["enable", "disable"]  # Enable/disable turning off the FortiGuard web filt | Default: disable
    webfilter_cache: Literal["enable", "disable"]  # Enable/disable FortiGuard web filter caching. | Default: enable
    webfilter_cache_ttl: int  # Time-to-live for web filter cache entries in secon | Default: 3600 | Min: 300 | Max: 86400
    webfilter_license: int  # Interval of time between license checks for the Fo | Default: 4294967295 | Min: 0 | Max: 4294967295
    webfilter_expiration: int  # Expiration date of the FortiGuard web filter contr | Default: 0 | Min: 0 | Max: 4294967295
    webfilter_timeout: int  # Web filter query time out | Default: 15 | Min: 1 | Max: 30
    sdns_server_ip: list[dict[str, Any]]  # IP address of the FortiGuard DNS rating server.
    sdns_server_port: int  # Port to connect to on the FortiGuard DNS rating se | Default: 53 | Min: 1 | Max: 65535
    anycast_sdns_server_ip: str  # IP address of the FortiGuard anycast DNS rating se | Default: 0.0.0.0
    anycast_sdns_server_port: int  # Port to connect to on the FortiGuard anycast DNS r | Default: 853 | Min: 1 | Max: 65535
    sdns_options: Literal["include-question-section"]  # Customization options for the FortiGuard DNS servi
    source_ip: str  # Source IPv4 address used to communicate with Forti | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used to communicate with Forti | Default: ::
    proxy_server_ip: str  # Hostname or IPv4 address of the proxy server. | MaxLen: 63
    proxy_server_port: int  # Port used to communicate with the proxy server. | Default: 0 | Min: 0 | Max: 65535
    proxy_username: str  # Proxy user name. | MaxLen: 64
    proxy_password: str  # Proxy user password. | MaxLen: 128
    ddns_server_ip: str  # IP address of the FortiDDNS server. | Default: 0.0.0.0
    ddns_server_ip6: str  # IPv6 address of the FortiDDNS server. | Default: ::
    ddns_server_port: int  # Port used to communicate with FortiDDNS servers. | Default: 443 | Min: 1 | Max: 65535
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class FortiguardObject:
    """Typed FortiObject for system/fortiguard with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable use of FortiGuard's Anycast network. | Default: enable
    fortiguard_anycast: Literal["enable", "disable"]
    # Configure which of Fortinet's servers to provide FortiGuard | Default: fortinet
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"]
    # Protocol used to communicate with the FortiGuard servers. | Default: https
    protocol: Literal["udp", "http", "https"]
    # Port used to communicate with the FortiGuard servers. | Default: 443
    port: Literal["8888", "53", "80", "443"]
    # Number of servers to alternate between as first FortiGuard o | Default: 1 | Min: 1 | Max: 266
    load_balance_servers: int
    # Automatically connect to and login to FortiCloud. | Default: enable
    auto_join_forticloud: Literal["enable", "disable"]
    # Location from which to receive FortiGuard updates. | Default: automatic
    update_server_location: Literal["automatic", "usa", "eu"]
    # FortiCloud Sandbox region. | MaxLen: 63
    sandbox_region: str
    # Enable/disable FortiCloud Sandbox inline-scan. | Default: disable
    sandbox_inline_scan: Literal["enable", "disable"]
    # Enable/disable Internet Service Database update. | Default: enable
    update_ffdb: Literal["enable", "disable"]
    # Enable/disable allowlist update. | Default: enable
    update_uwdb: Literal["enable", "disable"]
    # Enable/disable DLP signature update. | Default: enable
    update_dldb: Literal["enable", "disable"]
    # Enable/disable external resource update. | Default: enable
    update_extdb: Literal["enable", "disable"]
    # Enable/disable proxy dictionary rebuild. | Default: enable
    update_build_proxy: Literal["enable", "disable"]
    # Enable/disable use of persistent connection to receive updat | Default: disable
    persistent_connection: Literal["enable", "disable"]
    # FortiGuard Service virtual domain name. | MaxLen: 31
    vdom: str
    # Enable/disable automatic patch-level firmware upgrade from F | Default: enable
    auto_firmware_upgrade: Literal["enable", "disable"]
    # Allowed day(s) of the week to install an automatic patch-lev
    auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Delay of day(s) before installing an automatic patch-level f | Default: 3 | Min: 0 | Max: 14
    auto_firmware_upgrade_delay: int
    # Start time in the designated time window for automatic patch | Default: 1 | Min: 0 | Max: 23
    auto_firmware_upgrade_start_hour: int
    # End time in the designated time window for automatic patch-l | Default: 4 | Min: 0 | Max: 23
    auto_firmware_upgrade_end_hour: int
    # Threshold for number of days before FortiGuard license expir | Default: 15 | Min: 1 | Max: 100
    FDS_license_expiring_days: int
    # Enable/disable subscription to receive update notification f | Default: disable
    subscribe_update_notification: Literal["enable", "disable"]
    # Enable/disable turning off the FortiGuard antispam service. | Default: disable
    antispam_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard antispam request caching. Uses a s | Default: enable
    antispam_cache: Literal["enable", "disable"]
    # Time-to-live for antispam cache entries in seconds | Default: 1800 | Min: 300 | Max: 86400
    antispam_cache_ttl: int
    # Maximum permille of FortiGate memory the antispam cache is a | Default: 1 | Min: 1 | Max: 150
    antispam_cache_mpermille: int
    # Interval of time between license checks for the FortiGuard a | Default: 4294967295 | Min: 0 | Max: 4294967295
    antispam_license: int
    # Expiration date of the FortiGuard antispam contract. | Default: 0 | Min: 0 | Max: 4294967295
    antispam_expiration: int
    # Antispam query time out (1 - 30 sec, default = 7). | Default: 7 | Min: 1 | Max: 30
    antispam_timeout: int
    # Turn off FortiGuard Virus Outbreak Prevention service. | Default: disable
    outbreak_prevention_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard Virus Outbreak Prevention cache. | Default: enable
    outbreak_prevention_cache: Literal["enable", "disable"]
    # Time-to-live for FortiGuard Virus Outbreak Prevention cache | Default: 300 | Min: 300 | Max: 86400
    outbreak_prevention_cache_ttl: int
    # Maximum permille of memory FortiGuard Virus Outbreak Prevent | Default: 1 | Min: 1 | Max: 150
    outbreak_prevention_cache_mpermille: int
    # Interval of time between license checks for FortiGuard Virus | Default: 4294967295 | Min: 0 | Max: 4294967295
    outbreak_prevention_license: int
    # Expiration date of FortiGuard Virus Outbreak Prevention cont | Default: 0 | Min: 0 | Max: 4294967295
    outbreak_prevention_expiration: int
    # FortiGuard Virus Outbreak Prevention time out | Default: 7 | Min: 1 | Max: 30
    outbreak_prevention_timeout: int
    # Enable/disable turning off the FortiGuard web filtering serv | Default: disable
    webfilter_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard web filter caching. | Default: enable
    webfilter_cache: Literal["enable", "disable"]
    # Time-to-live for web filter cache entries in seconds | Default: 3600 | Min: 300 | Max: 86400
    webfilter_cache_ttl: int
    # Interval of time between license checks for the FortiGuard w | Default: 4294967295 | Min: 0 | Max: 4294967295
    webfilter_license: int
    # Expiration date of the FortiGuard web filter contract. | Default: 0 | Min: 0 | Max: 4294967295
    webfilter_expiration: int
    # Web filter query time out (1 - 30 sec, default = 15). | Default: 15 | Min: 1 | Max: 30
    webfilter_timeout: int
    # IP address of the FortiGuard DNS rating server.
    sdns_server_ip: list[dict[str, Any]]
    # Port to connect to on the FortiGuard DNS rating server. | Default: 53 | Min: 1 | Max: 65535
    sdns_server_port: int
    # IP address of the FortiGuard anycast DNS rating server. | Default: 0.0.0.0
    anycast_sdns_server_ip: str
    # Port to connect to on the FortiGuard anycast DNS rating serv | Default: 853 | Min: 1 | Max: 65535
    anycast_sdns_server_port: int
    # Customization options for the FortiGuard DNS service.
    sdns_options: Literal["include-question-section"]
    # Source IPv4 address used to communicate with FortiGuard. | Default: 0.0.0.0
    source_ip: str
    # Source IPv6 address used to communicate with FortiGuard. | Default: ::
    source_ip6: str
    # Hostname or IPv4 address of the proxy server. | MaxLen: 63
    proxy_server_ip: str
    # Port used to communicate with the proxy server. | Default: 0 | Min: 0 | Max: 65535
    proxy_server_port: int
    # Proxy user name. | MaxLen: 64
    proxy_username: str
    # Proxy user password. | MaxLen: 128
    proxy_password: str
    # IP address of the FortiDDNS server. | Default: 0.0.0.0
    ddns_server_ip: str
    # IPv6 address of the FortiDDNS server. | Default: ::
    ddns_server_ip6: str
    # Port used to communicate with FortiDDNS servers. | Default: 443 | Min: 1 | Max: 65535
    ddns_server_port: int
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
    def to_dict(self) -> FortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fortiguard:
    """
    Configure FortiGuard services.
    
    Path: system/fortiguard
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiguardObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "Fortiguard",
    "FortiguardPayload",
    "FortiguardResponse",
    "FortiguardObject",
]