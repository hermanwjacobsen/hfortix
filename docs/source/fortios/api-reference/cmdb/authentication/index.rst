Authentication
==============

Configure Authentication Rules configuration and management.

Overview
--------

The ``cmdb.authentication`` category provides configuration management for:

- :doc:`Rule <rule>` - Configure Authentication Rules.
- :doc:`Scheme <scheme>` - Configure Authentication Schemes.
- :doc:`Setting <setting>` - Configure authentication setting.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.authentication.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   rule
   scheme
   setting

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
