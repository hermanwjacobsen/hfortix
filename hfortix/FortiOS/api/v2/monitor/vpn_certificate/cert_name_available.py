"""Monitor API - CertNameAvailable operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class CertNameAvailable:
    """CertNameAvailable operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CertNameAvailable endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Check if the local certificate name is available to use.
        
        Args:
            mkey: The certificate name to be checked. (required)
            scope: Scope of certificate name [vdom*|global]. Global scope is only accessible for global administrators (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn_certificate.cert_name_available.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/vpn-certificate/cert-name-available", params=params)
