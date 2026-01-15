"""Type stubs for SWITCH_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .detected_device import DetectedDevice
    from .known_nac_device_criteria_list import KnownNacDeviceCriteriaList
    from .matched_devices import MatchedDevices
    from .fsw_firmware import FswFirmware
    from .isl_lockdown import IslLockdown
    from .managed_switch import ManagedSwitch
    from .mclag_icl import MclagIcl
    from .nac_device import NacDevice
    from .recommendation import Recommendation

__all__ = [
    "DetectedDevice",
    "KnownNacDeviceCriteriaList",
    "MatchedDevices",
    "SwitchController",
]


class SwitchController:
    """SWITCH_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fsw_firmware: FswFirmware
    isl_lockdown: IslLockdown
    managed_switch: ManagedSwitch
    mclag_icl: MclagIcl
    nac_device: NacDevice
    recommendation: Recommendation
    detected_device: DetectedDevice
    known_nac_device_criteria_list: KnownNacDeviceCriteriaList
    matched_devices: MatchedDevices

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize switch_controller category with HTTP client."""
        ...
