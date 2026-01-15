from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/fortianalyzer3/setting payload fields.
    
    Global FortiAnalyzer settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: server-cert-ca)
        - :class:`~.certificate.local.LocalEndpoint` (via: certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: server-cert-ca)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable logging to FortiAnalyzer. | Default: disable
    ips_archive: Literal["enable", "disable"]  # Enable/disable IPS packet archive logging. | Default: enable
    server: str  # The remote FortiAnalyzer. | MaxLen: 127
    alt_server: str  # Alternate FortiAnalyzer. | MaxLen: 127
    fallback_to_primary: Literal["enable", "disable"]  # Enable/disable this FortiGate unit to fallback to | Default: enable
    certificate_verification: Literal["enable", "disable"]  # Enable/disable identity verification of FortiAnaly | Default: enable
    serial: list[dict[str, Any]]  # Serial numbers of the FortiAnalyzer.
    server_cert_ca: str  # Mandatory CA on FortiGate in certificate chain of | MaxLen: 79
    preshared_key: str  # Preshared-key used for auto-authorization on Forti | MaxLen: 63
    access_config: Literal["enable", "disable"]  # Enable/disable FortiAnalyzer access to configurati | Default: enable
    hmac_algorithm: Literal["sha256"]  # OFTP login hash algorithm. | Default: sha256
    enc_algorithm: Literal["high-medium", "high", "low"]  # Configure the level of SSL protection for secure c | Default: high
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    conn_timeout: int  # FortiAnalyzer connection time-out in seconds | Default: 10 | Min: 1 | Max: 3600
    monitor_keepalive_period: int  # Time between OFTP keepalives in seconds | Default: 5 | Min: 1 | Max: 120
    monitor_failure_retry_period: int  # Time between FortiAnalyzer connection retries in s | Default: 5 | Min: 1 | Max: 86400
    certificate: str  # Certificate used to communicate with FortiAnalyzer | MaxLen: 35
    source_ip: str  # Source IPv4 or IPv6 address used to communicate wi | MaxLen: 63
    upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"]  # Enable/disable logging to hard disk and then uploa | Default: 5-minute
    upload_interval: Literal["daily", "weekly", "monthly"]  # Frequency to upload log files to FortiAnalyzer. | Default: daily
    upload_day: str  # Day of week (month) to upload logs.
    upload_time: str  # Time to upload logs (hh:mm).
    reliable: Literal["enable", "disable"]  # Enable/disable reliable logging to FortiAnalyzer. | Default: disable
    priority: Literal["default", "low"]  # Set log transmission priority. | Default: default
    max_log_rate: int  # FortiAnalyzer maximum log rate in MBps | Default: 0 | Min: 0 | Max: 100000
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

