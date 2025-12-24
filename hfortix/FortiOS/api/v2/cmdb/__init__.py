"""
FortiOS CMDB (Configuration Management Database) API

The CMDB API provides access to FortiOS configuration objects. Use these
endpoints
to create, read, update, and delete (CRUD) configuration items.

Key HTTP Methods:
    - GET: Retrieve configuration (list all or get specific item)
    - POST: Create new configuration objects
    - PUT: Update existing configuration objects
    - DELETE: Remove configuration objects

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Access CMDB endpoints via: fgt.api.cmdb
    >>>
    >>> # Firewall operations
    >>> fgt.api.cmdb.firewall.address.get()           # List addresses
    >>> fgt.api.cmdb.firewall.policy.post(...)        # Create policy
    >>> fgt.api.cmdb.firewall.address.put(name=...)   # Update address
    >>> fgt.api.cmdb.firewall.address.delete(name...) # Delete address
    >>>
    >>> # System operations
    >>> fgt.api.cmdb.system.interface.get(name="port1")
    >>> fgt.api.cmdb.system.admin.get()
    >>>
    >>> # Router operations
    >>> fgt.api.cmdb.router.static.get()
    >>> fgt.api.cmdb.router.bgp.put(...)

Available Endpoints:
    See the attributes list below for all available configuration categories.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

__all__ = ["CMDB"]


class CMDB:
    """
    FortiOS CMDB (Configuration Management Database) API.

    Provides access to FortiOS configuration endpoints for managing firewall
    policies,
    system settings, routing, VPN, logging, and more.

    Common Operations:
        - **Firewall**: Policies, addresses, services, VIPs, NAT
        - **System**: Interfaces, admins, DNS, NTP, HA, certificates
        - **Router**: Static routes, BGP, OSPF, policy routing
        - **VPN**: IPsec, SSL-VPN, certificates
        - **Security Profiles**: Antivirus, IPS, web filtering, DLP
        - **User**: User accounts, authentication, LDAP, RADIUS

    HTTP Methods by Operation:
        - **GET**: List/retrieve configuration (no changes)
        - **POST**: Create new objects (returns 404 if name already exists)
        - **PUT**: Update existing objects (returns 404 if name doesn't exist)
        - **DELETE**: Remove objects (returns 404 if name doesn't exist)

    Attributes:
        alertemail: Alert email configuration
        antivirus: Antivirus profiles and settings
        application: Application control lists and signatures
        authentication: Authentication rules and schemes
        automation: Automation stitches, actions, and triggers
        casb: Cloud Access Security Broker profiles
        certificate: Certificate management (CA, CRL, local, remote)
        diameter_filter: Diameter filter profiles
        dlp: Data Loss Prevention sensors and profiles
        dnsfilter: DNS filtering profiles and domains
        emailfilter: Email filter profiles and settings
        endpoint_control: Endpoint control configuration
        ethernet_oam: Ethernet OAM (Operations, Administration, Maintenance)
        extension_controller: Extension controller for FortiExtender
        file_filter: File filtering profiles
        firewall: Firewall policies, addresses, services, VIPs, NAT, schedules
        ftp_proxy: FTP proxy configuration
        icap: ICAP (Internet Content Adaptation Protocol) profiles
        ips: Intrusion Prevention System sensors and signatures
        log: Logging configuration (disk, FortiAnalyzer, syslog, memory)
        monitoring: Monitoring and NPU HPE configuration
        report: Report configuration and layouts
        router: Routing configuration (BGP, OSPF, static routes, RIP, IS-IS,
        multicast)
        rule: Detection rules (FMWP, IoT, OT device detection)
        sctp_filter: SCTP (Stream Control Transmission Protocol) filter
        profiles
        switch_controller: Managed switch configuration
        system: System settings (interfaces, admins, DNS, NTP, HA, SNMP, VDOM)
        user: User authentication (local, LDAP, RADIUS, TACACS+, SAML,
        certificates)
        videofilter: Video filtering (YouTube, Vimeo categories)
        virtual_patch: Virtual patching profiles for vulnerability protection
        voip: VoIP profiles (SIP, SCCP)
        vpn: VPN configuration (IPsec, SSL-VPN, L2TP, PPTP, certificates)
        waf: Web Application Firewall profiles and signatures
        web_proxy: Web proxy configuration
        webfilter: Web filtering profiles and URL filters
        wireless_controller: Wireless controller for FortiAP management
        ztna: Zero Trust Network Access configuration

    Example:
        >>> from hfortix.FortiOS import FortiOS
        >>> fgt = FortiOS(host="192.168.1.99", token="your-token")
        >>>
        >>> # Create firewall address (POST for new objects)
        >>> fgt.api.cmdb.firewall.address.post(
        ...     name="Server01",
        ...     subnet="192.168.100.10/32"
        ... )
        >>>
        >>> # Update firewall address (PUT for existing objects)
        >>> fgt.api.cmdb.firewall.address.put(
        ...     name="Server01",
        ...     subnet="192.168.100.20/32"
        ... )
        >>>
        >>> # Get specific address
        >>> addr = fgt.api.cmdb.firewall.address.get(name="Server01")
        >>>
        >>> # List all addresses
        >>> all_addrs = fgt.api.cmdb.firewall.address.get()
        >>>
        >>> # Delete address
        >>> fgt.api.cmdb.firewall.address.delete(name="Server01")
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize CMDB helper

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoint classes
        from importlib import import_module

        from .alertemail import Alertemail
        from .antivirus import Antivirus
        from .application import Application
        from .authentication import Authentication
        from .automation import Automation
        from .casb import Casb
        from .certificate import Certificate

        diameter_filter_mod = import_module(
            ".diameter_filter", "hfortix.FortiOS.api.v2.cmdb"
        )
        from .dlp import Dlp
        from .dnsfilter import Dnsfilter
        from .emailfilter import Emailfilter

        endpoint_control_mod = import_module(
            ".endpoint_control", "hfortix.FortiOS.api.v2.cmdb"
        )
        ethernet_oam_mod = import_module(
            ".ethernet_oam", "hfortix.FortiOS.api.v2.cmdb"
        )
        extension_controller_mod = import_module(
            ".extension_controller", "hfortix.FortiOS.api.v2.cmdb"
        )
        file_filter_mod = import_module(
            ".file_filter", "hfortix.FortiOS.api.v2.cmdb"
        )
        from .firewall import Firewall

        ftp_proxy_mod = import_module(
            ".ftp_proxy", "hfortix.FortiOS.api.v2.cmdb"
        )
        from .icap import Icap
        from .ips import Ips
        from .log import Log
        from .monitoring import Monitoring
        from .report import Report
        from .router import Router
        from .rule import Rule

        sctp_filter_mod = import_module(
            ".sctp_filter", "hfortix.FortiOS.api.v2.cmdb"
        )
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
        self.extension_controller = (
            extension_controller_mod.ExtensionController(client)
        )
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
