Fortiguard
==========

Overview
--------

The ``monitor.fortiguard`` namespace provides configuration management for:

- :doc:`Answers <answers>` - Answers configuration endpoint.
- :doc:`Redirect Portal <redirect_portal>` - Redirect Portal configuration endpoint.
- :doc:`Service Communication Stats <service_communication_stats>` - Service Communication Stats configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.fortiguard.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   answers
   redirect_portal
   service_communication_stats

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
