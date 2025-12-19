"""Monitor API - Ca operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ImportCa:
    """ImportCa operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ImportCa endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        import_method: str | None = None,
        scep_url: str | None = None,
        scep_ca_id: str | None = None,
        scope: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Import CA certificate.
        
        Args:
            import_method: Method of importing CA certificate.[file|scep] (optional)
            scep_url: SCEP server URL. Required for import via SCEP (optional)
            scep_ca_id: SCEP server CA identifier for import via SCEP. (optional)
            scope: Scope of CA certificate [vdom*|global]. Global scope is only accessible for global administrators (optional)
            file_content: Provided when uploading a file: base64 encoded file data. Must not contain whitespace or other invalid base64 characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn_certificate.ca.import.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if import_method is not None:
            data['import_method'] = import_method
        if scep_url is not None:
            data['scep_url'] = scep_url
        if scep_ca_id is not None:
            data['scep_ca_id'] = scep_ca_id
        if scope is not None:
            data['scope'] = scope
        if file_content is not None:
            data['file_content'] = file_content
        data.update(kwargs)
        return self._client.post("monitor", "/vpn-certificate/ca/import", data=data)


class Ca:
    """Ca operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ca endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.import_ca = ImportCa(client)
