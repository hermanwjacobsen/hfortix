Virtual Wan
===========

Overview
--------

The ``monitor.virtual_wan`` namespace provides configuration management for:

- :doc:`Health Check <health_check>` - Health Check configuration endpoint.
- :doc:`Interface Log <interface_log>` - Interface Log configuration endpoint.
- :doc:`Members <members>` - Members configuration endpoint.
- :doc:`Sla Log <sla_log>` - Sla Log configuration endpoint.
- :doc:`Sladb <sladb>` - Sladb configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.virtual_wan.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   health_check
   interface_log
   members
   sla_log
   sladb

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
