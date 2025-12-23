"""
FortiOS MONITOR - Monitor Registration Forticloud

Monitoring endpoint for monitor registration forticloud data.

API Endpoints:
    GET    /monitor/registration/forticloud

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.registration.forticloud.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.registration.forticloud.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class DeviceStatus:
    """
    Devicestatus Operations.

    Provides read-only access for FortiOS devicestatus data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DeviceStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        serials: list,
        update_cache: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Fetch device registration status from FortiCloud.

        Args:
            serials: Serials of FortiSwitch and FortiAP to fetch registration
            status. (required)
            update_cache: Clear cache and retrieve updated data. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.device_status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params["serials"] = serials
        if update_cache is not None:
            params["update_cache"] = update_cache
        params.update(kwargs)
        return self._client.get(
            "monitor", "/registration/forticloud/device-status", params=params
        )


class Disclaimer:
    """Disclaimer operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Disclaimer endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the FortiCloud disclaimer.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.disclaimer.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/registration/forticloud/disclaimer", params=params
        )


class Domains:
    """Domains operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Domains endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of FortiCloud login domains.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.domains.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/registration/forticloud/domains", params=params
        )


class Login:
    """Login operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Login endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        email: str | None = None,
        password: str | None = None,
        send_logs: bool | None = None,
        domain: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Login to FortiCloud.

        Args:
            email: Account email. (optional)
            password: Account password. (optional)
            send_logs: Send logs to FortiCloud. (optional)
            domain: FortiCloud domain. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.login.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        if send_logs is not None:
            data["send_logs"] = send_logs
        if domain is not None:
            data["domain"] = domain
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticloud/login", data=data
        )


class Logout:
    """Logout operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Logout endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Logout from FortiCloud.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.logout.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticloud/logout", data=data
        )


class Migrate:
    """Migrate operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Migrate endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        email: str | None = None,
        password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Migrate standalone FortiGate Cloud account to FortiCloud.

        Args:
            email: Account email. (optional)
            password: Account password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.migrate.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticloud/migrate", data=data
        )


class RegisterDevice:
    """RegisterDevice operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RegisterDevice endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        serial: str | None = None,
        email: str | None = None,
        password: str | None = None,
        reseller: str | None = None,
        reseller_id: int | None = None,
        country: str | None = None,
        is_government: bool | None = None,
        agreement_accepted: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Register a device to FortiCloud through FortiGate.

        Args:
            serial: Device serial number (optional)
            email: FortiCloud email. (optional)
            password: Password. (optional)
            reseller: Reseller. (optional)
            reseller_id: Reseller ID. (optional)
            country: Country. (optional)
            is_government: Set to true if the end-user is affiliated with a
            government. (optional)
            agreement_accepted: Set to true if the end-user accepted the
            agreement. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticloud.register_device.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serial is not None:
            data["serial"] = serial
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        if reseller is not None:
            data["reseller"] = reseller
        if reseller_id is not None:
            data["reseller_id"] = reseller_id
        if country is not None:
            data["country"] = country
        if is_government is not None:
            data["is_government"] = is_government
        if agreement_accepted is not None:
            data["agreement_accepted"] = agreement_accepted
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticloud/register-device", data=data
        )


class Forticloud:
    """Forticloud operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Forticloud endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.device_status = DeviceStatus(client)
        self.disclaimer = Disclaimer(client)
        self.domains = Domains(client)
        self.login = Login(client)
        self.logout = Logout(client)
        self.migrate = Migrate(client)
        self.register_device = RegisterDevice(client)
