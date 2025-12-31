Webproxy
========

Overview
--------

The ``monitor.webproxy`` namespace provides configuration management for:

- :doc:`Pacfile <pacfile>` - Pacfile configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.webproxy.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   pacfile

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
