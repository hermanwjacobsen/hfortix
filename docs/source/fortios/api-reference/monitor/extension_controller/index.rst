Extension Controller
====================

Overview
--------

The ``monitor.extension_controller`` namespace provides configuration management for:

- :doc:`Fortigate <fortigate>` - Fortigate configuration endpoint.
- :doc:`Lan Extension Vdom <lan_extension_vdom>` - Lan Extension Vdom configuration endpoint.
- :doc:`Lan Extension Vdom Status <lan_extension_vdom_status>` - Lan Extension Vdom Status configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.extension_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   fortigate
   lan_extension_vdom
   lan_extension_vdom_status

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
