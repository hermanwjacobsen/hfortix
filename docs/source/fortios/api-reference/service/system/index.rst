System
======

Overview
--------

The ``service.system`` namespace provides configuration management for:

- :doc:`System <system>` - System configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.service.system.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   system

See Also
--------

- :doc:`/api-reference/api-reference/service/index` - SERVICE API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
