Diameter Filter
===============

Configure Diameter filter profiles configuration and management.

Overview
--------

The ``cmdb.diameter-filter`` category provides configuration management for:

- :doc:`Profile <profile>` - Configure Diameter filter profiles.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.diameter-filter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   profile

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
