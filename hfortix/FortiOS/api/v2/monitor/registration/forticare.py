"""
FortiOS MONITOR - Monitor Registration Forticare

Monitoring endpoint for monitor registration forticare data.

API Endpoints:
    GET    /monitor/registration/forticare

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.registration.forticare.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.registration.forticare.get(
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


class AddLicense:
    """
    Addlicense Operations.

    Provides read-only access for FortiOS addlicense data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AddLicense endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        registration_code: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Add a FortiCare license.

        Args:
            registration_code: FortiCare contract number. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.add_license.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if registration_code is not None:
            data["registration_code"] = registration_code
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticare/add-license", data=data
        )


class CheckConnectivity:
    """CheckConnectivity operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CheckConnectivity endpoint.

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
        Check connectivity to FortiCare servers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.check_connectivity.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/registration/forticare/check-connectivity",
            params=params,
        )


class Create:
    """Create operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Create endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        email: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        title: str | None = None,
        company: str | None = None,
        address: str | None = None,
        city: str | None = None,
        country_code: int | None = None,
        state: str | None = None,
        state_code: str | None = None,
        postal_code: str | None = None,
        phone: str | None = None,
        industry: str | None = None,
        industry_id: int | None = None,
        orgsize_id: int | None = None,
        reseller_name: str | None = None,
        reseller_id: int | None = None,
        is_government: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create a new FortiCare account.

        Args:
            email: Account email. (optional)
            password: Account password. (optional)
            first_name: First name. (optional)
            last_name: Last name. (optional)
            title: Title. (optional)
            company: Company. (optional)
            address: Address. (optional)
            city: City. (optional)
            country_code: Country code. (optional)
            state: State/Province. (optional)
            state_code: State/Province code. (optional)
            postal_code: Postal code. (optional)
            phone: Phone number. (optional)
            industry: Industry. (optional)
            industry_id: Industry ID. (optional)
            orgsize_id: Organization size ID. (optional)
            reseller_name: Reseller name. (optional)
            reseller_id: Reseller ID. (optional)
            is_government: Set to true if the end-user is affiliated with a
            government. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.create.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if title is not None:
            data["title"] = title
        if company is not None:
            data["company"] = company
        if address is not None:
            data["address"] = address
        if city is not None:
            data["city"] = city
        if country_code is not None:
            data["country_code"] = country_code
        if state is not None:
            data["state"] = state
        if state_code is not None:
            data["state_code"] = state_code
        if postal_code is not None:
            data["postal_code"] = postal_code
        if phone is not None:
            data["phone"] = phone
        if industry is not None:
            data["industry"] = industry
        if industry_id is not None:
            data["industry_id"] = industry_id
        if orgsize_id is not None:
            data["orgsize_id"] = orgsize_id
        if reseller_name is not None:
            data["reseller_name"] = reseller_name
        if reseller_id is not None:
            data["reseller_id"] = reseller_id
        if is_government is not None:
            data["is_government"] = is_government
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticare/create", data=data
        )


class DeregisterDevice:
    """DeregisterDevice operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DeregisterDevice endpoint.

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
        Deregister the FortiGate from a FortiCare account.

        Args:
            email: FortiCare email. (optional)
            password: Account password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.deregister_device.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticare/deregister-device", data=data
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
        serial: str | None = None,
        email: str | None = None,
        password: str | None = None,
        reseller_name: str | None = None,
        reseller_id: int | None = None,
        agreement_accepted: bool | None = None,
        is_government: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Login to FortiCare.

        Args:
            serial: Serial number of an HA cluster member to register to login
            to FortiCare. Current device will be selected if not set.
            (optional)
            email: Account email. (optional)
            password: Account password. (optional)
            reseller_name: Reseller name. (optional)
            reseller_id: Reseller ID. (optional)
            agreement_accepted: Set to true if the end-user accepted the
            agreement. (optional)
            is_government: Set to true if the end-user is affiliated with a
            government. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.login.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serial is not None:
            data["serial"] = serial
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        if reseller_name is not None:
            data["reseller_name"] = reseller_name
        if reseller_id is not None:
            data["reseller_id"] = reseller_id
        if agreement_accepted is not None:
            data["agreement_accepted"] = agreement_accepted
        if is_government is not None:
            data["is_government"] = is_government
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticare/login", data=data
        )


class Transfer:
    """Transfer operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Transfer endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        email: str | None = None,
        password: str | None = None,
        old_email: str | None = None,
        old_password: str | None = None,
        is_government: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Transfer to a new FortiCare account.

        Args:
            email: Account email. (optional)
            password: Account password. (optional)
            old_email: Old account email. (optional)
            old_password: Old account password. (optional)
            is_government: Set to true if the end-user is affiliated with a
            government. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.registration.forticare.transfer.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        if old_email is not None:
            data["old_email"] = old_email
        if old_password is not None:
            data["old_password"] = old_password
        if is_government is not None:
            data["is_government"] = is_government
        data.update(kwargs)
        return self._client.post(
            "monitor", "/registration/forticare/transfer", data=data
        )


class Forticare:
    """Forticare operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Forticare endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.add_license = AddLicense(client)
        self.check_connectivity = CheckConnectivity(client)
        self.create = Create(client)
        self.deregister_device = DeregisterDevice(client)
        self.login = Login(client)
        self.transfer = Transfer(client)
