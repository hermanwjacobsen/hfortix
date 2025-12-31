Icap
====

Overview
--------

The ``cmdb.icap`` namespace provides configuration management for:

- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Server <server>` - Server configuration endpoint.
- :doc:`Server Group <server_group>` - Server Group configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.icap.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   profile
   server
   server_group

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
