Extender Controller
===================

Overview
--------

The ``monitor.extender_controller`` namespace provides configuration management for:

- :doc:`Extender <extender>` - Extender configuration endpoint.
- :doc:`Modem Firmware <modem_firmware>` - Modem Firmware configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.extender_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   extender
   modem_firmware

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
