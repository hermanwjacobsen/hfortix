Geoip
=====

Overview
--------

The ``monitor.geoip`` namespace provides configuration management for:

- :doc:`Geoip Query <geoip_query>` - Geoip Query configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.geoip.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   geoip_query

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
