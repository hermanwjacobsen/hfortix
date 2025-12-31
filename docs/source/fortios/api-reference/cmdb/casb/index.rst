Casb
====

Overview
--------

The ``cmdb.casb`` namespace provides configuration management for:

- :doc:`Attribute Match <attribute_match>` - Attribute Match configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Saas Application <saas_application>` - Saas Application configuration endpoint.
- :doc:`User Activity <user_activity>` - User Activity configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.casb.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   attribute_match
   profile
   saas_application
   user_activity

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
