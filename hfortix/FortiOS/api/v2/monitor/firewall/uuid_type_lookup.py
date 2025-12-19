"""Monitor API - UuidTypeLookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class UuidTypeLookup:
    """UuidTypeLookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize UuidTypeLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        uuids: Any,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a mapping of UUIDs to their firewall object type for given UUIDs.
        
        Args:
            uuids: UUID to be resolved. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.uuid_type_lookup.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params['uuids'] = uuids
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/uuid-type-lookup", params=params)
