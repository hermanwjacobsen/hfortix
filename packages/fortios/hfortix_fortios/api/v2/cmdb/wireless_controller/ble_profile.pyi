from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class BleProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/ble_profile payload fields.
    
    Configure Bluetooth Low Energy profile.
    
    **Usage:**
        payload: BleProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Bluetooth Low Energy profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"]  # Advertising type.
    ibeacon_uuid: str  # Universally Unique Identifier | Default: 005ea414-cbd1-11e5-9956-625662870761 | MaxLen: 63
    major_id: int  # Major ID. | Default: 1000 | Min: 0 | Max: 65535
    minor_id: int  # Minor ID. | Default: 2000 | Min: 0 | Max: 65535
    eddystone_namespace: str  # Eddystone namespace ID. | Default: 0102030405 | MaxLen: 20
    eddystone_instance: str  # Eddystone instance ID. | Default: abcdef | MaxLen: 12
    eddystone_url: str  # Eddystone URL. | Default: http://www.fortinet.com | MaxLen: 127
    txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]  # Transmit power level (default = 0). | Default: 0
    beacon_interval: int  # Beacon interval (default = 100 msec). | Default: 100 | Min: 40 | Max: 3500
    ble_scanning: Literal["enable", "disable"]  # Enable/disable Bluetooth Low Energy (BLE) scanning | Default: disable
    scan_type: Literal["active", "passive"]  # Scan Type (default = active). | Default: active
    scan_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -90 | MaxLen: 7
    scan_period: int  # Scan Period (default = 4000 msec). | Default: 4000 | Min: 1000 | Max: 10000
    scan_time: int  # Scan Time (default = 1000 msec). | Default: 1000 | Min: 1000 | Max: 10000
    scan_interval: int  # Scan Interval (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000
    scan_window: int  # Scan Windows (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class BleProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/ble_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Bluetooth Low Energy profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"]  # Advertising type.
    ibeacon_uuid: str  # Universally Unique Identifier | Default: 005ea414-cbd1-11e5-9956-625662870761 | MaxLen: 63
    major_id: int  # Major ID. | Default: 1000 | Min: 0 | Max: 65535
    minor_id: int  # Minor ID. | Default: 2000 | Min: 0 | Max: 65535
    eddystone_namespace: str  # Eddystone namespace ID. | Default: 0102030405 | MaxLen: 20
    eddystone_instance: str  # Eddystone instance ID. | Default: abcdef | MaxLen: 12
    eddystone_url: str  # Eddystone URL. | Default: http://www.fortinet.com | MaxLen: 127
    txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]  # Transmit power level (default = 0). | Default: 0
    beacon_interval: int  # Beacon interval (default = 100 msec). | Default: 100 | Min: 40 | Max: 3500
    ble_scanning: Literal["enable", "disable"]  # Enable/disable Bluetooth Low Energy (BLE) scanning | Default: disable
    scan_type: Literal["active", "passive"]  # Scan Type (default = active). | Default: active
    scan_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -90 | MaxLen: 7
    scan_period: int  # Scan Period (default = 4000 msec). | Default: 4000 | Min: 1000 | Max: 10000
    scan_time: int  # Scan Time (default = 1000 msec). | Default: 1000 | Min: 1000 | Max: 10000
    scan_interval: int  # Scan Interval (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000
    scan_window: int  # Scan Windows (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000


@final
class BleProfileObject:
    """Typed FortiObject for wireless_controller/ble_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Bluetooth Low Energy profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 63
    comment: str
    # Advertising type.
    advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"]
    # Universally Unique Identifier | Default: 005ea414-cbd1-11e5-9956-625662870761 | MaxLen: 63
    ibeacon_uuid: str
    # Major ID. | Default: 1000 | Min: 0 | Max: 65535
    major_id: int
    # Minor ID. | Default: 2000 | Min: 0 | Max: 65535
    minor_id: int
    # Eddystone namespace ID. | Default: 0102030405 | MaxLen: 20
    eddystone_namespace: str
    # Eddystone instance ID. | Default: abcdef | MaxLen: 12
    eddystone_instance: str
    # Eddystone URL. | Default: http://www.fortinet.com | MaxLen: 127
    eddystone_url: str
    # Transmit power level (default = 0). | Default: 0
    txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
    # Beacon interval (default = 100 msec). | Default: 100 | Min: 40 | Max: 3500
    beacon_interval: int
    # Enable/disable Bluetooth Low Energy (BLE) scanning. | Default: disable
    ble_scanning: Literal["enable", "disable"]
    # Scan Type (default = active). | Default: active
    scan_type: Literal["active", "passive"]
    # Minimum signal level/threshold in dBm required for the AP to | Default: -90 | MaxLen: 7
    scan_threshold: str
    # Scan Period (default = 4000 msec). | Default: 4000 | Min: 1000 | Max: 10000
    scan_period: int
    # Scan Time (default = 1000 msec). | Default: 1000 | Min: 1000 | Max: 10000
    scan_time: int
    # Scan Interval (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000
    scan_interval: int
    # Scan Windows (default = 50 msec). | Default: 50 | Min: 10 | Max: 1000
    scan_window: int
    
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
    def to_dict(self) -> BleProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class BleProfile:
    """
    Configure Bluetooth Low Energy profile.
    
    Path: wireless_controller/ble_profile
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
    ) -> BleProfileObject: ...
    
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
    ) -> BleProfileObject: ...
    
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
    ) -> FortiObjectList[BleProfileObject]: ...
    
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
    ) -> BleProfileObject: ...
    
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
    ) -> BleProfileObject: ...
    
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
    ) -> FortiObjectList[BleProfileObject]: ...
    
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
    ) -> BleProfileObject: ...
    
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
    ) -> BleProfileObject: ...
    
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
    ) -> FortiObjectList[BleProfileObject]: ...
    
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
    ) -> BleProfileObject | list[BleProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> BleProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> BleProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> BleProfileObject: ...
    
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
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
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
    "BleProfile",
    "BleProfilePayload",
    "BleProfileResponse",
    "BleProfileObject",
]