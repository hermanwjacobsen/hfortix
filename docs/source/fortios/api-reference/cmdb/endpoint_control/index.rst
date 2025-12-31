Endpoint Control
================

Overview
--------

The ``cmdb.endpoint_control`` namespace provides configuration management for:

- :doc:`Fctems <fctems>` - Fctems configuration endpoint.
- :doc:`Fctems Override <fctems_override>` - Fctems Override configuration endpoint.
- :doc:`Settings <settings>` - Settings configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.endpoint_control.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   fctems
   fctems_override
   settings

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
