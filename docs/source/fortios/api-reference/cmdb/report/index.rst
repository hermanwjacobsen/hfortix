Report
======

Overview
--------

The ``cmdb.report`` namespace provides configuration management for:

- :doc:`Layout <layout>` - Layout configuration endpoint.
- :doc:`Setting <setting>` - Setting configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.report.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   layout
   setting

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
