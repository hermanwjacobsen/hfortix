Azure
=====

Overview
--------

The ``monitor.azure`` namespace provides configuration management for:

- :doc:`Application List <application_list>` - Application List configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.azure.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   application_list

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
