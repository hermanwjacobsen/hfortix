Firewall
========

Firewall policies, addresses, and services.

.. automodule:: hfortix_fortios.api.v2.cmdb.firewall
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Firewall configuration through
   the ``fgt.api.cmdb.firewall`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Firewall endpoints
   result = fgt.api.cmdb.firewall.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
