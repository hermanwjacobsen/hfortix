"""
FortiOS Monitor API v2

Real-time monitoring, status, and operational endpoints.

Monitor API endpoints are read-only or action-based operations that don't
modify configuration. They provide real-time status, statistics, and
operational commands.

Implemented categories (32/32):
- azure/ - Azure SDN connector operations
- casb/ - CASB operations
- endpoint_control/ - FortiClient endpoint monitoring
- extender_controller/ - FortiExtender monitoring
- extension_controller/ - FortiGate LAN Extension monitoring
- firewall/ - Firewall monitoring, policies, sessions, and statistics
- firmware/ - Firmware upgrade operations
- fortiguard/ - FortiGuard service operations
- fortiview/ - FortiView statistics
- geoip/ - GeoIP lookup operations
- ips/ - IPS monitoring
- license/ - License status
- log/ - Log device operations
- network/ - Network monitoring
- registration/ - Device registration
- router/ - Router monitoring and BGP/OSPF operations
- sdwan/ - SD-WAN monitoring
- service/ - Service monitoring
- switch_controller/ - FortiSwitch controller monitoring
- system/ - System monitoring, status, and diagnostics
- user/ - User authentication and monitoring
- utm/ - UTM monitoring
- videofilter/ - Video filter monitoring
- virtual_wan/ - Virtual WAN monitoring
- vpn/ - VPN monitoring (IPsec/SSL)
- vpn_certificate/ - VPN certificate monitoring
- wanopt/ - WAN optimization monitoring
- web_ui/ - Web UI customization
- webcache/ - Web cache monitoring
- webfilter/ - Web filter monitoring
- webproxy/ - Web proxy monitoring
- wifi/ - WiFi controller and AP monitoring
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

    from .azure import Azure
    from .casb import Casb
    from .endpoint_control import EndpointControl
    from .extender_controller import ExtenderController
    from .extension_controller import ExtensionController
    from .firewall import Firewall
    from .firmware import Firmware
    from .fortiguard import Fortiguard
    from .fortiview import Fortiview
    from .geoip import Geoip
    from .ips import Ips
    from .license import License
    from .log import Log
    from .network import Network
    from .registration import Registration
    from .router import Router
    from .sdwan import Sdwan
    from .service import Service
    from .switch_controller import SwitchController
    from .system import System
    from .user import User
    from .utm import Utm
    from .videofilter import Videofilter
    from .virtual_wan import VirtualWan
    from .vpn import Vpn
    from .vpn_certificate import VpnCertificate
    from .wanopt import Wanopt
    from .web_ui import WebUi
    from .webcache import Webcache
    from .webfilter import Webfilter
    from .webproxy import Webproxy
    from .wifi import Wifi

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
        - firmware: Firmware upgrade operations
        - fortiguard: FortiGuard service operations
        - fortiview: FortiView statistics
        - geoip: GeoIP lookup operations
        - ips: IPS monitoring
        - license: License status
        - log: Log device operations
        - network: Network monitoring
        - registration: Device registration
        - router: Router monitoring and BGP/OSPF operations
        - sdwan: SD-WAN monitoring
        - service: Service monitoring
        - switch_controller: FortiSwitch controller monitoring
        - system: System monitoring, status, and diagnostics
        - user: User authentication and monitoring
        - utm: UTM monitoring
        - videofilter: Video filter monitoring
        - virtual_wan: Virtual WAN monitoring
        - vpn: VPN monitoring (IPsec/SSL)
        - vpn_certificate: VPN certificate monitoring
        - wanopt: WAN optimization monitoring
        - web_ui: Web UI customization
        - webcache: Web cache monitoring
        - webfilter: Web filter monitoring
        - webproxy: Web proxy monitoring
        - wifi: WiFi controller and AP monitoring

    Example:
        >>> # List Azure applications
        >>> apps = client.monitor.azure.application_list.list()

        >>> # Get firewall policy statistics
        >>> policies = client.monitor.firewall.policy.list()

        >>> # List active sessions
        >>> sessions =
        client.monitor.firewall.sessions.list(srcaddr='10.1.1.100')

        >>> # Check system status
        >>> status = client.monitor.system.status.get()
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Monitor API handler.

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client
        self._azure: Azure | None = None
        self._casb: Casb | None = None
        self._endpoint_control: EndpointControl | None = None
        self._extender_controller: ExtenderController | None = None
        self._extension_controller: ExtensionController | None = None
        self._firewall: Firewall | None = None
        self._firmware: Firmware | None = None
        self._fortiguard: Fortiguard | None = None
        self._fortiview: Fortiview | None = None
        self._geoip: Geoip | None = None
        self._ips: Ips | None = None
        self._license: License | None = None
        self._log: Log | None = None
        self._network: Network | None = None
        self._registration: Registration | None = None
        self._router: Router | None = None
        self._sdwan: Sdwan | None = None
        self._service: Service | None = None
        self._switch_controller: SwitchController | None = None
        self._system: System | None = None
        self._user: User | None = None
        self._utm: Utm | None = None
        self._videofilter: Videofilter | None = None
        self._virtual_wan: VirtualWan | None = None
        self._vpn: Vpn | None = None
        self._vpn_certificate: VpnCertificate | None = None
        self._wanopt: Wanopt | None = None
        self._web_ui: WebUi | None = None
        self._webcache: Webcache | None = None
        self._webfilter: Webfilter | None = None
        self._webproxy: Webproxy | None = None
        self._wifi: Wifi | None = None

    @property
    def azure(self):
        """Azure SDN connector operations."""
        if self._azure is None:
            from .azure import Azure

            self._azure = Azure(self._client)
        return self._azure

    @property
    def casb(self):
        """CASB operations."""
        if self._casb is None:
            from .casb import Casb

            self._casb = Casb(self._client)
        return self._casb

    @property
    def endpoint_control(self):
        """FortiClient endpoint monitoring."""
        if self._endpoint_control is None:
            from .endpoint_control import EndpointControl

            self._endpoint_control = EndpointControl(self._client)
        return self._endpoint_control

    @property
    def extender_controller(self):
        """FortiExtender monitoring."""
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

    @property
    def firmware(self):
        """Firmware upgrade operations."""
        if self._firmware is None:
            from .firmware import Firmware

            self._firmware = Firmware(self._client)
        return self._firmware

    @property
    def fortiguard(self):
        """FortiGuard service operations."""
        if self._fortiguard is None:
            from .fortiguard import Fortiguard

            self._fortiguard = Fortiguard(self._client)
        return self._fortiguard

    @property
    def fortiview(self):
        """FortiView statistics."""
        if self._fortiview is None:
            from .fortiview import Fortiview

            self._fortiview = Fortiview(self._client)
        return self._fortiview

    @property
    def geoip(self):
        """GeoIP lookup operations."""
        if self._geoip is None:
            from .geoip import Geoip

            self._geoip = Geoip(self._client)
        return self._geoip

    @property
    def ips(self):
        """IPS monitoring."""
        if self._ips is None:
            from .ips import Ips

            self._ips = Ips(self._client)
        return self._ips

    @property
    def license(self):
        """License status."""
        if self._license is None:
            from .license import License

            self._license = License(self._client)
        return self._license

    @property
    def log(self):
        """Log device operations."""
        if self._log is None:
            from .log import Log

            self._log = Log(self._client)
        return self._log

    @property
    def network(self):
        """Network monitoring."""
        if self._network is None:
            from .network import Network

            self._network = Network(self._client)
        return self._network

    @property
    def registration(self):
        """Device registration."""
        if self._registration is None:
            from .registration import Registration

            self._registration = Registration(self._client)
        return self._registration

    @property
    def router(self):
        """Router monitoring and BGP/OSPF operations."""
        if self._router is None:
            from .router import Router

            self._router = Router(self._client)
        return self._router

    @property
    def sdwan(self):
        """SD-WAN monitoring."""
        if self._sdwan is None:
            from .sdwan import Sdwan

            self._sdwan = Sdwan(self._client)
        return self._sdwan

    @property
    def service(self):
        """Service monitoring."""
        if self._service is None:
            from .service import Service

            self._service = Service(self._client)
        return self._service

    @property
    def switch_controller(self):
        """FortiSwitch controller monitoring."""
        if self._switch_controller is None:
            from .switch_controller import SwitchController

            self._switch_controller = SwitchController(self._client)
        return self._switch_controller

    @property
    def system(self):
        """System monitoring, status, and diagnostics."""
        if self._system is None:
            from .system import System

            self._system = System(self._client)
        return self._system

    @property
    def user(self):
        """User authentication and monitoring."""
        if self._user is None:
            from .user import User

            self._user = User(self._client)
        return self._user

    @property
    def utm(self):
        """UTM monitoring."""
        if self._utm is None:
            from .utm import Utm

            self._utm = Utm(self._client)
        return self._utm

    @property
    def videofilter(self):
        """Video filter monitoring."""
        if self._videofilter is None:
            from .videofilter import Videofilter

            self._videofilter = Videofilter(self._client)
        return self._videofilter

    @property
    def virtual_wan(self):
        """Virtual WAN monitoring."""
        if self._virtual_wan is None:
            from .virtual_wan import VirtualWan

            self._virtual_wan = VirtualWan(self._client)
        return self._virtual_wan

    @property
    def vpn(self):
        """VPN monitoring (IPsec/SSL)."""
        if self._vpn is None:
            from .vpn import Vpn

            self._vpn = Vpn(self._client)
        return self._vpn

    @property
    def vpn_certificate(self):
        """VPN certificate monitoring."""
        if self._vpn_certificate is None:
            from .vpn_certificate import VpnCertificate

            self._vpn_certificate = VpnCertificate(self._client)
        return self._vpn_certificate

    @property
    def wanopt(self):
        """WAN optimization monitoring."""
        if self._wanopt is None:
            from .wanopt import Wanopt

            self._wanopt = Wanopt(self._client)
        return self._wanopt

    @property
    def web_ui(self):
        """Web UI customization."""
        if self._web_ui is None:
            from .web_ui import WebUi

            self._web_ui = WebUi(self._client)
        return self._web_ui

    @property
    def webcache(self):
        """Web cache monitoring."""
        if self._webcache is None:
            from .webcache import Webcache

            self._webcache = Webcache(self._client)
        return self._webcache

    @property
    def webfilter(self):
        """Web filter monitoring."""
        if self._webfilter is None:
            from .webfilter import Webfilter

            self._webfilter = Webfilter(self._client)
        return self._webfilter

    @property
    def webproxy(self):
        """Web proxy monitoring."""
        if self._webproxy is None:
            from .webproxy import Webproxy

            self._webproxy = Webproxy(self._client)
        return self._webproxy

    @property
    def wifi(self):
        """WiFi controller and AP monitoring."""
        if self._wifi is None:
            from .wifi import Wifi

            self._wifi = Wifi(self._client)
        return self._wifi

    def __dir__(self):
        """Control autocomplete to show available attributes"""
        return [
            "azure",
            "casb",
            "endpoint_control",
            "extender_controller",
            "extension_controller",
            "firewall",
            "firmware",
            "fortiguard",
            "fortiview",
            "geoip",
            "ips",
            "license",
            "log",
            "network",
            "registration",
            "router",
            "sdwan",
            "service",
            "switch_controller",
            "system",
            "user",
            "utm",
            "videofilter",
            "virtual_wan",
            "vpn",
            "vpn_certificate",
            "wanopt",
            "web_ui",
            "webcache",
            "webfilter",
            "webproxy",
            "wifi",
        ]
