"""
FortiOS Monitor API v2

Real-time monitoring, status, and operational endpoints.

Monitor API endpoints are read-only or action-based operations that don't
modify configuration. They provide real-time status, statistics, and
operational commands.

Implemented categories (6/29):
- azure/ - Azure SDN connector operations
- casb/ - CASB (Cloud Access Security Broker) operations
- endpoint_control/ - FortiClient endpoint monitoring and management
- extender_controller/ - FortiExtender monitoring and management
- extension_controller/ - FortiGate LAN Extension monitoring
- firewall/ - Firewall monitoring, policies, sessions, and statistics
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient

__all__ = ["Monitor"]


class Monitor:
    """
    Monitor API handler.

    Provides access to FortiOS monitoring and operational endpoints.

    Available categories:
        - azure: Azure SDN connector operations
        - casb: CASB operations
        - endpoint_control: FortiClient endpoint monitoring
        - extender_controller: FortiExtender monitoring
        - extension_controller: FortiGate LAN Extension monitoring
        - firewall: Firewall monitoring, policies, sessions, and statistics

    Example:
        >>> # List Azure applications
        >>> apps = client.monitor.azure.application_list.list()

        >>> # Get CASB SaaS application details
        >>> details = client.monitor.casb.saas_application.details(mkey="Salesforce")

        >>> # Get endpoint summary
        >>> summary = client.monitor.endpoint_control.summary()

        >>> # List FortiExtenders
        >>> extenders = client.monitor.extender_controller.list()

        >>> # Get LAN Extension VDOM status
        >>> status = client.monitor.extension_controller.lan_extension_vdom.status()

        >>> # Get firewall policy statistics
        >>> policies = client.monitor.firewall.policy.list()

        >>> # List active sessions
        >>> sessions = client.monitor.firewall.sessions.list(srcaddr='10.1.1.100')
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Monitor API handler.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._azure = None
        self._casb = None
        self._endpoint_control = None
        self._extender_controller = None
        self._extension_controller = None
        self._firewall = None

    @property
    def azure(self):
        """Azure SDN connector operations."""
        if self._azure is None:
            from .azure import Azure

            self._azure = Azure(self._client)
        return self._azure

    @property
    def casb(self):
        """CASB (Cloud Access Security Broker) operations."""
        if self._casb is None:
            from .casb import Casb

            self._casb = Casb(self._client)
        return self._casb

    @property
    def endpoint_control(self):
        """FortiClient endpoint monitoring and management."""
        if self._endpoint_control is None:
            from .endpoint_control import EndpointControl

            self._endpoint_control = EndpointControl(self._client)
        return self._endpoint_control

    @property
    def extender_controller(self):
        """FortiExtender monitoring and management."""
        if self._extender_controller is None:
            from .extender_controller import ExtenderController

            self._extender_controller = ExtenderController(self._client)
        return self._extender_controller

    @property
    def extension_controller(self):
        """FortiGate LAN Extension monitoring."""
        if self._extension_controller is None:
            from .extension_controller import ExtensionController

            self._extension_controller = ExtensionController(self._client)
        return self._extension_controller

    @property
    def firewall(self):
        """Firewall monitoring, policies, sessions, and statistics."""
        if self._firewall is None:
            from .firewall import Firewall

            self._firewall = Firewall(self._client)
        return self._firewall

    def __dir__(self):
        """Control autocomplete to show available attributes"""
        return [
            "azure",
            "casb",
            "endpoint_control",
            "extender_controller",
            "extension_controller",
            "firewall",
        ]
