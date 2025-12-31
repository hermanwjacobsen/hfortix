Icap
====

Configure ICAP profiles configuration and management.

Overview
--------

The ``cmdb.icap`` category provides configuration management for:

- :doc:`Profile <profile>` - Configure ICAP profiles.
- :doc:`Server <server>` - Configure ICAP servers.
- :doc:`Server Group <server-group>` - Configure an ICAP server group consisting of multiple forward servers. Supports failover and load balancing.


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
   server-group

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
