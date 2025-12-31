Casb
====

Configure CASB attribute match rule configuration and management.

Overview
--------

The ``cmdb.casb`` category provides configuration management for:

- :doc:`Attribute Match <attribute-match>` - Configure CASB attribute match rule.
- :doc:`Profile <profile>` - Configure CASB profile.
- :doc:`Saas Application <saas-application>` - Configure CASB SaaS application.
- :doc:`User Activity <user-activity>` - Configure CASB user activity.


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
   
   attribute-match
   profile
   saas-application
   user-activity

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
