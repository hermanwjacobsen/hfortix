Certificate
===========

Overview
--------

The ``cmdb.certificate`` namespace provides configuration management for:

- :doc:`Ca <ca>` - Ca configuration endpoint.
- :doc:`Crl <crl>` - Crl configuration endpoint.
- :doc:`Hsm Local <hsm_local>` - Hsm Local configuration endpoint.
- :doc:`Local <local>` - Local configuration endpoint.
- :doc:`Remote <remote>` - Remote configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.certificate.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   ca
   crl
   hsm_local
   local
   remote

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
