"""Monitor API - AcmeCertificateStatus operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class AcmeCertificateStatus:
    """AcmeCertificateStatus operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AcmeCertificateStatus endpoint.

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
        Get ACME certificate status.
        
        Args:
            mkey: Check if specific certificate is available. (required)
            scope: Scope of certificate [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.acme_certificate_status.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/system/acme-certificate-status", params=params)
