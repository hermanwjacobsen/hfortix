"""FortiOS CMDB - Rule category"""

from .fmwp import Fmwp
from .iotd import Iotd
from .otdt import Otdt
from .otvp import Otvp

__all__ = ["Fmwp", "Iotd", "Otdt", "Otvp"]


class Rule:
    """
    Rule category wrapper.

    This class provides access to all rule CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Rule with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.fmwp = Fmwp(client)
        self.iotd = Iotd(client)
        self.otdt = Otdt(client)
        self.otvp = Otvp(client)
