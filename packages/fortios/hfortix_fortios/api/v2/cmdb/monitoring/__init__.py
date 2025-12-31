"""FortiOS CMDB - Monitoring category"""

from .npu_hpe import NpuHpe

__all__ = ["NpuHpe"]


class Monitoring:
    """
    Monitoring category wrapper.

    This class provides access to all monitoring CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Monitoring with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.npu_hpe = NpuHpe(client)
