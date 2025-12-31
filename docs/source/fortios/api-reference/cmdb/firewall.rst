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
   result = fgt.api.cmdb.firewall.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
