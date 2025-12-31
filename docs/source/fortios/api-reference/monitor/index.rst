Monitor API Reference
=====================

Real-time monitoring, statistics, and status information

.. toctree::
   :maxdepth: 1
   :caption: Categories

   azure
   casb
   endpoint-control
   extender-controller
   extension-controller
   firewall
   firmware
   fortiguard
   fortiview
   geoip
   ips
   license
   log
   network
   registration
   router
   sdwan
   service
   switch-controller
   system
   user
   utm
   videofilter
   virtual-wan
   vpn
   vpn-certificate
   wanopt
   web-ui
   webcache
   webfilter
   webproxy
   wifi


Overview
--------

The Monitor API Reference provides 32 categories of endpoints:

**Azure** (``monitor.azure``)
   Azure connector monitoring

**CASB** (``monitor.casb``)
   CASB monitoring

**Endpoint Control** (``monitor.endpoint_control``)
   Endpoint monitoring

**Extender Controller** (``monitor.extender_controller``)
   FortiExtender monitoring

**Extension Controller** (``monitor.extension_controller``)
   Extension controller monitoring

**Firewall** (``monitor.firewall``)
   Firewall statistics and sessions

**Firmware** (``monitor.firmware``)
   Firmware information

**FortiGuard** (``monitor.fortiguard``)
   FortiGuard services

**FortiView** (``monitor.fortiview``)
   FortiView statistics

**GeoIP** (``monitor.geoip``)
   GeoIP information

**IPS** (``monitor.ips``)
   IPS monitoring

**License** (``monitor.license``)
   License information

**Log** (``monitor.log``)
   Log monitoring

**Network** (``monitor.network``)
   Network monitoring

**Registration** (``monitor.registration``)
   Device registration

**Router** (``monitor.router``)
   Routing information

**SD-WAN** (``monitor.sdwan``)
   SD-WAN monitoring

**Service** (``monitor.service``)
   System services

**Switch Controller** (``monitor.switch_controller``)
   Switch monitoring

**System** (``monitor.system``)
   System status and resources

**User** (``monitor.user``)
   User monitoring

**UTM** (``monitor.utm``)
   UTM statistics

**Video Filter** (``monitor.videofilter``)
   Video filter monitoring

**Virtual WAN** (``monitor.virtual_wan``)
   Virtual WAN monitoring

**VPN** (``monitor.vpn``)
   VPN monitoring

**VPN Certificate** (``monitor.vpn_certificate``)
   VPN certificate monitoring

**WAN Optimization** (``monitor.wanopt``)
   WAN optimization monitoring

**Web UI** (``monitor.web_ui``)
   Web UI monitoring

**Web Cache** (``monitor.webcache``)
   Web cache monitoring

**Web Filter** (``monitor.webfilter``)
   Web filter monitoring

**Web Proxy** (``monitor.webproxy``)
   Web proxy monitoring

**WiFi** (``monitor.wifi``)
   WiFi monitoring


Usage Pattern
-------------

All Monitor API Reference endpoints follow the same pattern:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get all monitor data (HTTP GET without parameters)
   items = fgt.api.monitor.<category>.<endpoint>.get()
   
   # Get specific monitor data (HTTP GET with parameters)
   item = fgt.api.monitor.<category>.<endpoint>.get(param='value')
   
   # Note: Monitor API is read-only (GET only)
   # Use CMDB API for configuration changes
   
   # Update resource (CMDB only)
   result = fgt.api.monitor.<category>.<endpoint>.update(mkey='name', data)
   
   # Delete resource (CMDB only)
   result = fgt.api.monitor.<category>.<endpoint>.delete(mkey='name')

See Also
--------

- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Complete endpoint methods guide
- :doc:`/fortios/user-guide/filtering` - Filtering and query guide
