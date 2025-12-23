"""
HTTP Client Interface (Protocol)

This module defines the Protocol interface for HTTP clients used by FortiOS API
endpoints.
Using a Protocol (PEP 544) allows for duck-typing and enables users to provide
custom
HTTP client implementations.

Benefits:
- Users can provide custom HTTP clients (with caching, custom auth, proxying,
etc.)
- Easier testing with lightweight fake/mock clients
- Type-safe client swapping
- Maintains backward compatibility

Example:
    class CustomHTTPClient:
        '''Custom client with company-specific requirements'''
        def get(self, api_type: str, path: str, **kwargs) -> Union[dict[str,
        Any], Coroutine[Any, Any, dict[str, Any]]]:
            # Custom implementation with logging, auth, etc.
            ...

        def post(self, api_type: str, path: str, data: dict, **kwargs) ->
        Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
            # Custom implementation
            ...

        # ... put, delete

    # Use custom client
    fgt = FortiOS(host='...', token='...', client=CustomHTTPClient())
"""

from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Protocol,
    Union,
    runtime_checkable,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

__all__ = ["IHTTPClient"]


@runtime_checkable
class IHTTPClient(Protocol):
    """
    Protocol defining the interface for HTTP clients used by FortiOS endpoints.

    This protocol allows any class implementing these methods to be used as an
    HTTP client, enabling:
    - Custom HTTP client implementations
    - Easier testing with mock/fake clients
    - Support for both sync and async clients
    - Extension by library users

    Method signatures support both synchronous (returning dict) and
    asynchronous
    (returning Coroutine) implementations. The return type is Union to
    accommodate
    both modes.

    Implementations:
    - HTTPClient: Synchronous implementation using httpx.Client
    - AsyncHTTPClient: Asynchronous implementation using httpx.AsyncClient

    Note:
        All methods should handle vdom=False to skip VDOM parameter in
        requests.
        The raw_json parameter controls whether full API response is returned
        (True)
        or just the results section (False, default).
    """

    def get(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Perform GET request to retrieve resource(s) from the API.

        Args:
            api_type: API category (e.g., 'cmdb', 'monitor', 'log', 'service')
            path: Endpoint path (e.g., 'firewall/address',
            'firewall/address/web-server')
            params: Optional query parameters (filters, pagination, etc.)
            vdom: Virtual domain name, or False to skip VDOM parameter
            raw_json: If True, return full API response with metadata; if
            False, return only results

        Returns:
            dict: API response (sync mode) or Coroutine[dict] (async mode)

        Example (Sync):
            result = client.get("cmdb", "firewall/address/web-server")

        Example (Async):
            result = await client.get("cmdb", "firewall/address/web-server")
        """
        ...

    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Perform POST request to create new resource(s) in the API.

        Args:
            api_type: API category (e.g., 'cmdb', 'monitor', 'log', 'service')
            path: Endpoint path (e.g., 'firewall/address')
            data: Resource data to create
            params: Optional query parameters
            vdom: Virtual domain name, or False to skip VDOM parameter
            raw_json: If True, return full API response with metadata; if
            False, return only results

        Returns:
            dict: API response (sync mode) or Coroutine[dict] (async mode)

        Example (Sync):
            result = client.post("cmdb", "firewall/address", data={"name":
            "test", "subnet": "10.0.0.1/32"})

        Example (Async):
            result = await client.post("cmdb", "firewall/address", data={...})
        """
        ...

    def put(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Perform PUT request to update existing resource in the API.

        Args:
            api_type: API category (e.g., 'cmdb', 'monitor', 'log', 'service')
            path: Endpoint path with identifier (e.g.,
            'firewall/address/web-server')
            data: Updated resource data
            params: Optional query parameters
            vdom: Virtual domain name, or False to skip VDOM parameter
            raw_json: If True, return full API response with metadata; if
            False, return only results

        Returns:
            dict: API response (sync mode) or Coroutine[dict] (async mode)

        Example (Sync):
            result = client.put("cmdb", "firewall/address/web-server",
            data={"subnet": "10.0.0.2/32"})

        Example (Async):
            result = await client.put("cmdb", "firewall/address/web-server",
            data={...})
        """
        ...

    def delete(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Perform DELETE request to remove resource from the API.

        Args:
            api_type: API category (e.g., 'cmdb', 'monitor', 'log', 'service')
            path: Endpoint path with identifier (e.g.,
            'firewall/address/web-server')
            params: Optional query parameters
            vdom: Virtual domain name, or False to skip VDOM parameter
            raw_json: If True, return full API response with metadata; if
            False, return only results

        Returns:
            dict: API response (sync mode) or Coroutine[dict] (async mode)

        Example (Sync):
            result = client.delete("cmdb", "firewall/address/web-server")

        Example (Async):
            result = await client.delete("cmdb", "firewall/address/web-server")
        """
        ...

    # Optional methods for additional functionality
    # These are not required for basic HTTP client implementation
    # but are provided by the built-in HTTPClient and AsyncHTTPClient

    def close(self) -> Union[None, Coroutine[Any, Any, None]]:
        """
        Close the HTTP client and release resources.

        Returns:
            None (sync clients) or Coroutine[None] (async clients)

        Optional method - not required for basic protocol compliance.
        Custom clients may implement this for resource cleanup.

        Example (Sync):
            client.close()

        Example (Async):
            await client.close()
        """
        ...

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get connection statistics.

        Optional method - not required for basic protocol compliance.
        Returns statistics about HTTP connections if supported.

        Returns:
            Dictionary with connection pool metrics (if available)
        """
        ...

    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all API operations.

        Optional method - not required for basic protocol compliance.
        Only available when operation tracking is enabled.

        Returns:
            List of all API operations with timestamps and details
        """
        ...

    def get_write_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of write operations (POST/PUT/DELETE).

        Optional method - not required for basic protocol compliance.
        Only available when operation tracking is enabled.

        Returns:
            List of write operations with timestamps and details
        """
        ...

    def get_health_metrics(self) -> dict[str, Any]:
        """
        Get health metrics and performance indicators.

        Optional method - not required for basic protocol compliance.
        Only available when adaptive retry is enabled.

        Returns:
            Dictionary with health metrics (response times, backpressure, etc.)
        """
        ...

    def get_binary(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
    ) -> Union[bytes, Coroutine[Any, Any, bytes]]:
        """
        GET request returning binary data (for file downloads).

        Args:
            api_type: API category (e.g., 'cmdb', 'monitor', 'log')
            path: Endpoint path
            params: Optional query parameters
            vdom: Virtual domain name, or False to skip VDOM parameter

        Returns:
            Raw binary response data (bytes)
        """
        ...
