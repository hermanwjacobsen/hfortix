Certificate
===========

CA certificate configuration and management.

Overview
--------

The ``cmdb.certificate`` category provides configuration management for:

- :doc:`Ca <ca>` - CA certificate.
- :doc:`Crl <crl>` - Certificate Revocation List as a PEM file.
- :doc:`Hsm Local <hsm-local>` - Local certificates whose keys are stored on HSM.
- :doc:`Local <local>` - Local keys and certificates.
- :doc:`Remote <remote>` - Remote certificate as a PEM file.


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
   hsm-local
   local
   remote

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
