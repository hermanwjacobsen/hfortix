"""Monitor API - Object operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Usage:
    """Usage operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Usage endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        q_path: str | None = None,
        q_name: str | None = None,
        qtypes: list | None = None,
        scope: str | None = None,
        mkey: str | None = None,
        child_path: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve all objects that are currently using as well as objects that can use the given object.
        
        Args:
            q_path: The CMDB table's path (optional)
            q_name: The CMDB table's name (optional)
            qtypes: List of CMDB table qTypes (optional)
            scope: Scope of resource [vdom|global]. (optional)
            mkey: The mkey for the object (optional)
            child_path: The child path for the object (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.object.usage.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if q_path is not None:
            params['q_path'] = q_path
        if q_name is not None:
            params['q_name'] = q_name
        if qtypes is not None:
            params['qtypes'] = qtypes
        if scope is not None:
            params['scope'] = scope
        if mkey is not None:
            params['mkey'] = mkey
        if child_path is not None:
            params['child_path'] = child_path
        params.update(kwargs)
        return self._client.get("monitor", "/system/object/usage", params=params)


class Object:
    """Object operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Object endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.usage = Usage(client)
