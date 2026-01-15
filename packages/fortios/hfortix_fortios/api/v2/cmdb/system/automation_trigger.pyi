from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutomationTriggerPayload(TypedDict, total=False):
    """
    Type hints for system/automation_trigger payload fields.
    
    Trigger for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.automation-stitch.AutomationStitchEndpoint` (via: stitch-name)

    **Usage:**
        payload: AutomationTriggerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    trigger_type: Literal["event-based", "scheduled"]  # Trigger type. | Default: event-based
    event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]  # Event type. | Default: ioc
    vdom: list[dict[str, Any]]  # Virtual domain(s) that this trigger is valid for.
    license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]  # License type. | Default: forticare-support
    report_type: Literal["posture", "coverage", "optimization", "any"]  # Security Rating report. | Default: posture
    stitch_name: str  # Triggering stitch name. | MaxLen: 35
    logid: list[dict[str, Any]]  # Log IDs to trigger event.
    trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"]  # Scheduled trigger frequency (default = daily). | Default: daily
    trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week for trigger.
    trigger_day: int  # Day within a month to trigger. | Default: 1 | Min: 1 | Max: 31
    trigger_hour: int  # Hour of the day on which to trigger | Default: 0 | Min: 0 | Max: 23
    trigger_minute: int  # Minute of the hour on which to trigger | Default: 0 | Min: 0 | Max: 59
    trigger_datetime: str  # Trigger date and time (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    fields: list[dict[str, Any]]  # Customized trigger field settings.
    faz_event_name: str  # FortiAnalyzer event handler name. | MaxLen: 255
    faz_event_severity: str  # FortiAnalyzer event severity. | MaxLen: 255
    faz_event_tags: str  # FortiAnalyzer event tags. | MaxLen: 255
    serial: str  # Fabric connector serial number. | MaxLen: 255
    fabric_event_name: str  # Fabric connector event handler name. | MaxLen: 255
    fabric_event_severity: str  # Fabric connector event severity. | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

class AutomationTriggerVdomItem(TypedDict):
    """Type hints for vdom table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Virtual domain name. | MaxLen: 79


class AutomationTriggerLogidItem(TypedDict):
    """Type hints for logid table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Log ID. | Default: 0 | Min: 1 | Max: 65535


class AutomationTriggerFieldsItem(TypedDict):
    """Type hints for fields table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Name. | MaxLen: 35
    value: str  # Value. | MaxLen: 63


# Nested classes for table field children (object mode)

@final
class AutomationTriggerVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name. | MaxLen: 79
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
class AutomationTriggerLogidObject:
    """Typed object for logid table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Log ID. | Default: 0 | Min: 1 | Max: 65535
    id: int
    
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
class AutomationTriggerFieldsObject:
    """Typed object for fields table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Name. | MaxLen: 35
    name: str
    # Value. | MaxLen: 63
    value: str
    
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
class AutomationTriggerResponse(TypedDict):
    """
    Type hints for system/automation_trigger API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    trigger_type: Literal["event-based", "scheduled"]  # Trigger type. | Default: event-based
    event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]  # Event type. | Default: ioc
    vdom: list[AutomationTriggerVdomItem]  # Virtual domain(s) that this trigger is valid for.
    license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]  # License type. | Default: forticare-support
    report_type: Literal["posture", "coverage", "optimization", "any"]  # Security Rating report. | Default: posture
    stitch_name: str  # Triggering stitch name. | MaxLen: 35
    logid: list[AutomationTriggerLogidItem]  # Log IDs to trigger event.
    trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"]  # Scheduled trigger frequency (default = daily). | Default: daily
    trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week for trigger.
    trigger_day: int  # Day within a month to trigger. | Default: 1 | Min: 1 | Max: 31
    trigger_hour: int  # Hour of the day on which to trigger | Default: 0 | Min: 0 | Max: 23
    trigger_minute: int  # Minute of the hour on which to trigger | Default: 0 | Min: 0 | Max: 59
    trigger_datetime: str  # Trigger date and time (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    fields: list[AutomationTriggerFieldsItem]  # Customized trigger field settings.
    faz_event_name: str  # FortiAnalyzer event handler name. | MaxLen: 255
    faz_event_severity: str  # FortiAnalyzer event severity. | MaxLen: 255
    faz_event_tags: str  # FortiAnalyzer event tags. | MaxLen: 255
    serial: str  # Fabric connector serial number. | MaxLen: 255
    fabric_event_name: str  # Fabric connector event handler name. | MaxLen: 255
    fabric_event_severity: str  # Fabric connector event severity. | MaxLen: 255


@final
class AutomationTriggerObject:
    """Typed FortiObject for system/automation_trigger with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Description. | MaxLen: 255
    description: str
    # Trigger type. | Default: event-based
    trigger_type: Literal["event-based", "scheduled"]
    # Event type. | Default: ioc
    event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]
    # Virtual domain(s) that this trigger is valid for.
    vdom: list[AutomationTriggerVdomObject]
    # License type. | Default: forticare-support
    license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]
    # Security Rating report. | Default: posture
    report_type: Literal["posture", "coverage", "optimization", "any"]
    # Triggering stitch name. | MaxLen: 35
    stitch_name: str
    # Log IDs to trigger event.
    logid: list[AutomationTriggerLogidObject]
    # Scheduled trigger frequency (default = daily). | Default: daily
    trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"]
    # Day of week for trigger.
    trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Day within a month to trigger. | Default: 1 | Min: 1 | Max: 31
    trigger_day: int
    # Hour of the day on which to trigger (0 - 23, default = 1). | Default: 0 | Min: 0 | Max: 23
    trigger_hour: int
    # Minute of the hour on which to trigger (0 - 59, default = 0) | Default: 0 | Min: 0 | Max: 59
    trigger_minute: int
    # Trigger date and time (YYYY-MM-DD HH:MM:SS). | Default: 0000-00-00 00:00:00
    trigger_datetime: str
    # Customized trigger field settings.
    fields: list[AutomationTriggerFieldsObject]
    # FortiAnalyzer event handler name. | MaxLen: 255
    faz_event_name: str
    # FortiAnalyzer event severity. | MaxLen: 255
    faz_event_severity: str
    # FortiAnalyzer event tags. | MaxLen: 255
    faz_event_tags: str
    # Fabric connector serial number. | MaxLen: 255
    serial: str
    # Fabric connector event handler name. | MaxLen: 255
    fabric_event_name: str
    # Fabric connector event severity. | MaxLen: 255
    fabric_event_severity: str
    
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
    def to_dict(self) -> AutomationTriggerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutomationTrigger:
    """
    Trigger for automation stitches.
    
    Path: system/automation_trigger
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> FortiObjectList[AutomationTriggerObject]: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> FortiObjectList[AutomationTriggerObject]: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> FortiObjectList[AutomationTriggerObject]: ...
    
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
    ) -> AutomationTriggerObject | list[AutomationTriggerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationTriggerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationTriggerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutomationTriggerObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
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
    "AutomationTrigger",
    "AutomationTriggerPayload",
    "AutomationTriggerResponse",
    "AutomationTriggerObject",
]