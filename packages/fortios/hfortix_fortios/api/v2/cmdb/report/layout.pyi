from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LayoutPayload(TypedDict, total=False):
    """
    Type hints for report/layout payload fields.
    
    Report layout configuration.
    
    **Usage:**
        payload: LayoutPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Report layout name. | MaxLen: 35
    title: str  # Report title. | MaxLen: 127
    subtitle: str  # Report subtitle. | MaxLen: 127
    description: str  # Description. | MaxLen: 127
    style_theme: str  # Report style theme. | MaxLen: 35
    options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]  # Report layout options. | Default: include-table-of-content auto-numbering-heading view-chart-as-heading
    format: Literal["pdf"]  # Report format. | Default: pdf
    schedule_type: Literal["demand", "daily", "weekly"]  # Report schedule type. | Default: daily
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Schedule days of week to generate report. | Default: sunday
    time: str  # Schedule time to generate report (format = hh:mm).
    cutoff_option: Literal["run-time", "custom"]  # Cutoff-option is either run-time or custom. | Default: run-time
    cutoff_time: str  # Custom cutoff time to generate report
    email_send: Literal["enable", "disable"]  # Enable/disable sending emails after reports are ge | Default: disable
    email_recipients: str  # Email recipients for generated reports. | MaxLen: 511
    max_pdf_report: int  # Maximum number of PDF reports to keep at one time | Default: 31 | Min: 1 | Max: 365
    page: str  # Configure report page.
    body_item: list[dict[str, Any]]  # Configure report body item.

# Nested TypedDicts for table field children (dict mode)

class LayoutBodyitemItem(TypedDict):
    """Type hints for body-item table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Report item ID. | Default: 0 | Min: 0 | Max: 4294967295
    description: str  # Description. | MaxLen: 63
    type: Literal["text", "image", "chart", "misc"]  # Report item type. | Default: text
    style: str  # Report item style. | MaxLen: 71
    top_n: int  # Value of top. | Default: 0 | Min: 0 | Max: 4294967295
    parameters: str  # Parameters.
    text_component: Literal["text", "heading1", "heading2", "heading3"]  # Report item text component. | Default: text
    content: str  # Report item text content. | MaxLen: 511
    img_src: str  # Report item image file name. | MaxLen: 127
    chart: str  # Report item chart name. | MaxLen: 71
    chart_options: Literal["include-no-data", "hide-title", "show-caption"]  # Report chart options. | Default: include-no-data hide-title show-caption
    misc_component: Literal["hline", "page-break", "column-break", "section-start"]  # Report item miscellaneous component. | Default: hline
    title: str  # Report section title. | MaxLen: 511


# Nested classes for table field children (object mode)

@final
class LayoutBodyitemObject:
    """Typed object for body-item table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Report item ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Description. | MaxLen: 63
    description: str
    # Report item type. | Default: text
    type: Literal["text", "image", "chart", "misc"]
    # Report item style. | MaxLen: 71
    style: str
    # Value of top. | Default: 0 | Min: 0 | Max: 4294967295
    top_n: int
    # Parameters.
    parameters: str
    # Report item text component. | Default: text
    text_component: Literal["text", "heading1", "heading2", "heading3"]
    # Report item text content. | MaxLen: 511
    content: str
    # Report item image file name. | MaxLen: 127
    img_src: str
    # Report item chart name. | MaxLen: 71
    chart: str
    # Report chart options. | Default: include-no-data hide-title show-caption
    chart_options: Literal["include-no-data", "hide-title", "show-caption"]
    # Report item miscellaneous component. | Default: hline
    misc_component: Literal["hline", "page-break", "column-break", "section-start"]
    # Report section title. | MaxLen: 511
    title: str
    
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
class LayoutResponse(TypedDict):
    """
    Type hints for report/layout API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Report layout name. | MaxLen: 35
    title: str  # Report title. | MaxLen: 127
    subtitle: str  # Report subtitle. | MaxLen: 127
    description: str  # Description. | MaxLen: 127
    style_theme: str  # Report style theme. | MaxLen: 35
    options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]  # Report layout options. | Default: include-table-of-content auto-numbering-heading view-chart-as-heading
    format: Literal["pdf"]  # Report format. | Default: pdf
    schedule_type: Literal["demand", "daily", "weekly"]  # Report schedule type. | Default: daily
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Schedule days of week to generate report. | Default: sunday
    time: str  # Schedule time to generate report (format = hh:mm).
    cutoff_option: Literal["run-time", "custom"]  # Cutoff-option is either run-time or custom. | Default: run-time
    cutoff_time: str  # Custom cutoff time to generate report
    email_send: Literal["enable", "disable"]  # Enable/disable sending emails after reports are ge | Default: disable
    email_recipients: str  # Email recipients for generated reports. | MaxLen: 511
    max_pdf_report: int  # Maximum number of PDF reports to keep at one time | Default: 31 | Min: 1 | Max: 365
    page: str  # Configure report page.
    body_item: list[LayoutBodyitemItem]  # Configure report body item.


@final
class LayoutObject:
    """Typed FortiObject for report/layout with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Report layout name. | MaxLen: 35
    name: str
    # Report title. | MaxLen: 127
    title: str
    # Report subtitle. | MaxLen: 127
    subtitle: str
    # Description. | MaxLen: 127
    description: str
    # Report style theme. | MaxLen: 35
    style_theme: str
    # Report layout options. | Default: include-table-of-content auto-numbering-heading view-chart-as-heading
    options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]
    # Report format. | Default: pdf
    format: Literal["pdf"]
    # Report schedule type. | Default: daily
    schedule_type: Literal["demand", "daily", "weekly"]
    # Schedule days of week to generate report. | Default: sunday
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Schedule time to generate report (format = hh:mm).
    time: str
    # Cutoff-option is either run-time or custom. | Default: run-time
    cutoff_option: Literal["run-time", "custom"]
    # Custom cutoff time to generate report (format = hh:mm).
    cutoff_time: str
    # Enable/disable sending emails after reports are generated. | Default: disable
    email_send: Literal["enable", "disable"]
    # Email recipients for generated reports. | MaxLen: 511
    email_recipients: str
    # Maximum number of PDF reports to keep at one time | Default: 31 | Min: 1 | Max: 365
    max_pdf_report: int
    # Configure report page.
    page: str
    # Configure report body item.
    body_item: list[LayoutBodyitemObject]
    
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
    def to_dict(self) -> LayoutPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Layout:
    """
    Report layout configuration.
    
    Path: report/layout
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
    ) -> LayoutObject: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> list[LayoutObject]: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> list[LayoutObject]: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> list[LayoutObject]: ...
    
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
    ) -> LayoutObject | list[LayoutObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LayoutObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LayoutObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> LayoutObject: ...
    
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
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Layout",
    "LayoutPayload",
    "LayoutResponse",
    "LayoutObject",
]