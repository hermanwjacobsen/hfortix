CMDB
====

CMDB API Reference

This section contains all CMDB endpoints for FortiOS configuration and monitoring.

Categories
----------

- :doc:`Alertemail <alertemail/index>` - 1 endpoints
- :doc:`Antivirus <antivirus/index>` - 4 endpoints
- :doc:`Application <application/index>` - 5 endpoints
- :doc:`Authentication <authentication/index>` - 3 endpoints
- :doc:`Automation <automation/index>` - 1 endpoints
- :doc:`Casb <casb/index>` - 4 endpoints
- :doc:`Certificate <certificate/index>` - 5 endpoints
- :doc:`Diameter Filter <diameter_filter/index>` - 1 endpoints
- :doc:`Dlp <dlp/index>` - 8 endpoints
- :doc:`Dnsfilter <dnsfilter/index>` - 2 endpoints
- :doc:`Emailfilter <emailfilter/index>` - 8 endpoints
- :doc:`Endpoint Control <endpoint_control/index>` - 3 endpoints
- :doc:`Ethernet Oam <ethernet_oam/index>` - 1 endpoints
- :doc:`Extension Controller <extension_controller/index>` - 6 endpoints
- :doc:`File Filter <file_filter/index>` - 1 endpoints
- :doc:`Firewall <firewall/index>` - 89 endpoints
- :doc:`Ftp Proxy <ftp_proxy/index>` - 1 endpoints
- :doc:`Icap <icap/index>` - 3 endpoints
- :doc:`IPS <ips/index>` - 8 endpoints
- :doc:`Log <log/index>` - 56 endpoints
- :doc:`Monitoring <monitoring/index>` - 1 endpoints
- :doc:`Report <report/index>` - 2 endpoints
- :doc:`Router <router/index>` - 26 endpoints
- :doc:`Rule <rule/index>` - 4 endpoints
- :doc:`Sctp Filter <sctp_filter/index>` - 1 endpoints
- :doc:`Switch Controller <switch_controller/index>` - 48 endpoints
- :doc:`System <system/index>` - 145 endpoints
- :doc:`User <user/index>` - 24 endpoints
- :doc:`Videofilter <videofilter/index>` - 3 endpoints
- :doc:`Virtual Patch <virtual_patch/index>` - 1 endpoints
- :doc:`Voip <voip/index>` - 1 endpoints
- :doc:`VPN <vpn/index>` - 19 endpoints
- :doc:`WAF <waf/index>` - 3 endpoints
- :doc:`Web Proxy <web_proxy/index>` - 10 endpoints
- :doc:`Webfilter <webfilter/index>` - 14 endpoints
- :doc:`Wireless Controller <wireless_controller/index>` - 44 endpoints
- :doc:`ZTNA <ztna/index>` - 5 endpoints


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access CMDB endpoints via:
   fgt.api.cmdb.<category>.<endpoint>

All Categories
---------------

.. toctree::
   :maxdepth: 1
   
   alertemail/index
   antivirus/index
   application/index
   authentication/index
   automation/index
   casb/index
   certificate/index
   diameter_filter/index
   dlp/index
   dnsfilter/index
   emailfilter/index
   endpoint_control/index
   ethernet_oam/index
   extension_controller/index
   file_filter/index
   firewall/index
   ftp_proxy/index
   icap/index
   ips/index
   log/index
   monitoring/index
   report/index
   router/index
   rule/index
   sctp_filter/index
   switch_controller/index
   system/index
   user/index
   videofilter/index
   virtual_patch/index
   voip/index
   vpn/index
   waf/index
   web_proxy/index
   webfilter/index
   wireless_controller/index
   ztna/index
