Application
===========

Configure custom application signatures configuration and management.

Overview
--------

The ``cmdb.application`` category provides configuration management for:

- :doc:`Custom <custom>` - Configure custom application signatures.
- :doc:`Group <group>` - Configure firewall application groups.
- :doc:`List <list>` - Configure application control lists.
- :doc:`Name <name>` - Configure application signatures.
- :doc:`Rule Settings <rule-settings>` - Configure application rule settings.


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
   rule-settings

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
