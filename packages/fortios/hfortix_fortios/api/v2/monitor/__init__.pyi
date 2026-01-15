"""Type stubs for MONITOR category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import azure
    from . import casb
    from . import endpoint_control
    from . import extender_controller
    from . import extension_controller
    from . import firewall
    from . import firmware
    from . import fortiguard
    from . import fortiview
    from . import geoip
    from . import ips
    from . import license
    from . import log
    from . import network
    from . import registration
    from . import router
    from . import sdwan
    from . import service
    from . import switch_controller
    from . import system
    from . import user
    from . import utm
    from . import videofilter
    from . import virtual_wan
    from . import vpn
    from . import vpn_certificate
    from . import wanopt
    from . import web_ui
    from . import webcache
    from . import webfilter
    from . import webproxy
    from . import wifi

__all__ = [
    "Monitor",
    "MonitorDictMode",
    "MonitorObjectMode",
]

class MonitorDictMode:
    """MONITOR API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    azure: azure.Azure  # No mode classes yet
    casb: casb.Casb  # No mode classes yet
    endpoint_control: endpoint_control.EndpointControl  # No mode classes yet
    extender_controller: extender_controller.ExtenderController  # No mode classes yet
    extension_controller: extension_controller.ExtensionController  # No mode classes yet
    firewall: firewall.Firewall  # No mode classes yet
    firmware: firmware.Firmware  # No mode classes yet
    fortiguard: fortiguard.Fortiguard  # No mode classes yet
    fortiview: fortiview.Fortiview  # No mode classes yet
    geoip: geoip.Geoip  # No mode classes yet
    ips: ips.Ips  # No mode classes yet
    license: license.License  # No mode classes yet
    log: log.Log  # No mode classes yet
    network: network.Network  # No mode classes yet
    registration: registration.Registration  # No mode classes yet
    router: router.Router  # No mode classes yet
    sdwan: sdwan.Sdwan  # No mode classes yet
    service: service.Service  # No mode classes yet
    switch_controller: switch_controller.SwitchController  # No mode classes yet
    system: system.System  # No mode classes yet
    user: user.User  # No mode classes yet
    utm: utm.Utm  # No mode classes yet
    videofilter: videofilter.Videofilter  # No mode classes yet
    virtual_wan: virtual_wan.VirtualWan  # No mode classes yet
    vpn: vpn.Vpn  # No mode classes yet
    vpn_certificate: vpn_certificate.VpnCertificate  # No mode classes yet
    wanopt: wanopt.Wanopt  # No mode classes yet
    web_ui: web_ui.WebUi  # No mode classes yet
    webcache: webcache.Webcache  # No mode classes yet
    webfilter: webfilter.Webfilter  # No mode classes yet
    webproxy: webproxy.Webproxy  # No mode classes yet
    wifi: wifi.Wifi  # No mode classes yet

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize MONITOR category with HTTP client."""
        ...


class MonitorObjectMode:
    """MONITOR API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    azure: azure.Azure  # No mode classes yet
    casb: casb.Casb  # No mode classes yet
    endpoint_control: endpoint_control.EndpointControl  # No mode classes yet
    extender_controller: extender_controller.ExtenderController  # No mode classes yet
    extension_controller: extension_controller.ExtensionController  # No mode classes yet
    firewall: firewall.Firewall  # No mode classes yet
    firmware: firmware.Firmware  # No mode classes yet
    fortiguard: fortiguard.Fortiguard  # No mode classes yet
    fortiview: fortiview.Fortiview  # No mode classes yet
    geoip: geoip.Geoip  # No mode classes yet
    ips: ips.Ips  # No mode classes yet
    license: license.License  # No mode classes yet
    log: log.Log  # No mode classes yet
    network: network.Network  # No mode classes yet
    registration: registration.Registration  # No mode classes yet
    router: router.Router  # No mode classes yet
    sdwan: sdwan.Sdwan  # No mode classes yet
    service: service.Service  # No mode classes yet
    switch_controller: switch_controller.SwitchController  # No mode classes yet
    system: system.System  # No mode classes yet
    user: user.User  # No mode classes yet
    utm: utm.Utm  # No mode classes yet
    videofilter: videofilter.Videofilter  # No mode classes yet
    virtual_wan: virtual_wan.VirtualWan  # No mode classes yet
    vpn: vpn.Vpn  # No mode classes yet
    vpn_certificate: vpn_certificate.VpnCertificate  # No mode classes yet
    wanopt: wanopt.Wanopt  # No mode classes yet
    web_ui: web_ui.WebUi  # No mode classes yet
    webcache: webcache.Webcache  # No mode classes yet
    webfilter: webfilter.Webfilter  # No mode classes yet
    webproxy: webproxy.Webproxy  # No mode classes yet
    wifi: wifi.Wifi  # No mode classes yet

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize MONITOR category with HTTP client."""
        ...


# Base class for backwards compatibility
class Monitor:
    """MONITOR API category."""
    
    azure: azure.Azure
    casb: casb.Casb
    endpoint_control: endpoint_control.EndpointControl
    extender_controller: extender_controller.ExtenderController
    extension_controller: extension_controller.ExtensionController
    firewall: firewall.Firewall
    firmware: firmware.Firmware
    fortiguard: fortiguard.Fortiguard
    fortiview: fortiview.Fortiview
    geoip: geoip.Geoip
    ips: ips.Ips
    license: license.License
    log: log.Log
    network: network.Network
    registration: registration.Registration
    router: router.Router
    sdwan: sdwan.Sdwan
    service: service.Service
    switch_controller: switch_controller.SwitchController
    system: system.System
    user: user.User
    utm: utm.Utm
    videofilter: videofilter.Videofilter
    virtual_wan: virtual_wan.VirtualWan
    vpn: vpn.Vpn
    vpn_certificate: vpn_certificate.VpnCertificate
    wanopt: wanopt.Wanopt
    web_ui: web_ui.WebUi
    webcache: webcache.Webcache
    webfilter: webfilter.Webfilter
    webproxy: webproxy.Webproxy
    wifi: wifi.Wifi

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize MONITOR category with HTTP client."""
        ...