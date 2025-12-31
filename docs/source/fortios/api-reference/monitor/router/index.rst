Router
======

Overview
--------

The ``monitor.router`` namespace provides configuration management for:

- :doc:`Bgp <bgp>` - Bgp configuration endpoint.
- :doc:`Charts <charts>` - Charts configuration endpoint.
- :doc:`IPv4 <ipv4>` - IPv4 configuration endpoint.
- :doc:`IPv6 <ipv6>` - IPv6 configuration endpoint.
- :doc:`Lookup <lookup>` - Lookup configuration endpoint.
- :doc:`Lookup Policy <lookup_policy>` - Lookup Policy configuration endpoint.
- :doc:`Ospf <ospf>` - Ospf configuration endpoint.
- :doc:`Policy <policy>` - Policy configuration endpoint.
- :doc:`Policy6 <policy6>` - Policy6 configuration endpoint.
- :doc:`Sdwan <sdwan>` - Sdwan configuration endpoint.
- :doc:`Statistics <statistics>` - Statistics configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.router.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   bgp
   charts
   ipv4
   ipv6
   lookup
   lookup_policy
   ospf
   policy
   policy6
   sdwan
   statistics

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
