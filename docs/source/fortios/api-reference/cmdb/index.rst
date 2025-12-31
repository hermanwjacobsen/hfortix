CMDB API Reference
==================

Configuration Management Database - Device configuration and settings

Overview
--------

The CMDB API Reference provides 37 categories of endpoints:

:doc:`alertemail` - **Alert Email** (``cmdb.alertemail``)
   Email alerting configuration

:doc:`antivirus` - **Antivirus** (``cmdb.antivirus``)
   Antivirus profiles and settings

:doc:`application` - **Application** (``cmdb.application``)
   Application control and lists

:doc:`authentication` - **Authentication** (``cmdb.authentication``)
   Authentication settings

:doc:`automation` - **Automation** (``cmdb.automation``)
   Automation stitches and actions

:doc:`casb` - **CASB** (``cmdb.casb``)
   Cloud Access Security Broker

:doc:`certificate` - **Certificate** (``cmdb.certificate``)
   Certificate management

:doc:`diameter-filter` - **Diameter Filter** (``cmdb.diameter_filter``)
   Diameter filtering profiles

:doc:`dlp` - **DLP** (``cmdb.dlp``)
   Data Loss Prevention

:doc:`dnsfilter` - **DNS Filter** (``cmdb.dnsfilter``)
   DNS filtering profiles

:doc:`emailfilter` - **Email Filter** (``cmdb.emailfilter``)
   Email filtering profiles

:doc:`endpoint-control` - **Endpoint Control** (``cmdb.endpoint_control``)
   Endpoint control settings

:doc:`ethernet-oam` - **Ethernet OAM** (``cmdb.ethernet_oam``)
   Ethernet OAM configuration

:doc:`extension-controller` - **Extension Controller** (``cmdb.extension_controller``)
   FortiExtender controller

:doc:`file-filter` - **File Filter** (``cmdb.file_filter``)
   File filtering profiles

:doc:`firewall` - **Firewall** (``cmdb.firewall``)
   Firewall policies, addresses, and services

:doc:`ftp-proxy` - **FTP Proxy** (``cmdb.ftp_proxy``)
   FTP proxy settings

:doc:`icap` - **ICAP** (``cmdb.icap``)
   ICAP server configuration

:doc:`ips` - **IPS** (``cmdb.ips``)
   Intrusion Prevention System

:doc:`log` - **Log** (``cmdb.log``)
   Logging configuration

:doc:`monitoring` - **Monitoring** (``cmdb.monitoring``)
   Monitoring configuration

:doc:`report` - **Report** (``cmdb.report``)
   Report settings

:doc:`router` - **Router** (``cmdb.router``)
   Routing configuration

:doc:`rule` - **Rule** (``cmdb.rule``)
   Rule-based configuration

:doc:`sctp-filter` - **SCTP Filter** (``cmdb.sctp_filter``)
   SCTP filtering

:doc:`switch-controller` - **Switch Controller** (``cmdb.switch_controller``)
   Switch controller settings

:doc:`system` - **System** (``cmdb.system``)
   System configuration and settings

:doc:`user` - **User** (``cmdb.user``)
   User and authentication

:doc:`videofilter` - **Video Filter** (``cmdb.videofilter``)
   Video filtering

:doc:`virtual-patch` - **Virtual Patch** (``cmdb.virtual_patch``)
   Virtual patching

:doc:`voip` - **VoIP** (``cmdb.voip``)
   VoIP configuration

:doc:`vpn` - **VPN** (``cmdb.vpn``)
   VPN configuration

:doc:`waf` - **WAF** (``cmdb.waf``)
   Web Application Firewall

:doc:`web-proxy` - **Web Proxy** (``cmdb.web_proxy``)
   Web proxy settings

:doc:`webfilter` - **Web Filter** (``cmdb.webfilter``)
   Web filtering profiles

:doc:`wireless-controller` - **Wireless Controller** (``cmdb.wireless_controller``)
   Wireless controller

:doc:`ztna` - **ZTNA** (``cmdb.ztna``)
   Zero Trust Network Access

.. toctree::
   :maxdepth: 1
   :hidden:

   alertemail
   antivirus
   application
   authentication
   automation
   casb
   certificate
   diameter-filter
   dlp
   dnsfilter
   emailfilter
   endpoint-control
   ethernet-oam
   extension-controller
   file-filter
   firewall
   ftp-proxy
   icap
   ips
   log
   monitoring
   report
   router
   rule
   sctp-filter
   switch-controller
   system
   user
   videofilter
   virtual-patch
   voip
   vpn
   waf
   web-proxy
   webfilter
   wireless-controller
   ztna

Usage Pattern
-------------

All CMDB API Reference endpoints follow the same pattern:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get all resources (HTTP GET without mkey)
   items = fgt.api.cmdb.<category>.<endpoint>.get()
   
   # Get specific resource (HTTP GET with mkey)
   item = fgt.api.cmdb.<category>.<endpoint>.get(mkey='name')
   
   # Create resource (HTTP POST)
   result = fgt.api.cmdb.<category>.<endpoint>.post(json=data)
   
   # Update resource (CMDB only)
   result = fgt.api.cmdb.<category>.<endpoint>.update(mkey='name', data)
   
   # Delete resource (CMDB only)
   result = fgt.api.cmdb.<category>.<endpoint>.delete(mkey='name')

See Also
--------

- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Complete endpoint methods guide
- :doc:`/fortios/user-guide/filtering` - Filtering and query guide
