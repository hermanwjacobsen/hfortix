Endpoint Control
================

Overview
--------

The ``monitor.endpoint_control`` namespace provides configuration management for:

- :doc:`Avatar <avatar>` - Avatar configuration endpoint.
- :doc:`Ems <ems>` - Ems configuration endpoint.
- :doc:`Installer <installer>` - Installer configuration endpoint.
- :doc:`Record List <record_list>` - Record List configuration endpoint.
- :doc:`Summary <summary>` - Summary configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.endpoint_control.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   avatar
   ems
   installer
   record_list
   summary

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
