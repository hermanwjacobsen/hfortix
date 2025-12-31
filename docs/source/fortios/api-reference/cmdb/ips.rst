IPS
===

Intrusion Prevention System.

.. automodule:: hfortix_fortios.api.v2.cmdb.ips
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS IPS configuration through
   the ``fgt.api.cmdb.ips`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access IPS endpoints
   result = fgt.api.cmdb.ips.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
