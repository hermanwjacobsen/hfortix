"""
FortiOS MONITOR - Monitor Switch Controller Managed Switch

Monitoring endpoint for monitor switch controller managed switch data.

API Endpoints:
    GET    /monitor/switch_controller/managed_switch

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.switch_controller.managed_switch.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.switch_controller.managed_switch.get(
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


class Bios:
    """
    Bios Operations.

    Provides read-only access for FortiOS bios data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Bios endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get a list of BIOS info by managed FortiSwitches.

        Args:
            mkey: Filter: FortiSwitch ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.managed_switch.bios.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor", "/switch-controller/managed-switch/bios", params=params
        )


class BouncePort:
    """BouncePort operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize BouncePort endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        port: str | None = None,
        duration: int | None = None,
        stop: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset the port to force all connected clients to re-request DHCP lease.

        Args:
            mkey: FortiSwitch ID. (optional)
            port: FortiSwitch Port ID. (optional)
            duration: Duration in seconds from 1 to 5 for port to be down.
            Defaults to 1 second if not provided. (optional)
            stop: Stop a bounce in progress. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.bounce_port.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if port is not None:
            data["port"] = port
        if duration is not None:
            data["duration"] = duration
        if stop is not None:
            data["stop"] = stop
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/switch-controller/managed-switch/bounce-port",
            data=data,
        )


class CableStatus:
    """CableStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CableStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        port: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Diagnose cable information for a port.

        Args:
            mkey: Filter: FortiSwitch ID. (required)
            port: Name of managed FortiSwitch port. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.cable_status.get(mkey='value',
            port='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["port"] = port
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/cable-status",
            params=params,
        )


class DhcpSnooping:
    """DhcpSnooping operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DhcpSnooping endpoint.

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
        Retrieve DHCP servers monitored by FortiSwitches.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/dhcp-snooping",
            params=params,
        )


class FaceplateXml:
    """FaceplateXml operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize FaceplateXml endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve XML for rendering FortiSwitch faceplate widget.

        Args:
            mkey: Name of managed FortiSwitch. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.faceplate_xml.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/faceplate-xml",
            params=params,
        )


class FactoryReset:
    """FactoryReset operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize FactoryReset endpoint.

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
        Send 'Factory Reset' command to a given FortiSwitch.

        Args:
            mkey: Name of managed FortiSwitch. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.factory_reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/switch-controller/managed-switch/factory-reset",
            data=data,
        )


class HealthStatus:
    """HealthStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HealthStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        serial: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve health-check statistics for managed FortiSwitches.

        Args:
            mkey: Filter: FortiSwitch ID. (optional)
            serial: Filter: FortiSwitch Serial. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.health_status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if serial is not None:
            params["serial"] = serial
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/health-status",
            params=params,
        )


class Models:
    """Models operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Models endpoint.

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
        Retrieve a list of FortiSwitch models that may be pre-configured.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.managed_switch.models.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/models",
            params=params,
        )


class PoeReset:
    """PoeReset operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PoeReset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        port: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset PoE on a given FortiSwitch's port.

        Args:
            mkey: Name of managed FortiSwitch. (optional)
            port: Name of port to reset PoE on. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.poe_reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if port is not None:
            data["port"] = port
        data.update(kwargs)
        return self._client.post(
            "monitor", "/switch-controller/managed-switch/poe-reset", data=data
        )


class PortHealth:
    """PortHealth operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PortHealth endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve port health statistics for managed FortiSwitches.

        Args:
            mkey: Filter: FortiSwitch ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.port_health.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/port-health",
            params=params,
        )


class PortStats:
    """PortStats operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PortStats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve port statistics for configured FortiSwitches.

        Args:
            mkey: Filter: FortiSwitch ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.port_stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/port-stats",
            params=params,
        )


class PortStatsReset:
    """PortStatsReset operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PortStatsReset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        ports: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset port statistics for a given FortiSwitch.

        Args:
            mkey: FortiSwitch ID. (optional)
            ports: Name of ports to reset statistics on. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if ports is not None:
            data["ports"] = ports
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/switch-controller/managed-switch/port-stats-reset",
            data=data,
        )


class Restart:
    """Restart operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Restart endpoint.

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
        Restart a given FortiSwitch.

        Args:
            mkey: Name of managed FortiSwitch. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.managed_switch.restart.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        data.update(kwargs)
        return self._client.post(
            "monitor", "/switch-controller/managed-switch/restart", data=data
        )


class Status:
    """Status operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve statistics for configured FortiSwitches.

        Args:
            mkey: Filter: FortiSwitch ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.managed_switch.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/status",
            params=params,
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
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get a list of transceivers being used by managed FortiSwitches.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.transceivers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/managed-switch/transceivers",
            params=params,
        )


class TxRx:
    """TxRx operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TxRx endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        port: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the transceiver Tx and Rx power for a specific port.

        Args:
            mkey: Filter: FortiSwitch ID. (required)
            port: Name of the port. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.managed_switch.tx_rx.get(mkey='value',
            port='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["port"] = port
        params.update(kwargs)
        return self._client.get(
            "monitor", "/switch-controller/managed-switch/tx-rx", params=params
        )


class Update:
    """Update operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        admin: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update administrative state for a given FortiSwitch (enable or disable
        authorization).

        Args:
            mkey: FortiSwitch name. (optional)
            admin: New FortiSwitch administrative state
            [enable|disable|discovered]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.managed_switch.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if admin is not None:
            data["admin"] = admin
        data.update(kwargs)
        return self._client.post(
            "monitor", "/switch-controller/managed-switch/update", data=data
        )


class ManagedSwitch:
    """ManagedSwitch operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ManagedSwitch endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.bios = Bios(client)
        self.bounce_port = BouncePort(client)
        self.cable_status = CableStatus(client)
        self.dhcp_snooping = DhcpSnooping(client)
        self.faceplate_xml = FaceplateXml(client)
        self.factory_reset = FactoryReset(client)
        self.health_status = HealthStatus(client)
        self.models = Models(client)
        self.poe_reset = PoeReset(client)
        self.port_health = PortHealth(client)
        self.port_stats = PortStats(client)
        self.port_stats_reset = PortStatsReset(client)
        self.restart = Restart(client)
        self.status = Status(client)
        self.transceivers = Transceivers(client)
        self.tx_rx = TxRx(client)
        self.update = Update(client)
