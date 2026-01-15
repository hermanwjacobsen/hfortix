from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class InternetServiceNamePayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_name payload fields.
    
    Define internet service names.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.city.CityEndpoint` (via: city-id)
        - :class:`~.firewall.country.CountryEndpoint` (via: country-id)
        - :class:`~.firewall.internet-service.InternetServiceEndpoint` (via: internet-service-id)
        - :class:`~.firewall.region.RegionEndpoint` (via: region-id)

    **Usage:**
        payload: InternetServiceNamePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Internet Service name. | MaxLen: 63
    type: Literal["default", "location"]  # Internet Service name type. | Default: default
    internet_service_id: int  # Internet Service ID. | Default: 0 | Min: 0 | Max: 4294967295
    country_id: int  # Country or Area ID. | Default: 0 | Min: 0 | Max: 4294967295
    region_id: int  # Region ID. | Default: 0 | Min: 0 | Max: 4294967295
    city_id: int  # City ID. | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class InternetServiceNameResponse(TypedDict):
    """
    Type hints for firewall/internet_service_name API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Internet Service name. | MaxLen: 63
    type: Literal["default", "location"]  # Internet Service name type. | Default: default
    internet_service_id: int  # Internet Service ID. | Default: 0 | Min: 0 | Max: 4294967295
    country_id: int  # Country or Area ID. | Default: 0 | Min: 0 | Max: 4294967295
    region_id: int  # Region ID. | Default: 0 | Min: 0 | Max: 4294967295
    city_id: int  # City ID. | Default: 0 | Min: 0 | Max: 4294967295


@final
class InternetServiceNameObject:
    """Typed FortiObject for firewall/internet_service_name with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Internet Service name. | MaxLen: 63
    name: str
    # Internet Service name type. | Default: default
    type: Literal["default", "location"]
    # Internet Service ID. | Default: 0 | Min: 0 | Max: 4294967295
    internet_service_id: int
    # Country or Area ID. | Default: 0 | Min: 0 | Max: 4294967295
    country_id: int
    # Region ID. | Default: 0 | Min: 0 | Max: 4294967295
    region_id: int
    # City ID. | Default: 0 | Min: 0 | Max: 4294967295
    city_id: int
    
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
    def to_dict(self) -> InternetServiceNamePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InternetServiceName:
    """
    Define internet service names.
    
    Path: firewall/internet_service_name
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> list[InternetServiceNameObject]: ...
    
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> list[InternetServiceNameObject]: ...
    
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> list[InternetServiceNameObject]: ...
    
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
    ) -> InternetServiceNameObject | list[InternetServiceNameObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InternetServiceNameObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InternetServiceNameObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
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
    ) -> InternetServiceNameObject: ...
    
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
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
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
    "InternetServiceName",
    "InternetServiceNamePayload",
    "InternetServiceNameResponse",
    "InternetServiceNameObject",
]