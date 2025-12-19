"""UUID list and type lookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class TypeLookup:
    """UUID type lookup resource."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize TypeLookup resource.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        uuids: str | list[str],
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a mapping of UUIDs to their firewall object type for given UUIDs.

        Args:
            uuids: UUID or list of UUIDs to lookup (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary mapping UUIDs to their object types

        Example:
            >>> fgt.api.monitor.firewall.uuid.type_lookup.get(uuids='uuid1')
            >>> fgt.api.monitor.firewall.uuid.type_lookup.get(uuids=['uuid1', 'uuid2'])
        """
        params = payload_dict.copy() if payload_dict else {}
        params["uuids"] = uuids
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/uuid-type-lookup", params=params)


class UUID:
    """UUID list and type lookup operations."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize UUID endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize resource endpoints
        self.type_lookup = TypeLookup(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of all UUIDs with their object type and VDOM.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing UUID list

        Example:
            >>> fgt.api.monitor.firewall.uuid.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/uuid-list", params=params)
