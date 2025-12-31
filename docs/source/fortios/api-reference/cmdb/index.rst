CMDB API Reference
==================

Configuration Management Database - Device configuration and settings

.. toctree::
   :maxdepth: 1
   :caption: Categories

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


Overview
--------

The CMDB API Reference provides 37 categories of endpoints:

**Alert Email** (``cmdb.alertemail``)
   Email alerting configuration

**Antivirus** (``cmdb.antivirus``)
   Antivirus profiles and settings

**Application** (``cmdb.application``)
   Application control and lists

**Authentication** (``cmdb.authentication``)
   Authentication settings

**Automation** (``cmdb.automation``)
   Automation stitches and actions

**CASB** (``cmdb.casb``)
   Cloud Access Security Broker

**Certificate** (``cmdb.certificate``)
   Certificate management

**Diameter Filter** (``cmdb.diameter_filter``)
   Diameter filtering profiles

**DLP** (``cmdb.dlp``)
   Data Loss Prevention

**DNS Filter** (``cmdb.dnsfilter``)
   DNS filtering profiles

**Email Filter** (``cmdb.emailfilter``)
   Email filtering profiles

**Endpoint Control** (``cmdb.endpoint_control``)
   Endpoint control settings

**Ethernet OAM** (``cmdb.ethernet_oam``)
   Ethernet OAM configuration

**Extension Controller** (``cmdb.extension_controller``)
   FortiExtender controller

**File Filter** (``cmdb.file_filter``)
   File filtering profiles

**Firewall** (``cmdb.firewall``)
   Firewall policies, addresses, and services

**FTP Proxy** (``cmdb.ftp_proxy``)
   FTP proxy settings

**ICAP** (``cmdb.icap``)
   ICAP server configuration

**IPS** (``cmdb.ips``)
   Intrusion Prevention System

**Log** (``cmdb.log``)
   Logging configuration

**Monitoring** (``cmdb.monitoring``)
   Monitoring configuration

**Report** (``cmdb.report``)
   Report settings

**Router** (``cmdb.router``)
   Routing configuration

**Rule** (``cmdb.rule``)
   Rule-based configuration

**SCTP Filter** (``cmdb.sctp_filter``)
   SCTP filtering

**Switch Controller** (``cmdb.switch_controller``)
   Switch controller settings

**System** (``cmdb.system``)
   System configuration and settings

**User** (``cmdb.user``)
   User and authentication

**Video Filter** (``cmdb.videofilter``)
   Video filtering

**Virtual Patch** (``cmdb.virtual_patch``)
   Virtual patching

**VoIP** (``cmdb.voip``)
   VoIP configuration

**VPN** (``cmdb.vpn``)
   VPN configuration

**WAF** (``cmdb.waf``)
   Web Application Firewall

**Web Proxy** (``cmdb.web_proxy``)
   Web proxy settings

**Web Filter** (``cmdb.webfilter``)
   Web filtering profiles

**Wireless Controller** (``cmdb.wireless_controller``)
   Wireless controller

**ZTNA** (``cmdb.ztna``)
   Zero Trust Network Access


Usage Pattern
-------------

All CMDB API Reference endpoints follow the same pattern:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # List resources
   items = fgt.api.cmdb.<category>.<endpoint>.list()
   
   # Get specific resource
   item = fgt.api.cmdb.<category>.<endpoint>.get(mkey='name')
   
   # Create resource (CMDB only)
   result = fgt.api.cmdb.<category>.<endpoint>.create(data)
   
   # Update resource (CMDB only)
   result = fgt.api.cmdb.<category>.<endpoint>.update(mkey='name', data)
   
   # Delete resource (CMDB only)
   result = fgt.api.cmdb.<category>.<endpoint>.delete(mkey='name')

See Also
--------

- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Complete endpoint methods guide
- :doc:`../../user-guide/filtering` - Filtering and query guide
