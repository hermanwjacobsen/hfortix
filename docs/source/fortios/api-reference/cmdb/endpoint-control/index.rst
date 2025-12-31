Endpoint Control
================

Configure FortiClient Enterprise Management Server (EMS) entries configuration and management.

Overview
--------

The ``cmdb.endpoint-control`` category provides configuration management for:

- :doc:`Fctems <fctems>` - Configure FortiClient Enterprise Management Server (EMS) entries.
- :doc:`Fctems Override <fctems-override>` - Configure FortiClient Enterprise Management Server (EMS) entries.
- :doc:`Settings <settings>` - Configure endpoint control settings.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.endpoint-control.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   fctems
   fctems-override
   settings

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
