Extension Controller
====================

FortiExtender dataplan configuration configuration and management.

Overview
--------

The ``cmdb.extension-controller`` category provides configuration management for:

- :doc:`Dataplan <dataplan>` - FortiExtender dataplan configuration.
- :doc:`Extender <extender>` - Extender controller configuration.
- :doc:`Extender Profile <extender-profile>` - FortiExtender extender profile configuration.
- :doc:`Extender Vap <extender-vap>` - FortiExtender wifi vap configuration.
- :doc:`Fortigate <fortigate>` - FortiGate controller configuration.
- :doc:`Fortigate Profile <fortigate-profile>` - FortiGate connector profile configuration.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.extension-controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   dataplan
   extender
   extender-profile
   extender-vap
   fortigate
   fortigate-profile

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
