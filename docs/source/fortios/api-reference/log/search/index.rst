Search
======

Overview
--------

The ``log.search`` namespace provides configuration management for:

- :doc:`Search <search>` - Search configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.search.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   search

See Also
--------

- :doc:`/api-reference/api-reference/log/index` - LOG API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
