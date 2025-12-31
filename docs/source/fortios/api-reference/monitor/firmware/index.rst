Firmware
========

Overview
--------

The ``monitor.firmware`` namespace provides configuration management for:

- :doc:`Extension Device <extension_device>` - Extension Device configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.firmware.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   extension_device

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
