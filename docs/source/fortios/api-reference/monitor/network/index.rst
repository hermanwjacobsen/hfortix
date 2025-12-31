Network
=======

Overview
--------

The ``monitor.network`` namespace provides configuration management for:

- :doc:`Arp <arp>` - Arp configuration endpoint.
- :doc:`Ddns <ddns>` - Ddns configuration endpoint.
- :doc:`Debug Flow <debug_flow>` - Debug Flow configuration endpoint.
- :doc:`DNS <dns>` - DNS configuration endpoint.
- :doc:`Fortiguard <fortiguard>` - Fortiguard configuration endpoint.
- :doc:`Lldp <lldp>` - Lldp configuration endpoint.
- :doc:`Reverse IP Lookup <reverse_ip_lookup>` - Reverse IP Lookup configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.network.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   arp
   ddns
   debug_flow
   dns
   fortiguard
   lldp
   reverse_ip_lookup

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
