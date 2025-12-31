Security Rating
===============

Overview
--------

The ``service.security_rating`` namespace provides configuration management for:

- :doc:`Security Rating <security_rating>` - Security Rating configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.service.security_rating.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   security_rating

See Also
--------

- :doc:`/api-reference/api-reference/service/index` - SERVICE API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
