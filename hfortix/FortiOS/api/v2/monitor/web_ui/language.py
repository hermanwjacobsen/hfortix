"""Monitor API - Language operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ImportLanguage:
    """ImportLanguage operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ImportLanguage endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Import localization language file to this FortiGate.
        
        Args:
            file_content: Provided when uploading a file: base64 encoded file data. Must not contain whitespace or other invalid base64 characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.web_ui.language.import.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if file_content is not None:
            data['file_content'] = file_content
        data.update(kwargs)
        return self._client.post("monitor", "/web-ui/language/import", data=data)


class Language:
    """Language operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Language endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.import_language = ImportLanguage(client)
