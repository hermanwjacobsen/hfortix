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
   result = fgt.api.cmdb.dnsfilter.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
