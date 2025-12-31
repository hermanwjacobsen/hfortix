Registration
============

Overview
--------

The ``monitor.registration`` namespace provides configuration management for:

- :doc:`Forticare <forticare>` - Forticare configuration endpoint.
- :doc:`Forticloud <forticloud>` - Forticloud configuration endpoint.
- :doc:`Vdom <vdom>` - Vdom configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.registration.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   forticare
   forticloud
   vdom

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
