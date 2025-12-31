"""FortiOS CMDB - Extension-controller category"""

from .dataplan import Dataplan
from .extender import Extender
from .extender_profile import ExtenderProfile
from .extender_vap import ExtenderVap
from .fortigate import Fortigate
from .fortigate_profile import FortigateProfile

__all__ = [
    "Dataplan",
    "Extender",
    "ExtenderProfile",
    "ExtenderVap",
    "Fortigate",
    "FortigateProfile",
]


class ExtensionController:
    """
    ExtensionController category wrapper.

    This class provides access to all extension-controller CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize ExtensionController with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.dataplan = Dataplan(client)
        self.extender = Extender(client)
        self.extender_profile = ExtenderProfile(client)
        self.extender_vap = ExtenderVap(client)
        self.fortigate = Fortigate(client)
        self.fortigate_profile = FortigateProfile(client)
