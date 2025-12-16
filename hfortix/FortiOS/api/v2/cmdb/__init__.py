"""
FortiOS CMDB API
Configuration Management Database endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

__all__ = ["CMDB"]


class CMDB:
    """
    CMDB API helper class
    Provides access to FortiOS configuration endpoints

    Attributes:
        alertemail: Alert email configuration
        antivirus: Antivirus profiles and settings
        application: Application control lists
        authentication: Authentication rules and settings
        automation: Automation stitches and actions
        casb: Cloud Access Security Broker
        certificate: Certificate management
        diameter_filter: Diameter filter profiles
        dlp: Data Loss Prevention
        dnsfilter: DNS filtering profiles
        emailfilter: Email filter profiles
        endpoint_control: Endpoint control settings
        ethernet_oam: Ethernet OAM settings
        extension_controller: Extension controller
        file_filter: File filtering profiles
        firewall: Firewall policies and objects
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize CMDB helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .alertemail import AlertEmail
        from .antivirus import Antivirus
        from .application import Application
        from .authentication import Authentication
        from .automation import Automation
        from .casb import Casb
        from .certificate import Certificate
        from .diameter_filter import DiameterFilter
        from .dlp import DLP
        from .dnsfilter import DNSFilter
        from .emailfilter import EmailFilter
        from .endpoint_control import EndpointControl
        from .ethernet_oam import EthernetOAM
        from .extension_controller import ExtensionController
        from .file_filter import FileFilter
        from .firewall import Firewall

        self.alertemail: AlertEmail = AlertEmail(client)
        self.antivirus: Antivirus = Antivirus(client)
        self.application: Application = Application(client)
        self.authentication: Authentication = Authentication(client)
        self.automation: Automation = Automation(client)
        self.casb: Casb = Casb(client)
        self.certificate: Certificate = Certificate(client)
        self.diameter_filter: DiameterFilter = DiameterFilter(client)
        self.dlp: DLP = DLP(client)
        self.dnsfilter: DNSFilter = DNSFilter(client)
        self.emailfilter: EmailFilter = EmailFilter(client)
        self.endpoint_control: EndpointControl = EndpointControl(client)
        self.ethernet_oam: EthernetOAM = EthernetOAM(client)
        self.extension_controller: ExtensionController = ExtensionController(client)
        self.file_filter: FileFilter = FileFilter(client)
        self.firewall: Firewall = Firewall(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "alertemail",
            "antivirus",
            "application",
            "authentication",
            "automation",
            "casb",
            "certificate",
            "diameter_filter",
            "dlp",
            "dnsfilter",
            "emailfilter",
            "endpoint_control",
            "ethernet_oam",
            "extension_controller",
            "file_filter",
            "firewall",
        ]
