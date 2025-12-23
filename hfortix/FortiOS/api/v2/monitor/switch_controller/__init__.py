"""
FortiOS Monitor - Switch Controller
FortiSwitch controller monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

__all__ = ["SwitchController"]

from .detected_device import DetectedDevice
from .fsw_firmware import FswFirmware
from .isl_lockdown import IslLockdown
from .known_nac_device_criteria_list import KnownNacDeviceCriteriaList
from .managed_switch import ManagedSwitch
from .matched_devices import MatchedDevices
from .mclag_icl import MclagIcl
from .nac_device import NacDevice
from .recommendation import Recommendation


class SwitchController:
    """SwitchController Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize SwitchController Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.detected_device = DetectedDevice(client)
        self.fsw_firmware = FswFirmware(client)
        self.isl_lockdown = IslLockdown(client)
        self.known_nac_device_criteria_list = KnownNacDeviceCriteriaList(
            client
        )
        self.managed_switch = ManagedSwitch(client)
        self.matched_devices = MatchedDevices(client)
        self.mclag_icl = MclagIcl(client)
        self.nac_device = NacDevice(client)
        self.recommendation = Recommendation(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "detected_device",
            "fsw_firmware",
            "isl_lockdown",
            "known_nac_device_criteria_list",
            "managed_switch",
            "matched_devices",
            "mclag_icl",
            "nac_device",
            "recommendation",
        ]
