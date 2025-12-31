Service
=======

Overview
--------

The ``monitor.service`` namespace provides configuration management for:

- :doc:`Ldap <ldap>` - Ldap configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.service.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   ldap

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
