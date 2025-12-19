"""Monitor API - Database operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Upgrade:
    """Upgrade operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Upgrade endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        db_name: str | None = None,
        confirm_not_signed: bool | None = None,
        confirm_not_ga_certified: bool | None = None,
        file_id: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Upgrade or downgrade UTM engine or signature package (IPS/AntiVirus/Application Control/Industrial database/Security Rating/Internet Service Database) using uploaded file.
        
        Args:
            db_name: Security service database name [ips|appctrl|industrial_db|antivirus|security_rating|isdb|iotddb] (optional)
            confirm_not_signed: Confirm whether unsigned pkg files may be uploaded. (optional)
            confirm_not_ga_certified: Confirm whether non GA-certified pkg files may be uploaded. (optional)
            file_id: File id of existing pkg file from a previous upload. (optional)
            file_content: Provided when uploading a file: base64 encoded file data. Must not contain whitespace or other invalid base64 characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.license.database.upgrade.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if db_name is not None:
            data['db_name'] = db_name
        if confirm_not_signed is not None:
            data['confirm_not_signed'] = confirm_not_signed
        if confirm_not_ga_certified is not None:
            data['confirm_not_ga_certified'] = confirm_not_ga_certified
        if file_id is not None:
            data['file_id'] = file_id
        if file_content is not None:
            data['file_content'] = file_content
        data.update(kwargs)
        return self._client.post("monitor", "/license/database/upgrade", data=data)


class Database:
    """Database operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Database endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.upgrade = Upgrade(client)
