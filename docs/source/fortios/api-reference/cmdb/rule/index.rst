Rule
====

Show FMWP signatures configuration and management.

Overview
--------

The ``cmdb.rule`` category provides configuration management for:

- :doc:`Fmwp <fmwp>` - Show FMWP signatures.
- :doc:`Iotd <iotd>` - Show IOT detection signatures.
- :doc:`Otdt <otdt>` - Show OT detection signatures.
- :doc:`Otvp <otvp>` - Show OT patch signatures.


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

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
