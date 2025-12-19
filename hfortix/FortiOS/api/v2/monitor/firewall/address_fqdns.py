"""Monitor API - AddressFqdns operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class AddressFqdns:
    """AddressFqdns operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AddressFqdns endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List of FQDN address objects and the IPs they resolved to.
        
        Args:
            mkey: Name of the FQDN address to retrieve. If this is not provided, the count of IPs FQDN resolves to will be returned. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.address_fqdns.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/address-fqdns", params=params)
