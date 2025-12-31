VPN
===

Overview
--------

The ``monitor.vpn`` namespace provides configuration management for:

- :doc:`Ike <ike>` - Ike configuration endpoint.
- :doc:`Ipsec <ipsec>` - Ipsec configuration endpoint.
- :doc:`Ssl <ssl>` - Ssl configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.vpn.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   ike
   ipsec
   ssl

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
