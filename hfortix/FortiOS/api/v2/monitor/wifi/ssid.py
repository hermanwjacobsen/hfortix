"""Monitor API - Ssid operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GenerateKeys:
    """GenerateKeys operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize GenerateKeys endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mpsk_profile: str | None = None,
        group: str | None = None,
        prefix: str | None = None,
        count: int | None = None,
        key_length: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Generate pre-shared keys for specific multi pre-shared key profile.
        
        Args:
            mpsk_profile: Multi pre-shared key profile to add keys to. (optional)
            group: Multi pre-shared key group to add keys to. (optional)
            prefix: Prefix to be added at the start of the generated key's name. (optional)
            count: Number of keys to be generated [1-512]. (optional)
            key_length: Length of the keys to be generated [8-63]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.ssid.generate_keys.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mpsk_profile is not None:
            data['mpsk_profile'] = mpsk_profile
        if group is not None:
            data['group'] = group
        if prefix is not None:
            data['prefix'] = prefix
        if count is not None:
            data['count'] = count
        if key_length is not None:
            data['key_length'] = key_length
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/ssid/generate-keys", data=data)


class Ssid:
    """Ssid operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ssid endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.generate_keys = GenerateKeys(client)
