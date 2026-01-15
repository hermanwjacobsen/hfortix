from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/disk/setting payload fields.
    
    Settings for local disk logging.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable local disk logging. | Default: enable
    ips_archive: Literal["enable", "disable"]  # Enable/disable IPS packet archiving to the local d | Default: enable
    max_log_file_size: int  # Maximum log file size before rolling | Default: 20 | Min: 1 | Max: 100
    max_policy_packet_capture_size: int  # Maximum size of policy sniffer in MB | Default: 100 | Min: 0 | Max: 4294967295
    roll_schedule: Literal["daily", "weekly"]  # Frequency to check log file for rolling. | Default: daily
    roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week on which to roll log file. | Default: sunday
    roll_time: str  # Time of day to roll the log file (hh:mm).
    diskfull: Literal["overwrite", "nolog"]  # Action to take when disk is full. The system can o | Default: overwrite
    log_quota: int  # Disk log quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    dlp_archive_quota: int  # DLP archive quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    report_quota: int  # Report db quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    maximum_log_age: int  # Delete log files older than (days). | Default: 7 | Min: 0 | Max: 3650
    upload: Literal["enable", "disable"]  # Enable/disable uploading log files when they are r | Default: disable
    upload_destination: Literal["ftp-server"]  # The type of server to upload log files to. Only FT | Default: ftp-server
    uploadip: str  # IP address of the FTP server to upload log files t | Default: 0.0.0.0
    uploadport: int  # TCP port to use for communicating with the FTP ser | Default: 21 | Min: 0 | Max: 65535
    source_ip: str  # Source IP address to use for uploading disk log fi | Default: 0.0.0.0
    uploaduser: str  # Username required to log into the FTP server to up | MaxLen: 35
    uploadpass: str  # Password required to log into the FTP server to up | MaxLen: 128
    uploaddir: str  # The remote directory on the FTP server to upload l | MaxLen: 63
    uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]  # Types of log files to upload. Separate multiple en | Default: traffic event virus webfilter IPS emailfilter dlp-archive anomaly voip dlp app-ctrl waf gtp dns ssh ssl
    uploadsched: Literal["disable", "enable"]  # Set the schedule for uploading log files to the FT | Default: disable
    uploadtime: str  # Time of day at which log files are uploaded if upl
    upload_delete_files: Literal["enable", "disable"]  # Delete log files after uploading | Default: enable
    upload_ssl_conn: Literal["default", "high", "low", "disable"]  # Enable/disable encrypted FTPS communication to upl | Default: default
    full_first_warning_threshold: int  # Log full first warning threshold as a percent | Default: 75 | Min: 1 | Max: 98
    full_second_warning_threshold: int  # Log full second warning threshold as a percent | Default: 90 | Min: 2 | Max: 99
    full_final_warning_threshold: int  # Log full final warning threshold as a percent | Default: 95 | Min: 3 | Max: 100
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for log/disk/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable local disk logging. | Default: enable
    ips_archive: Literal["enable", "disable"]  # Enable/disable IPS packet archiving to the local d | Default: enable
    max_log_file_size: int  # Maximum log file size before rolling | Default: 20 | Min: 1 | Max: 100
    max_policy_packet_capture_size: int  # Maximum size of policy sniffer in MB | Default: 100 | Min: 0 | Max: 4294967295
    roll_schedule: Literal["daily", "weekly"]  # Frequency to check log file for rolling. | Default: daily
    roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week on which to roll log file. | Default: sunday
    roll_time: str  # Time of day to roll the log file (hh:mm).
    diskfull: Literal["overwrite", "nolog"]  # Action to take when disk is full. The system can o | Default: overwrite
    log_quota: int  # Disk log quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    dlp_archive_quota: int  # DLP archive quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    report_quota: int  # Report db quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    maximum_log_age: int  # Delete log files older than (days). | Default: 7 | Min: 0 | Max: 3650
    upload: Literal["enable", "disable"]  # Enable/disable uploading log files when they are r | Default: disable
    upload_destination: Literal["ftp-server"]  # The type of server to upload log files to. Only FT | Default: ftp-server
    uploadip: str  # IP address of the FTP server to upload log files t | Default: 0.0.0.0
    uploadport: int  # TCP port to use for communicating with the FTP ser | Default: 21 | Min: 0 | Max: 65535
    source_ip: str  # Source IP address to use for uploading disk log fi | Default: 0.0.0.0
    uploaduser: str  # Username required to log into the FTP server to up | MaxLen: 35
    uploadpass: str  # Password required to log into the FTP server to up | MaxLen: 128
    uploaddir: str  # The remote directory on the FTP server to upload l | MaxLen: 63
    uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]  # Types of log files to upload. Separate multiple en | Default: traffic event virus webfilter IPS emailfilter dlp-archive anomaly voip dlp app-ctrl waf gtp dns ssh ssl
    uploadsched: Literal["disable", "enable"]  # Set the schedule for uploading log files to the FT | Default: disable
    uploadtime: str  # Time of day at which log files are uploaded if upl
    upload_delete_files: Literal["enable", "disable"]  # Delete log files after uploading | Default: enable
    upload_ssl_conn: Literal["default", "high", "low", "disable"]  # Enable/disable encrypted FTPS communication to upl | Default: default
    full_first_warning_threshold: int  # Log full first warning threshold as a percent | Default: 75 | Min: 1 | Max: 98
    full_second_warning_threshold: int  # Log full second warning threshold as a percent | Default: 90 | Min: 2 | Max: 99
    full_final_warning_threshold: int  # Log full final warning threshold as a percent | Default: 95 | Min: 3 | Max: 100
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class SettingObject:
    """Typed FortiObject for log/disk/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable local disk logging. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable IPS packet archiving to the local disk. | Default: enable
    ips_archive: Literal["enable", "disable"]
    # Maximum log file size before rolling (1 - 100 Mbytes). | Default: 20 | Min: 1 | Max: 100
    max_log_file_size: int
    # Maximum size of policy sniffer in MB (0 means unlimited). | Default: 100 | Min: 0 | Max: 4294967295
    max_policy_packet_capture_size: int
    # Frequency to check log file for rolling. | Default: daily
    roll_schedule: Literal["daily", "weekly"]
    # Day of week on which to roll log file. | Default: sunday
    roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Time of day to roll the log file (hh:mm).
    roll_time: str
    # Action to take when disk is full. The system can overwrite t | Default: overwrite
    diskfull: Literal["overwrite", "nolog"]
    # Disk log quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    log_quota: int
    # DLP archive quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    dlp_archive_quota: int
    # Report db quota (MB). | Default: 0 | Min: 0 | Max: 4294967295
    report_quota: int
    # Delete log files older than (days). | Default: 7 | Min: 0 | Max: 3650
    maximum_log_age: int
    # Enable/disable uploading log files when they are rolled. | Default: disable
    upload: Literal["enable", "disable"]
    # The type of server to upload log files to. Only FTP is curre | Default: ftp-server
    upload_destination: Literal["ftp-server"]
    # IP address of the FTP server to upload log files to. | Default: 0.0.0.0
    uploadip: str
    # TCP port to use for communicating with the FTP server | Default: 21 | Min: 0 | Max: 65535
    uploadport: int
    # Source IP address to use for uploading disk log files. | Default: 0.0.0.0
    source_ip: str
    # Username required to log into the FTP server to upload disk | MaxLen: 35
    uploaduser: str
    # Password required to log into the FTP server to upload disk | MaxLen: 128
    uploadpass: str
    # The remote directory on the FTP server to upload log files t | MaxLen: 63
    uploaddir: str
    # Types of log files to upload. Separate multiple entries with | Default: traffic event virus webfilter IPS emailfilter dlp-archive anomaly voip dlp app-ctrl waf gtp dns ssh ssl
    uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]
    # Set the schedule for uploading log files to the FTP server | Default: disable
    uploadsched: Literal["disable", "enable"]
    # Time of day at which log files are uploaded if uploadsched i
    uploadtime: str
    # Delete log files after uploading (default = enable). | Default: enable
    upload_delete_files: Literal["enable", "disable"]
    # Enable/disable encrypted FTPS communication to upload log fi | Default: default
    upload_ssl_conn: Literal["default", "high", "low", "disable"]
    # Log full first warning threshold as a percent | Default: 75 | Min: 1 | Max: 98
    full_first_warning_threshold: int
    # Log full second warning threshold as a percent | Default: 90 | Min: 2 | Max: 99
    full_second_warning_threshold: int
    # Log full final warning threshold as a percent | Default: 95 | Min: 3 | Max: 100
    full_final_warning_threshold: int
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
    Settings for local disk logging.
    
    Path: log/disk/setting
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
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
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
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
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
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]