"""Type stubs for CMDB category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import alertemail
    from . import antivirus
    from . import application
    from . import authentication
    from . import automation
    from . import casb
    from . import certificate
    from . import diameter_filter
    from . import dlp
    from . import dnsfilter
    from . import emailfilter
    from . import endpoint_control
    from . import ethernet_oam
    from . import extension_controller
    from . import file_filter
    from . import firewall
    from . import ftp_proxy
    from . import icap
    from . import ips
    from . import log
    from . import monitoring
    from . import report
    from . import router
    from . import rule
    from . import sctp_filter
    from . import switch_controller
    from . import system
    from . import user
    from . import videofilter
    from . import virtual_patch
    from . import voip
    from . import vpn
    from . import waf
    from . import web_proxy
    from . import webfilter
    from . import wireless_controller
    from . import ztna

__all__ = [
    "CMDB",
    "CMDBDictMode",
    "CMDBObjectMode",
]

class CMDBDictMode:
    """CMDB API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    alertemail: alertemail.Alertemail  # No mode classes yet
    antivirus: antivirus.Antivirus  # No mode classes yet
    application: application.Application  # No mode classes yet
    authentication: authentication.Authentication  # No mode classes yet
    automation: automation.Automation  # No mode classes yet
    casb: casb.Casb  # No mode classes yet
    certificate: certificate.Certificate  # No mode classes yet
    diameter_filter: diameter_filter.DiameterFilter  # No mode classes yet
    dlp: dlp.Dlp  # No mode classes yet
    dnsfilter: dnsfilter.Dnsfilter  # No mode classes yet
    emailfilter: emailfilter.Emailfilter  # No mode classes yet
    endpoint_control: endpoint_control.EndpointControl  # No mode classes yet
    ethernet_oam: ethernet_oam.EthernetOam  # No mode classes yet
    extension_controller: extension_controller.ExtensionController  # No mode classes yet
    file_filter: file_filter.FileFilter  # No mode classes yet
    firewall: firewall.Firewall  # No mode classes yet
    ftp_proxy: ftp_proxy.FtpProxy  # No mode classes yet
    icap: icap.Icap  # No mode classes yet
    ips: ips.Ips  # No mode classes yet
    log: log.Log  # No mode classes yet
    monitoring: monitoring.Monitoring  # No mode classes yet
    report: report.Report  # No mode classes yet
    router: router.Router  # No mode classes yet
    rule: rule.Rule  # No mode classes yet
    sctp_filter: sctp_filter.SctpFilter  # No mode classes yet
    switch_controller: switch_controller.SwitchController  # No mode classes yet
    system: system.System  # No mode classes yet
    user: user.User  # No mode classes yet
    videofilter: videofilter.Videofilter  # No mode classes yet
    virtual_patch: virtual_patch.VirtualPatch  # No mode classes yet
    voip: voip.Voip  # No mode classes yet
    vpn: vpn.Vpn  # No mode classes yet
    waf: waf.Waf  # No mode classes yet
    web_proxy: web_proxy.WebProxy  # No mode classes yet
    webfilter: webfilter.Webfilter  # No mode classes yet
    wireless_controller: wireless_controller.WirelessController  # No mode classes yet
    ztna: ztna.Ztna  # No mode classes yet

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize CMDB category with HTTP client."""
        ...


class CMDBObjectMode:
    """CMDB API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    alertemail: alertemail.Alertemail  # No mode classes yet
    antivirus: antivirus.Antivirus  # No mode classes yet
    application: application.Application  # No mode classes yet
    authentication: authentication.Authentication  # No mode classes yet
    automation: automation.Automation  # No mode classes yet
    casb: casb.Casb  # No mode classes yet
    certificate: certificate.Certificate  # No mode classes yet
    diameter_filter: diameter_filter.DiameterFilter  # No mode classes yet
    dlp: dlp.Dlp  # No mode classes yet
    dnsfilter: dnsfilter.Dnsfilter  # No mode classes yet
    emailfilter: emailfilter.Emailfilter  # No mode classes yet
    endpoint_control: endpoint_control.EndpointControl  # No mode classes yet
    ethernet_oam: ethernet_oam.EthernetOam  # No mode classes yet
    extension_controller: extension_controller.ExtensionController  # No mode classes yet
    file_filter: file_filter.FileFilter  # No mode classes yet
    firewall: firewall.Firewall  # No mode classes yet
    ftp_proxy: ftp_proxy.FtpProxy  # No mode classes yet
    icap: icap.Icap  # No mode classes yet
    ips: ips.Ips  # No mode classes yet
    log: log.Log  # No mode classes yet
    monitoring: monitoring.Monitoring  # No mode classes yet
    report: report.Report  # No mode classes yet
    router: router.Router  # No mode classes yet
    rule: rule.Rule  # No mode classes yet
    sctp_filter: sctp_filter.SctpFilter  # No mode classes yet
    switch_controller: switch_controller.SwitchController  # No mode classes yet
    system: system.System  # No mode classes yet
    user: user.User  # No mode classes yet
    videofilter: videofilter.Videofilter  # No mode classes yet
    virtual_patch: virtual_patch.VirtualPatch  # No mode classes yet
    voip: voip.Voip  # No mode classes yet
    vpn: vpn.Vpn  # No mode classes yet
    waf: waf.Waf  # No mode classes yet
    web_proxy: web_proxy.WebProxy  # No mode classes yet
    webfilter: webfilter.Webfilter  # No mode classes yet
    wireless_controller: wireless_controller.WirelessController  # No mode classes yet
    ztna: ztna.Ztna  # No mode classes yet

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize CMDB category with HTTP client."""
        ...


# Base class for backwards compatibility
class CMDB:
    """CMDB API category."""
    
    alertemail: alertemail.Alertemail
    antivirus: antivirus.Antivirus
    application: application.Application
    authentication: authentication.Authentication
    automation: automation.Automation
    casb: casb.Casb
    certificate: certificate.Certificate
    diameter_filter: diameter_filter.DiameterFilter
    dlp: dlp.Dlp
    dnsfilter: dnsfilter.Dnsfilter
    emailfilter: emailfilter.Emailfilter
    endpoint_control: endpoint_control.EndpointControl
    ethernet_oam: ethernet_oam.EthernetOam
    extension_controller: extension_controller.ExtensionController
    file_filter: file_filter.FileFilter
    firewall: firewall.Firewall
    ftp_proxy: ftp_proxy.FtpProxy
    icap: icap.Icap
    ips: ips.Ips
    log: log.Log
    monitoring: monitoring.Monitoring
    report: report.Report
    router: router.Router
    rule: rule.Rule
    sctp_filter: sctp_filter.SctpFilter
    switch_controller: switch_controller.SwitchController
    system: system.System
    user: user.User
    videofilter: videofilter.Videofilter
    virtual_patch: virtual_patch.VirtualPatch
    voip: voip.Voip
    vpn: vpn.Vpn
    waf: waf.Waf
    web_proxy: web_proxy.WebProxy
    webfilter: webfilter.Webfilter
    wireless_controller: wireless_controller.WirelessController
    ztna: ztna.Ztna

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize CMDB category with HTTP client."""
        ...