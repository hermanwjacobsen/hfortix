"""UUID list and type lookup operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class UUID:
    """UUID list and type lookup operations."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize UUID endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Retrieve a list of all UUIDs with their object type and VDOM.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing UUID list

        Example:
            >>> fgt.api.monitor.firewall.uuid.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/uuid-list", params=params)

    def type_lookup(
        self, data_dict: Optional[Dict[str, Any]] = None, uuids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Retrieve a mapping of UUIDs to their firewall object type for given UUIDs.

        Args:
            data_dict: Optional dictionary of parameters
            uuids: Comma-separated list of UUIDs to lookup (required)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary mapping UUIDs to their object types

        Example:
            >>> fgt.api.monitor.firewall.uuid.type_lookup(uuids='uuid1,uuid2,uuid3')
        """
        params = data_dict.copy() if data_dict else {}
        if uuids is not None:
            params["uuids"] = uuids
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/uuid-type-lookup", params=params)
