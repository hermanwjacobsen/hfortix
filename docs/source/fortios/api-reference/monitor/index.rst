Monitor API Reference
=====================

Real-time monitoring, statistics, and status information

Overview
--------

The Monitor API Reference provides 32 categories of endpoints:

:doc:`azure` - **Azure** (``monitor.azure``)
   Azure connector monitoring

:doc:`casb` - **CASB** (``monitor.casb``)
   CASB monitoring

:doc:`endpoint-control` - **Endpoint Control** (``monitor.endpoint_control``)
   Endpoint monitoring

:doc:`extender-controller` - **Extender Controller** (``monitor.extender_controller``)
   FortiExtender monitoring

:doc:`extension-controller` - **Extension Controller** (``monitor.extension_controller``)
   Extension controller monitoring

:doc:`firewall` - **Firewall** (``monitor.firewall``)
   Firewall statistics and sessions

:doc:`firmware` - **Firmware** (``monitor.firmware``)
   Firmware information

:doc:`fortiguard` - **FortiGuard** (``monitor.fortiguard``)
   FortiGuard services

:doc:`fortiview` - **FortiView** (``monitor.fortiview``)
   FortiView statistics

:doc:`geoip` - **GeoIP** (``monitor.geoip``)
   GeoIP information

:doc:`ips` - **IPS** (``monitor.ips``)
   IPS monitoring

:doc:`license` - **License** (``monitor.license``)
   License information

:doc:`log` - **Log** (``monitor.log``)
   Log monitoring

:doc:`network` - **Network** (``monitor.network``)
   Network monitoring

:doc:`registration` - **Registration** (``monitor.registration``)
   Device registration

:doc:`router` - **Router** (``monitor.router``)
   Routing information

:doc:`sdwan` - **SD-WAN** (``monitor.sdwan``)
   SD-WAN monitoring

:doc:`service` - **Service** (``monitor.service``)
   System services

:doc:`switch-controller` - **Switch Controller** (``monitor.switch_controller``)
   Switch monitoring

:doc:`system` - **System** (``monitor.system``)
   System status and resources

:doc:`user` - **User** (``monitor.user``)
   User monitoring

:doc:`utm` - **UTM** (``monitor.utm``)
   UTM statistics

:doc:`videofilter` - **Video Filter** (``monitor.videofilter``)
   Video filter monitoring

:doc:`virtual-wan` - **Virtual WAN** (``monitor.virtual_wan``)
   Virtual WAN monitoring

:doc:`vpn` - **VPN** (``monitor.vpn``)
   VPN monitoring

:doc:`vpn-certificate` - **VPN Certificate** (``monitor.vpn_certificate``)
   VPN certificate monitoring

:doc:`wanopt` - **WAN Optimization** (``monitor.wanopt``)
   WAN optimization monitoring

:doc:`web-ui` - **Web UI** (``monitor.web_ui``)
   Web UI monitoring

:doc:`webcache` - **Web Cache** (``monitor.webcache``)
   Web cache monitoring

:doc:`webfilter` - **Web Filter** (``monitor.webfilter``)
   Web filter monitoring

:doc:`webproxy` - **Web Proxy** (``monitor.webproxy``)
   Web proxy monitoring

:doc:`wifi` - **WiFi** (``monitor.wifi``)
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
