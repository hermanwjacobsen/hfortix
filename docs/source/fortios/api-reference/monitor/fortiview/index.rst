Fortiview
=========

Overview
--------

The ``monitor.fortiview`` namespace provides configuration management for:

- :doc:`Historical Statistics <historical_statistics>` - Historical Statistics configuration endpoint.
- :doc:`Realtime Proxy Statistics <realtime_proxy_statistics>` - Realtime Proxy Statistics configuration endpoint.
- :doc:`Realtime Statistics <realtime_statistics>` - Realtime Statistics configuration endpoint.
- :doc:`Session <session>` - Session configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.fortiview.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   historical_statistics
   realtime_proxy_statistics
   realtime_statistics
   session

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