class SettingSerialItem(TypedDict):
    """Type hints for serial table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Serial Number. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SettingSerialObject:
    """Typed object for serial table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial Number. | MaxLen: 79
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
class SettingResponse(TypedDict):
    """
    Type hints for log/fortianalyzer3/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable logging to FortiAnalyzer. | Default: disable
    ips_archive: Literal["enable", "disable"]  # Enable/disable IPS packet archive logging. | Default: enable
    server: str  # The remote FortiAnalyzer. | MaxLen: 127
    alt_server: str  # Alternate FortiAnalyzer. | MaxLen: 127
    fallback_to_primary: Literal["enable", "disable"]  # Enable/disable this FortiGate unit to fallback to | Default: enable
    certificate_verification: Literal["enable", "disable"]  # Enable/disable identity verification of FortiAnaly | Default: enable
    serial: list[SettingSerialItem]  # Serial numbers of the FortiAnalyzer.
    server_cert_ca: str  # Mandatory CA on FortiGate in certificate chain of | MaxLen: 79
    preshared_key: str  # Preshared-key used for auto-authorization on Forti | MaxLen: 63
    access_config: Literal["enable", "disable"]  # Enable/disable FortiAnalyzer access to configurati | Default: enable
    hmac_algorithm: Literal["sha256"]  # OFTP login hash algorithm. | Default: sha256
    enc_algorithm: Literal["high-medium", "high", "low"]  # Configure the level of SSL protection for secure c | Default: high
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    conn_timeout: int  # FortiAnalyzer connection time-out in seconds | Default: 10 | Min: 1 | Max: 3600
    monitor_keepalive_period: int  # Time between OFTP keepalives in seconds | Default: 5 | Min: 1 | Max: 120
    monitor_failure_retry_period: int  # Time between FortiAnalyzer connection retries in s | Default: 5 | Min: 1 | Max: 86400
    certificate: str  # Certificate used to communicate with FortiAnalyzer | MaxLen: 35
    source_ip: str  # Source IPv4 or IPv6 address used to communicate wi | MaxLen: 63
    upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"]  # Enable/disable logging to hard disk and then uploa | Default: 5-minute
    upload_interval: Literal["daily", "weekly", "monthly"]  # Frequency to upload log files to FortiAnalyzer. | Default: daily
    upload_day: str  # Day of week (month) to upload logs.
    upload_time: str  # Time to upload logs (hh:mm).
    reliable: Literal["enable", "disable"]  # Enable/disable reliable logging to FortiAnalyzer. | Default: disable
    priority: Literal["default", "low"]  # Set log transmission priority. | Default: default
    max_log_rate: int  # FortiAnalyzer maximum log rate in MBps | Default: 0 | Min: 0 | Max: 100000
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class SettingObject:
    """Typed FortiObject for log/fortianalyzer3/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable logging to FortiAnalyzer. | Default: disable
    status: Literal["enable", "disable"]
    # Enable/disable IPS packet archive logging. | Default: enable
    ips_archive: Literal["enable", "disable"]
    # The remote FortiAnalyzer. | MaxLen: 127
    server: str
    # Alternate FortiAnalyzer. | MaxLen: 127
    alt_server: str
    # Enable/disable this FortiGate unit to fallback to the primar | Default: enable
    fallback_to_primary: Literal["enable", "disable"]
    # Enable/disable identity verification of FortiAnalyzer by use | Default: enable
    certificate_verification: Literal["enable", "disable"]
    # Serial numbers of the FortiAnalyzer.
    serial: list[SettingSerialObject]
    # Mandatory CA on FortiGate in certificate chain of server. | MaxLen: 79
    server_cert_ca: str
    # Preshared-key used for auto-authorization on FortiAnalyzer. | MaxLen: 63
    preshared_key: str
    # Enable/disable FortiAnalyzer access to configuration and dat | Default: enable
    access_config: Literal["enable", "disable"]
    # OFTP login hash algorithm. | Default: sha256
    hmac_algorithm: Literal["sha256"]
    # Configure the level of SSL protection for secure communicati | Default: high
    enc_algorithm: Literal["high-medium", "high", "low"]
    # Minimum supported protocol version for SSL/TLS connections | Default: default
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # FortiAnalyzer connection time-out in seconds | Default: 10 | Min: 1 | Max: 3600
    conn_timeout: int
    # Time between OFTP keepalives in seconds | Default: 5 | Min: 1 | Max: 120
    monitor_keepalive_period: int
    # Time between FortiAnalyzer connection retries in seconds | Default: 5 | Min: 1 | Max: 86400
    monitor_failure_retry_period: int
    # Certificate used to communicate with FortiAnalyzer. | MaxLen: 35
    certificate: str
    # Source IPv4 or IPv6 address used to communicate with FortiAn | MaxLen: 63
    source_ip: str
    # Enable/disable logging to hard disk and then uploading to Fo | Default: 5-minute
    upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"]
    # Frequency to upload log files to FortiAnalyzer. | Default: daily
    upload_interval: Literal["daily", "weekly", "monthly"]
    # Day of week (month) to upload logs.
    upload_day: str
    # Time to upload logs (hh:mm).
    upload_time: str
    # Enable/disable reliable logging to FortiAnalyzer. | Default: disable
    reliable: Literal["enable", "disable"]
    # Set log transmission priority. | Default: default
    priority: Literal["default", "low"]
    # FortiAnalyzer maximum log rate in MBps (0 = unlimited). | Default: 0 | Min: 0 | Max: 100000
    max_log_rate: int
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
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    Global FortiAnalyzer settings.
    
    Path: log/fortianalyzer3/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]