Ethernet Oam
============

CFM domain configuration configuration and management.

Overview
--------

The ``cmdb.ethernet-oam`` category provides configuration management for:

- :doc:`Cfm <cfm>` - CFM domain configuration.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.ethernet-oam.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   cfm

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
