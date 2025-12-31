Waf
===

Hidden table for datasource configuration and management.

Overview
--------

The ``cmdb.waf`` category provides configuration management for:

- :doc:`Main Class <main-class>` - Hidden table for datasource.
- :doc:`Profile <profile>` - Configure Web application firewall configuration.
- :doc:`Signature <signature>` - Hidden table for datasource.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.waf.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   main-class
   profile
   signature

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
