"""Monitor API - Recommendation operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class PseConfig:
    """PseConfig operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize PseConfig endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        fortilink: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Execute switch recommendation for pse-config to prevent PSE-PSE scenarios.
        
        Args:
            fortilink: FortiLink interface name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.switch_controller.recommendation.pse_config.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if fortilink is not None:
            data['fortilink'] = fortilink
        data.update(kwargs)
        return self._client.post("monitor", "/switch-controller/recommendation/pse-config", data=data)


class Recommendation:
    """Recommendation operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Recommendation endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.pse_config = PseConfig(client)
