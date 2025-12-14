"""
FortiOS CMDB - Firewall Shaper Sub-category

This module provides access to firewall traffic shaper endpoints.
"""


class Shaper:
    """Firewall shaper sub-category"""
    
    def __init__(self, client):
        self._client = client
        self._per_ip_shaper = None
        self._traffic_shaper = None
    
    @property
    def per_ip_shaper(self):
        """Access firewall.shaper/per-ip-shaper endpoint"""
        if self._per_ip_shaper is None:
            from .shaper_per_ip_shaper import PerIpShaper
            self._per_ip_shaper = PerIpShaper(self._client)
        return self._per_ip_shaper
    
    @property
    def traffic_shaper(self):
        """Access firewall.shaper/traffic-shaper endpoint"""
        if self._traffic_shaper is None:
            from .shaper_traffic_shaper import TrafficShaper
            self._traffic_shaper = TrafficShaper(self._client)
        return self._traffic_shaper
