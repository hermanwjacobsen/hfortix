from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for alertemail/setting payload fields.
    
    Configure alert email settings.
    
    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    username: str  # Name that appears in the From: field of alert emai | MaxLen: 63
    mailto1: str  # Email address to send alert email to | MaxLen: 63
    mailto2: str  # Optional second email address to send alert email | MaxLen: 63
    mailto3: str  # Optional third email address to send alert email t | MaxLen: 63
    filter_mode: Literal["category", "threshold"]  # How to filter log messages that are sent to alert | Default: category
    email_interval: int  # Interval between sending alert emails | Default: 5 | Min: 1 | Max: 99999
    IPS_logs: Literal["enable", "disable"]  # Enable/disable IPS logs in alert email. | Default: disable
    firewall_authentication_failure_logs: Literal["enable", "disable"]  # Enable/disable firewall authentication failure log | Default: disable
    HA_logs: Literal["enable", "disable"]  # Enable/disable HA logs in alert email. | Default: disable
    IPsec_errors_logs: Literal["enable", "disable"]  # Enable/disable IPsec error logs in alert email. | Default: disable
    FDS_update_logs: Literal["enable", "disable"]  # Enable/disable FortiGuard update logs in alert ema | Default: disable
    PPP_errors_logs: Literal["enable", "disable"]  # Enable/disable PPP error logs in alert email. | Default: disable
    sslvpn_authentication_errors_logs: Literal["enable", "disable"]  # Enable/disable Agentless VPN authentication error | Default: disable
    antivirus_logs: Literal["enable", "disable"]  # Enable/disable antivirus logs in alert email. | Default: disable
    webfilter_logs: Literal["enable", "disable"]  # Enable/disable web filter logs in alert email. | Default: disable
    configuration_changes_logs: Literal["enable", "disable"]  # Enable/disable configuration change logs in alert | Default: disable
    violation_traffic_logs: Literal["enable", "disable"]  # Enable/disable violation traffic logs in alert ema | Default: disable
    admin_login_logs: Literal["enable", "disable"]  # Enable/disable administrator login/logout logs in | Default: disable
    FDS_license_expiring_warning: Literal["enable", "disable"]  # Enable/disable FortiGuard license expiration warni | Default: disable
    log_disk_usage_warning: Literal["enable", "disable"]  # Enable/disable disk usage warnings in alert email. | Default: disable
    fortiguard_log_quota_warning: Literal["enable", "disable"]  # Enable/disable FortiCloud log quota warnings in al | Default: disable
    amc_interface_bypass_mode: Literal["enable", "disable"]  # Enable/disable Fortinet Advanced Mezzanine Card | Default: disable
    FIPS_CC_errors: Literal["enable", "disable"]  # Enable/disable FIPS and Common Criteria error logs | Default: disable
    FSSO_disconnect_logs: Literal["enable", "disable"]  # Enable/disable logging of FSSO collector agent dis | Default: disable
    ssh_logs: Literal["enable", "disable"]  # Enable/disable SSH logs in alert email. | Default: disable
    local_disk_usage: int  # Disk usage percentage at which to send alert email | Default: 75 | Min: 1 | Max: 99
    emergency_interval: int  # Emergency alert interval in minutes. | Default: 1 | Min: 1 | Max: 99999
    alert_interval: int  # Alert alert interval in minutes. | Default: 2 | Min: 1 | Max: 99999
    critical_interval: int  # Critical alert interval in minutes. | Default: 3 | Min: 1 | Max: 99999
    error_interval: int  # Error alert interval in minutes. | Default: 5 | Min: 1 | Max: 99999
    warning_interval: int  # Warning alert interval in minutes. | Default: 10 | Min: 1 | Max: 99999
    notification_interval: int  # Notification alert interval in minutes. | Default: 20 | Min: 1 | Max: 99999
    information_interval: int  # Information alert interval in minutes. | Default: 30 | Min: 1 | Max: 99999
    debug_interval: int  # Debug alert interval in minutes. | Default: 60 | Min: 1 | Max: 99999
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log. | Default: alert

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for alertemail/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    username: str  # Name that appears in the From: field of alert emai | MaxLen: 63
    mailto1: str  # Email address to send alert email to | MaxLen: 63
    mailto2: str  # Optional second email address to send alert email | MaxLen: 63
    mailto3: str  # Optional third email address to send alert email t | MaxLen: 63
    filter_mode: Literal["category", "threshold"]  # How to filter log messages that are sent to alert | Default: category
    email_interval: int  # Interval between sending alert emails | Default: 5 | Min: 1 | Max: 99999
    IPS_logs: Literal["enable", "disable"]  # Enable/disable IPS logs in alert email. | Default: disable
    firewall_authentication_failure_logs: Literal["enable", "disable"]  # Enable/disable firewall authentication failure log | Default: disable
    HA_logs: Literal["enable", "disable"]  # Enable/disable HA logs in alert email. | Default: disable
    IPsec_errors_logs: Literal["enable", "disable"]  # Enable/disable IPsec error logs in alert email. | Default: disable
    FDS_update_logs: Literal["enable", "disable"]  # Enable/disable FortiGuard update logs in alert ema | Default: disable
    PPP_errors_logs: Literal["enable", "disable"]  # Enable/disable PPP error logs in alert email. | Default: disable
    sslvpn_authentication_errors_logs: Literal["enable", "disable"]  # Enable/disable Agentless VPN authentication error | Default: disable
    antivirus_logs: Literal["enable", "disable"]  # Enable/disable antivirus logs in alert email. | Default: disable
    webfilter_logs: Literal["enable", "disable"]  # Enable/disable web filter logs in alert email. | Default: disable
    configuration_changes_logs: Literal["enable", "disable"]  # Enable/disable configuration change logs in alert | Default: disable
    violation_traffic_logs: Literal["enable", "disable"]  # Enable/disable violation traffic logs in alert ema | Default: disable
    admin_login_logs: Literal["enable", "disable"]  # Enable/disable administrator login/logout logs in | Default: disable
    FDS_license_expiring_warning: Literal["enable", "disable"]  # Enable/disable FortiGuard license expiration warni | Default: disable
    log_disk_usage_warning: Literal["enable", "disable"]  # Enable/disable disk usage warnings in alert email. | Default: disable
    fortiguard_log_quota_warning: Literal["enable", "disable"]  # Enable/disable FortiCloud log quota warnings in al | Default: disable
    amc_interface_bypass_mode: Literal["enable", "disable"]  # Enable/disable Fortinet Advanced Mezzanine Card | Default: disable
    FIPS_CC_errors: Literal["enable", "disable"]  # Enable/disable FIPS and Common Criteria error logs | Default: disable
    FSSO_disconnect_logs: Literal["enable", "disable"]  # Enable/disable logging of FSSO collector agent dis | Default: disable
    ssh_logs: Literal["enable", "disable"]  # Enable/disable SSH logs in alert email. | Default: disable
    local_disk_usage: int  # Disk usage percentage at which to send alert email | Default: 75 | Min: 1 | Max: 99
    emergency_interval: int  # Emergency alert interval in minutes. | Default: 1 | Min: 1 | Max: 99999
    alert_interval: int  # Alert alert interval in minutes. | Default: 2 | Min: 1 | Max: 99999
    critical_interval: int  # Critical alert interval in minutes. | Default: 3 | Min: 1 | Max: 99999
    error_interval: int  # Error alert interval in minutes. | Default: 5 | Min: 1 | Max: 99999
    warning_interval: int  # Warning alert interval in minutes. | Default: 10 | Min: 1 | Max: 99999
    notification_interval: int  # Notification alert interval in minutes. | Default: 20 | Min: 1 | Max: 99999
    information_interval: int  # Information alert interval in minutes. | Default: 30 | Min: 1 | Max: 99999
    debug_interval: int  # Debug alert interval in minutes. | Default: 60 | Min: 1 | Max: 99999
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log. | Default: alert


