"""IPv6 FQDN address object resolution monitoring."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class AddressFqdns6:
    """IPv6 FQDN address objects and resolved IPs."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize AddressFqdns6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List of all IPv6 FQDN address objects and the IPs they resolved to.

        Args:
            data_dict: Optional dictionary of parameters
            name: Filter by address object name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IPv6 FQDN address resolutions

        Example:
            >>> fgt.api.monitor.firewall.address_fqdns6.list()
            >>> fgt.api.monitor.firewall.address_fqdns6.list(name='google_dns_v6')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/address-fqdns6", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get IPv6 FQDN resolution for a specific address object.

        Args:
            data_dict: Optional dictionary of parameters
            name: Address object name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IPv6 FQDN address resolution

        Example:
            >>> fgt.api.monitor.firewall.address_fqdns6.get(name='google_dns_v6')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/address-fqdns6", params=params)
