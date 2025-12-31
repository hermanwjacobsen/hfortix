WAF
===

Overview
--------

The ``cmdb.waf`` namespace provides configuration management for:

- :doc:`Main Class <main_class>` - Main Class configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Signature <signature>` - Signature configuration endpoint.


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
   
   main_class
   profile
   signature

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
