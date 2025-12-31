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
   result = fgt.api.cmdb.ips.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
