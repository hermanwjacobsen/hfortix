Virtual Patch
=============

Configure virtual-patch profile configuration and management.

Overview
--------

The ``cmdb.virtual-patch`` category provides configuration management for:

- :doc:`Profile <profile>` - Configure virtual-patch profile.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.virtual-patch.<endpoint>

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