@final
class SettingObject:
    """Typed FortiObject for alertemail/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name that appears in the From: field of alert emails | MaxLen: 63
    username: str
    # Email address to send alert email to | MaxLen: 63
    mailto1: str
    # Optional second email address to send alert email to | MaxLen: 63
    mailto2: str
    # Optional third email address to send alert email to | MaxLen: 63
    mailto3: str
    # How to filter log messages that are sent to alert emails. | Default: category
    filter_mode: Literal["category", "threshold"]
    # Interval between sending alert emails | Default: 5 | Min: 1 | Max: 99999
    email_interval: int
    # Enable/disable IPS logs in alert email. | Default: disable
    IPS_logs: Literal["enable", "disable"]
    # Enable/disable firewall authentication failure logs in alert | Default: disable
    firewall_authentication_failure_logs: Literal["enable", "disable"]
    # Enable/disable HA logs in alert email. | Default: disable
    HA_logs: Literal["enable", "disable"]
    # Enable/disable IPsec error logs in alert email. | Default: disable
    IPsec_errors_logs: Literal["enable", "disable"]
    # Enable/disable FortiGuard update logs in alert email. | Default: disable
    FDS_update_logs: Literal["enable", "disable"]
    # Enable/disable PPP error logs in alert email. | Default: disable
    PPP_errors_logs: Literal["enable", "disable"]
    # Enable/disable Agentless VPN authentication error logs in al | Default: disable
    sslvpn_authentication_errors_logs: Literal["enable", "disable"]
    # Enable/disable antivirus logs in alert email. | Default: disable
    antivirus_logs: Literal["enable", "disable"]
    # Enable/disable web filter logs in alert email. | Default: disable
    webfilter_logs: Literal["enable", "disable"]
    # Enable/disable configuration change logs in alert email. | Default: disable
    configuration_changes_logs: Literal["enable", "disable"]
    # Enable/disable violation traffic logs in alert email. | Default: disable
    violation_traffic_logs: Literal["enable", "disable"]
    # Enable/disable administrator login/logout logs in alert emai | Default: disable
    admin_login_logs: Literal["enable", "disable"]
    # Enable/disable FortiGuard license expiration warnings in ale | Default: disable
    FDS_license_expiring_warning: Literal["enable", "disable"]
    # Enable/disable disk usage warnings in alert email. | Default: disable
    log_disk_usage_warning: Literal["enable", "disable"]
    # Enable/disable FortiCloud log quota warnings in alert email. | Default: disable
    fortiguard_log_quota_warning: Literal["enable", "disable"]
    # Enable/disable Fortinet Advanced Mezzanine Card (AMC) interf | Default: disable
    amc_interface_bypass_mode: Literal["enable", "disable"]
    # Enable/disable FIPS and Common Criteria error logs in alert | Default: disable
    FIPS_CC_errors: Literal["enable", "disable"]
    # Enable/disable logging of FSSO collector agent disconnect. | Default: disable
    FSSO_disconnect_logs: Literal["enable", "disable"]
    # Enable/disable SSH logs in alert email. | Default: disable
    ssh_logs: Literal["enable", "disable"]
    # Disk usage percentage at which to send alert email | Default: 75 | Min: 1 | Max: 99
    local_disk_usage: int
    # Emergency alert interval in minutes. | Default: 1 | Min: 1 | Max: 99999
    emergency_interval: int
    # Alert alert interval in minutes. | Default: 2 | Min: 1 | Max: 99999
    alert_interval: int
    # Critical alert interval in minutes. | Default: 3 | Min: 1 | Max: 99999
    critical_interval: int
    # Error alert interval in minutes. | Default: 5 | Min: 1 | Max: 99999
    error_interval: int
    # Warning alert interval in minutes. | Default: 10 | Min: 1 | Max: 99999
    warning_interval: int
    # Notification alert interval in minutes. | Default: 20 | Min: 1 | Max: 99999
    notification_interval: int
    # Information alert interval in minutes. | Default: 30 | Min: 1 | Max: 99999
    information_interval: int
    # Debug alert interval in minutes. | Default: 60 | Min: 1 | Max: 99999
    debug_interval: int
    # Lowest severity level to log. | Default: alert
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    
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
    Configure alert email settings.
    
    Path: alertemail/setting
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
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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