Extension Controller
====================

Overview
--------

The ``cmdb.extension_controller`` namespace provides configuration management for:

- :doc:`Dataplan <dataplan>` - Dataplan configuration endpoint.
- :doc:`Extender <extender>` - Extender configuration endpoint.
- :doc:`Extender Profile <extender_profile>` - Extender Profile configuration endpoint.
- :doc:`Extender Vap <extender_vap>` - Extender Vap configuration endpoint.
- :doc:`Fortigate <fortigate>` - Fortigate configuration endpoint.
- :doc:`Fortigate Profile <fortigate_profile>` - Fortigate Profile configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.extension_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   dataplan
   extender
   extender_profile
   extender_vap
   fortigate
   fortigate_profile

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
