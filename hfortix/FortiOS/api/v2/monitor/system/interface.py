"""
FortiOS MONITOR - Monitor System Interface

Monitoring endpoint for monitor system interface data.

API Endpoints:
    GET    /monitor/system/interface

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.interface.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.interface.get(
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


class DhcpRenew:
    """
    Dhcprenew Operations.

    Provides read-only access for FortiOS dhcprenew data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DhcpRenew endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Renew DHCP lease of an interface.

        Args:
            mkey: Name of the interface. (optional)
            ipv6: Renew the DHCPv6 lease. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.dhcp_renew.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if ipv6 is not None:
            data["ipv6"] = ipv6
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/interface/dhcp-renew", data=data
        )


class DhcpStatus:
    """DhcpStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DhcpStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the DHCP client status of an interface.

        Args:
            mkey: Name of the interface. (required)
            ipv6: Retrieve the DHCPv6 client status. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.dhcp_status.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        if ipv6 is not None:
            params["ipv6"] = ipv6
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/dhcp-status", params=params
        )


class KernelInterfaces:
    """KernelInterfaces operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize KernelInterfaces endpoint.

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
        Retrieve a list of kernel interfaces.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.kernel_interfaces.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/kernel-interfaces", params=params
        )


class Poe:
    """Poe operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Poe endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve PoE statistics for system interfaces.

        Args:
            mkey: Filter: Name of the interface to fetch PoE statistics for.
            (optional)
            scope: Scope from which to retrieve the interface stats from
            [vdom|global] (default=vdom). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.poe.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/poe", params=params
        )


class PoeUsage:
    """PoeUsage operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PoeUsage endpoint.

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
        Retrieve PoE usage stats across all VDOMs.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.poe_usage.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/poe-usage", params=params
        )


class SpeedTestStatus:
    """SpeedTestStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SpeedTestStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        id: int,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the current status of a speed-test with the results if
        finished.

        Args:
            id: ID of the speed test. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.speed_test_status.get(id=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["id"] = id
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/speed-test-status", params=params
        )


class SpeedTestTrigger:
    """SpeedTestTrigger operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SpeedTestTrigger endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Run a speed-test on the given interface.

        Args:
            mkey: Name of the interface. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.speed_test_trigger.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/interface/speed-test-trigger", data=data
        )


class Transceivers:
    """Transceivers operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Transceivers endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get a list of transceivers being used by the FortiGate.

        Args:
            scope: Scope from which to retrieve the transceiver information
            from [vdom|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.transceivers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface/transceivers", params=params
        )


class WakeOnLan:
    """WakeOnLan operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize WakeOnLan endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        mac: str | None = None,
        protocol_option: str | None = None,
        port: int | None = None,
        address: str | None = None,
        secureon_password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Send wake on lan packet to device.

        Args:
            mkey: Name of the interface that will send out the packet.
            (optional)
            mac: MAC of device to wake up. (optional)
            protocol_option: protocol [wol | udp]. Default is udp (optional)
            port: Port used by UDP WoL packets (0, 7, or 9). Port 9 will be
            used by default. (optional)
            address: Broadcast IP address used by UDP WoL packets. (optional)
            secureon_password: Password of the destination host if SecureOn is
            enabled. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.wake_on_lan.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if mac is not None:
            data["mac"] = mac
        if protocol_option is not None:
            data["protocol_option"] = protocol_option
        if port is not None:
            data["port"] = port
        if address is not None:
            data["address"] = address
        if secureon_password is not None:
            data["secureon_password"] = secureon_password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/interface/wake-on-lan", data=data
        )


class Interface:
    """Interface operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Interface endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.dhcp_renew = DhcpRenew(client)
        self.dhcp_status = DhcpStatus(client)
        self.kernel_interfaces = KernelInterfaces(client)
        self.poe = Poe(client)
        self.poe_usage = PoeUsage(client)
        self.speed_test_status = SpeedTestStatus(client)
        self.speed_test_trigger = SpeedTestTrigger(client)
        self.transceivers = Transceivers(client)
        self.wake_on_lan = WakeOnLan(client)

    def get(
        self,
        interface_name: str | None = None,
        include_vlan: bool | None = None,
        include_aggregate: bool | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve statistics for all system interfaces.

        Args:
            interface_name: Filter: interface name. (optional)
            include_vlan: Enable to include VLANs in result list. (optional)
            include_aggregate: Enable to include Aggregate interfaces in result
            list. (optional)
            scope: Scope from which to retrieve the interface stats from
            [vdom|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.interface.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if interface_name is not None:
            params["interface_name"] = interface_name
        if include_vlan is not None:
            params["include_vlan"] = include_vlan
        if include_aggregate is not None:
            params["include_aggregate"] = include_aggregate
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/system/interface", params=params)
