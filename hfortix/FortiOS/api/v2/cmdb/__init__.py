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
        ftp_proxy: FTP proxy settings
        icap: ICAP profiles and servers
        ips: Intrusion Prevention System
        log: Logging configuration
        monitoring: Monitoring configuration
        report: Report configuration and layouts
        router: Router configuration (BGP, OSPF, static routes, etc.)
        rule: Rule signatures (FMWP, IOT, OT detection)
        sctp_filter: SCTP filter profiles
        system: System configuration (interface, admin, DNS, NTP, HA, SNMP, etc.)
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize CMDB helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .alertemail import Alertemail
        from .antivirus import Antivirus
        from .application import Application
        from .authentication import Authentication
        from .automation import Automation
        from .casb import Casb
        from .certificate import Certificate
        from importlib import import_module
        diameter_filter_mod = import_module('.diameter-filter', 'hfortix.FortiOS.api.v2.cmdb')
        from .dlp import Dlp
        from .dnsfilter import Dnsfilter
        from .emailfilter import Emailfilter
        endpoint_control_mod = import_module('.endpoint-control', 'hfortix.FortiOS.api.v2.cmdb')
        ethernet_oam_mod = import_module('.ethernet-oam', 'hfortix.FortiOS.api.v2.cmdb')
        extension_controller_mod = import_module('.extension-controller', 'hfortix.FortiOS.api.v2.cmdb')
        file_filter_mod = import_module('.file-filter', 'hfortix.FortiOS.api.v2.cmdb')
        from .firewall import Firewall
        ftp_proxy_mod = import_module('.ftp-proxy', 'hfortix.FortiOS.api.v2.cmdb')
        from .icap import Icap
        from .ips import Ips
        from .log import Log
        from .monitoring import Monitoring
        from .report import Report
        from .router import Router
        from .rule import Rule
        sctp_filter_mod = import_module('.sctp-filter', 'hfortix.FortiOS.api.v2.cmdb')
        from .system import System

        self.alertemail = Alertemail(client)
        self.antivirus = Antivirus(client)
        self.application = Application(client)
        self.authentication = Authentication(client)
        self.automation = Automation(client)
        self.casb = Casb(client)
        self.certificate = Certificate(client)
        self.diameter_filter = diameter_filter_mod.DiameterFilter(client)
        self.dlp = Dlp(client)
        self.dnsfilter = Dnsfilter(client)
        self.emailfilter = Emailfilter(client)
        self.endpoint_control = endpoint_control_mod.EndpointControl(client)
        self.ethernet_oam = ethernet_oam_mod.EthernetOam(client)
        self.extension_controller = extension_controller_mod.ExtensionController(client)
        self.file_filter = file_filter_mod.FileFilter(client)
        self.firewall = Firewall(client)
        self.ftp_proxy = ftp_proxy_mod.FtpProxy(client)
        self.icap = Icap(client)
        self.ips = Ips(client)
        self.log = Log(client)
        self.monitoring = Monitoring(client)
        self.report = Report(client)
        self.router = Router(client)
        self.rule = Rule(client)
        self.sctp_filter = sctp_filter_mod.SctpFilter(client)
        self.system = System(client)

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
            "ftp_proxy",
            "icap",
            "ips",
            "log",
            "monitoring",
            "report",
            "router",
            "rule",
            "sctp_filter",
            "system",
        ]
