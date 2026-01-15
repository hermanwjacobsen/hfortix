"""
FortiManager Proxy Response Models

Data classes for FMG proxy responses.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DeviceResult:
    """
    Result from a single device in a proxy response.
    
    Attributes:
        target: Device name (e.g., "firewall-01")
        response: The FortiOS API response dict
        status: FMG status dict with code and message
    """
    target: str
    response: dict[str, Any]
    status: dict[str, Any] = field(default_factory=lambda: {"code": 0, "message": "OK"})
    
    @property
    def success(self) -> bool:
        """Check if the request was successful."""
        return self.status.get("code") == 0
    
    @property
    def failed(self) -> bool:
        """Check if the request failed."""
        return not self.success
    
    @property
    def http_status(self) -> int | None:
        """HTTP status code from the FortiOS response."""
        return self.response.get("http_status")
    
    @property
    def results(self) -> Any:
        """Results data from the FortiOS response."""
        return self.response.get("results")


@dataclass
class ProxyResponse:
    """
    Response from a FortiManager proxy request.
    
    Contains results from one or more devices.
    
    Attributes:
        data: List of DeviceResult objects
        status: Overall FMG status
        url: The FMG API URL used
    """
    data: list[DeviceResult] = field(default_factory=list)
    status: dict[str, Any] = field(default_factory=lambda: {"code": 0, "message": "OK"})
    url: str = "/sys/proxy/json"
    
    def __iter__(self):
        """Iterate over device results."""
        return iter(self.data)
    
    def __len__(self) -> int:
        """Number of device results."""
        return len(self.data)
    
    def __getitem__(self, index: int) -> DeviceResult:
        """Get device result by index."""
        return self.data[index]
    
    @property
    def success(self) -> bool:
        """Check if all device requests were successful."""
        return self.status.get("code") == 0 and all(d.success for d in self.data)
    
    @property
    def success_count(self) -> int:
        """Count of successful device results."""
        return sum(1 for d in self.data if d.success)
    
    @property
    def failed_count(self) -> int:
        """Count of failed device results."""
        return sum(1 for d in self.data if d.failed)
    
    @property
    def first(self) -> DeviceResult | None:
        """Get the first device result (convenience for single-device requests)."""
        return self.data[0] if self.data else None
    
    @classmethod
    def from_fmg_response(cls, response: dict[str, Any]) -> "ProxyResponse":
        """
        Parse a FortiManager JSON-RPC response into a ProxyResponse.
        
        Args:
            response: Raw FMG response dict
            
        Returns:
            ProxyResponse object
        """
        result = response.get("result", [{}])[0]
        
        device_results = []
        for item in result.get("data", []):
            device_results.append(DeviceResult(
                target=item.get("target", "unknown"),
                response=item.get("response", {}),
                status=item.get("status", {"code": -1, "message": "Unknown"}),
            ))
        
        return cls(
            data=device_results,
            status=result.get("status", {"code": -1, "message": "Unknown"}),
            url=result.get("url", "/sys/proxy/json"),
        )
