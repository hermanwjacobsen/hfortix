"""Monitor API - Guest operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Email:
    """Email operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Email endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        group: str | None = None,
        guest: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Sent guest login details via email.
        
        Args:
            group: Guest group name. (optional)
            guest: Guest user IDs. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.guest.email.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if group is not None:
            data['group'] = group
        if guest is not None:
            data['guest'] = guest
        data.update(kwargs)
        return self._client.post("monitor", "/user/guest/email", data=data)


class Sms:
    """Sms operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Sms endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        group: str | None = None,
        guest: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Sent guest login details via SMS.
        
        Args:
            group: Guest group name. (optional)
            guest: Guest user IDs. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.guest.sms.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if group is not None:
            data['group'] = group
        if guest is not None:
            data['guest'] = guest
        data.update(kwargs)
        return self._client.post("monitor", "/user/guest/sms", data=data)


class Guest:
    """Guest operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Guest endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.email = Email(client)
        self.sms = Sms(client)
