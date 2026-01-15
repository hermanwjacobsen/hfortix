from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FederatedUpgradePayload(TypedDict, total=False):
    """
    Type hints for system/federated_upgrade payload fields.
    
    Coordinate federated upgrades within the Security Fabric.
    
    **Usage:**
        payload: FederatedUpgradePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]  # Current status of the upgrade. | Default: disabled
    source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"]  # Source that set up the federated upgrade config. | Default: user
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]  # Reason for upgrade failure. | Default: none
    failure_device: str  # Serial number of the node to include. | MaxLen: 79
    upgrade_id: int  # Unique identifier for this upgrade. | Default: 0 | Min: 0 | Max: 4294967295
    next_path_index: int  # The index of the next image to upgrade to. | Default: 0 | Min: 0 | Max: 10
    ignore_signing_errors: Literal["enable", "disable"]  # Allow/reject use of FortiGate firmware images that | Default: disable
    ha_reboot_controller: str  # Serial number of the FortiGate unit that will cont | MaxLen: 79
    known_ha_members: list[dict[str, Any]]  # Known members of the HA cluster. If a member is mi
    initial_version: str  # Firmware version when the upgrade was set up.
    starter_admin: str  # Admin that started the upgrade. | MaxLen: 64
    node_list: list[dict[str, Any]]  # Nodes which will be included in the upgrade.

# Nested TypedDicts for table field children (dict mode)

class FederatedUpgradeKnownhamembersItem(TypedDict):
    """Type hints for known-ha-members table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    serial: str  # Serial number of HA member | MaxLen: 79


class FederatedUpgradeNodelistItem(TypedDict):
    """Type hints for node-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    serial: str  # Serial number of the node to include. | MaxLen: 79
    timing: Literal["immediate", "scheduled"]  # Run immediately or at a scheduled time. | Default: immediate
    maximum_minutes: int  # Maximum number of minutes to allow for immediate u | Default: 15 | Min: 5 | Max: 10080
    time: str  # Scheduled upgrade execution time in UTC
    setup_time: str  # Upgrade preparation start time in UTC
    upgrade_path: str  # Fortinet OS image versions to upgrade through in m
    device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"]  # Fortinet device type. | Default: fortigate
    allow_download: Literal["enable", "disable"]  # Enable/disable download firmware images. | Default: enable
    coordinating_fortigate: str  # Serial number of the FortiGate unit that controls | MaxLen: 79
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]  # Upgrade failure reason. | Default: none


# Nested classes for table field children (object mode)

@final
class FederatedUpgradeKnownhamembersObject:
    """Typed object for known-ha-members table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial number of HA member | MaxLen: 79
    serial: str
    
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
class FederatedUpgradeNodelistObject:
    """Typed object for node-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial number of the node to include. | MaxLen: 79
    serial: str
    # Run immediately or at a scheduled time. | Default: immediate
    timing: Literal["immediate", "scheduled"]
    # Maximum number of minutes to allow for immediate upgrade pre | Default: 15 | Min: 5 | Max: 10080
    maximum_minutes: int
    # Scheduled upgrade execution time in UTC
    time: str
    # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC)
    setup_time: str
    # Fortinet OS image versions to upgrade through in major-minor
    upgrade_path: str
    # Fortinet device type. | Default: fortigate
    device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"]
    # Enable/disable download firmware images. | Default: enable
    allow_download: Literal["enable", "disable"]
    # Serial number of the FortiGate unit that controls this devic | MaxLen: 79
    coordinating_fortigate: str
    # Upgrade failure reason. | Default: none
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]
    
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
class FederatedUpgradeResponse(TypedDict):
    """
    Type hints for system/federated_upgrade API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]  # Current status of the upgrade. | Default: disabled
    source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"]  # Source that set up the federated upgrade config. | Default: user
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]  # Reason for upgrade failure. | Default: none
    failure_device: str  # Serial number of the node to include. | MaxLen: 79
    upgrade_id: int  # Unique identifier for this upgrade. | Default: 0 | Min: 0 | Max: 4294967295
    next_path_index: int  # The index of the next image to upgrade to. | Default: 0 | Min: 0 | Max: 10
    ignore_signing_errors: Literal["enable", "disable"]  # Allow/reject use of FortiGate firmware images that | Default: disable
    ha_reboot_controller: str  # Serial number of the FortiGate unit that will cont | MaxLen: 79
    known_ha_members: list[FederatedUpgradeKnownhamembersItem]  # Known members of the HA cluster. If a member is mi
    initial_version: str  # Firmware version when the upgrade was set up.
    starter_admin: str  # Admin that started the upgrade. | MaxLen: 64
    node_list: list[FederatedUpgradeNodelistItem]  # Nodes which will be included in the upgrade.


@final
class FederatedUpgradeObject:
    """Typed FortiObject for system/federated_upgrade with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Current status of the upgrade. | Default: disabled
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]
    # Source that set up the federated upgrade config. | Default: user
    source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"]
    # Reason for upgrade failure. | Default: none
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]
    # Serial number of the node to include. | MaxLen: 79
    failure_device: str
    # Unique identifier for this upgrade. | Default: 0 | Min: 0 | Max: 4294967295
    upgrade_id: int
    # The index of the next image to upgrade to. | Default: 0 | Min: 0 | Max: 10
    next_path_index: int
    # Allow/reject use of FortiGate firmware images that are unsig | Default: disable
    ignore_signing_errors: Literal["enable", "disable"]
    # Serial number of the FortiGate unit that will control the re | MaxLen: 79
    ha_reboot_controller: str
    # Known members of the HA cluster. If a member is missing at u
    known_ha_members: list[FederatedUpgradeKnownhamembersObject]
    # Firmware version when the upgrade was set up.
    initial_version: str
    # Admin that started the upgrade. | MaxLen: 64
    starter_admin: str
    # Nodes which will be included in the upgrade.
    node_list: list[FederatedUpgradeNodelistObject]
    
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
    def to_dict(self) -> FederatedUpgradePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FederatedUpgrade:
    """
    Coordinate federated upgrades within the Security Fabric.
    
    Path: system/federated_upgrade
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FederatedUpgradeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "FederatedUpgrade",
    "FederatedUpgradePayload",
    "FederatedUpgradeResponse",
    "FederatedUpgradeObject",
]