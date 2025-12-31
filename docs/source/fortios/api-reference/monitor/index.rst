MONITOR
=======

MONITOR API Reference

This section contains all MONITOR endpoints for FortiOS configuration and monitoring.

Categories
----------

- :doc:`Azure <azure/index>` - 1 endpoints
- :doc:`Casb <casb/index>` - 1 endpoints
- :doc:`Endpoint Control <endpoint_control/index>` - 5 endpoints
- :doc:`Extender Controller <extender_controller/index>` - 2 endpoints
- :doc:`Extension Controller <extension_controller/index>` - 3 endpoints
- :doc:`Firewall <firewall/index>` - 44 endpoints
- :doc:`Firmware <firmware/index>` - 1 endpoints
- :doc:`Fortiguard <fortiguard/index>` - 3 endpoints
- :doc:`Fortiview <fortiview/index>` - 4 endpoints
- :doc:`Geoip <geoip/index>` - 1 endpoints
- :doc:`IPS <ips/index>` - 5 endpoints
- :doc:`License <license/index>` - 5 endpoints
- :doc:`Log <log/index>` - 15 endpoints
- :doc:`Network <network/index>` - 7 endpoints
- :doc:`Registration <registration/index>` - 3 endpoints
- :doc:`Router <router/index>` - 11 endpoints
- :doc:`Sdwan <sdwan/index>` - 1 endpoints
- :doc:`Service <service/index>` - 1 endpoints
- :doc:`Switch Controller <switch_controller/index>` - 9 endpoints
- :doc:`System <system/index>` - 83 endpoints
- :doc:`User <user/index>` - 16 endpoints
- :doc:`UTM <utm/index>` - 5 endpoints
- :doc:`Videofilter <videofilter/index>` - 1 endpoints
- :doc:`Virtual Wan <virtual_wan/index>` - 5 endpoints
- :doc:`VPN <vpn/index>` - 3 endpoints
- :doc:`VPN Certificate <vpn_certificate/index>` - 6 endpoints
- :doc:`Wanopt <wanopt/index>` - 3 endpoints
- :doc:`Web Ui <web_ui/index>` - 2 endpoints
- :doc:`Webcache <webcache/index>` - 1 endpoints
- :doc:`Webfilter <webfilter/index>` - 5 endpoints
- :doc:`Webproxy <webproxy/index>` - 1 endpoints
- :doc:`Wifi <wifi/index>` - 21 endpoints


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access MONITOR endpoints via:
   fgt.api.monitor.<category>.<endpoint>

All Categories
---------------

.. toctree::
   :maxdepth: 1
   
   azure/index
   casb/index
   endpoint_control/index
   extender_controller/index
   extension_controller/index
   firewall/index
   firmware/index
   fortiguard/index
   fortiview/index
   geoip/index
   ips/index
   license/index
   log/index
   network/index
   registration/index
   router/index
   sdwan/index
   service/index
   switch_controller/index
   system/index
   user/index
   utm/index
   videofilter/index
   virtual_wan/index
   vpn/index
   vpn_certificate/index
   wanopt/index
   web_ui/index
   webcache/index
   webfilter/index
   webproxy/index
   wifi/index
