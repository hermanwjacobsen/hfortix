Rule
====

Overview
--------

The ``cmdb.rule`` namespace provides configuration management for:

- :doc:`Fmwp <fmwp>` - Fmwp configuration endpoint.
- :doc:`Iotd <iotd>` - Iotd configuration endpoint.
- :doc:`Otdt <otdt>` - Otdt configuration endpoint.
- :doc:`Otvp <otvp>` - Otvp configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.rule.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   fmwp
   iotd
   otdt
   otvp

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
