CASB
====

Cloud Access Security Broker.

.. automodule:: hfortix_fortios.api.v2.cmdb.casb
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS CASB configuration through
   the ``fgt.api.cmdb.casb`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access CASB endpoints
   result = fgt.api.cmdb.casb.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
