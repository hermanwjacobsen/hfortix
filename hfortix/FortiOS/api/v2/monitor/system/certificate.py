"""Monitor API - Certificate operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Download:
    """Download operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        type: str,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download certificate.
        
        Args:
            mkey: Name of certificate. (required)
            type: Type of certificate [local-cer|remote-cer|local-ca|remote-ca|local-csr|crl]. (required)
            scope: Scope of certificate [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.certificate.download.get(mkey='value', type='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params['type'] = type
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/system/certificate/download", params=params)


class ReadInfo:
    """ReadInfo operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ReadInfo endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        value: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get certificate information from a certificate string.
        
        Args:
            value: PEM formatted certificate. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.certificate.read_info.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if value is not None:
            data['value'] = value
        data.update(kwargs)
        return self._client.post("monitor", "/system/certificate/read-info", data=data)


class Certificate:
    """Certificate operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Certificate endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
        self.read_info = ReadInfo(client)
