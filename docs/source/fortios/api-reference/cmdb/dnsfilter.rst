DNS Filter
==========

DNS filtering profiles.

.. automodule:: hfortix_fortios.api.v2.cmdb.dnsfilter
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS DNS Filter configuration through
   the ``fgt.api.cmdb.dnsfilter`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access DNS Filter endpoints
   result = fgt.api.cmdb.dnsfilter.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
