Application
===========

Overview
--------

The ``cmdb.application`` namespace provides configuration management for:

- :doc:`Custom <custom>` - Custom configuration endpoint.
- :doc:`Group <group>` - Group configuration endpoint.
- :doc:`List <list>` - List configuration endpoint.
- :doc:`Name <name>` - Name configuration endpoint.
- :doc:`Rule Settings <rule_settings>` - Rule Settings configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.application.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   custom
   group
   list
   name
   rule_settings

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
