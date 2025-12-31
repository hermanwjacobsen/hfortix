ZTNA
====

Zero Trust Network Access.

.. automodule:: hfortix_fortios.api.v2.cmdb.ztna
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS ZTNA configuration through
   the ``fgt.api.cmdb.ztna`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access ZTNA endpoints
   result = fgt.api.cmdb.ztna.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
