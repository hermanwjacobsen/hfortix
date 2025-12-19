"""
FortiOS Monitor - Wifi
WiFi controller and AP monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Wifi"]

from .ap_channels import ApChannels
from .ap_names import ApNames
from .ap_profile import ApProfile
from .ap_status import ApStatus
from .client import Client
from .euclid import Euclid
from .firmware import Firmware
from .interfering_ap import InterferingAp
from .managed_ap import ManagedAp
from .matched_devices import MatchedDevices
from .meta import Meta
from .nac_device import NacDevice
from .network import Network
from .region_image import RegionImage
from .rogue_ap import RogueAp
from .spectrum import Spectrum
from .ssid import Ssid
from .station_capability import StationCapability
from .statistics import Statistics
from .unassociated_devices import UnassociatedDevices
from .vlan_probe import VlanProbe


class Wifi:
    """Wifi Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Wifi Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.ap_channels = ApChannels(client)
        self.ap_names = ApNames(client)
        self.ap_profile = ApProfile(client)
        self.ap_status = ApStatus(client)
        self.client = Client(client)
        self.euclid = Euclid(client)
        self.firmware = Firmware(client)
        self.interfering_ap = InterferingAp(client)
        self.managed_ap = ManagedAp(client)
        self.matched_devices = MatchedDevices(client)
        self.meta = Meta(client)
        self.nac_device = NacDevice(client)
        self.network = Network(client)
        self.region_image = RegionImage(client)
        self.rogue_ap = RogueAp(client)
        self.spectrum = Spectrum(client)
        self.ssid = Ssid(client)
        self.station_capability = StationCapability(client)
        self.statistics = Statistics(client)
        self.unassociated_devices = UnassociatedDevices(client)
        self.vlan_probe = VlanProbe(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "ap_channels",
            "ap_names",
            "ap_profile",
            "ap_status",
            "client",
            "euclid",
            "firmware",
            "interfering_ap",
            "managed_ap",
            "matched_devices",
            "meta",
            "nac_device",
            "network",
            "region_image",
            "rogue_ap",
            "spectrum",
            "ssid",
            "station_capability",
            "statistics",
            "unassociated_devices",
            "vlan_probe"
        ]
