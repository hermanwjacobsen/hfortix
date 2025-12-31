Ethernet OAM
============

Ethernet OAM configuration.

.. automodule:: hfortix_fortios.api.v2.cmdb.ethernet_oam
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Ethernet OAM configuration through
   the ``fgt.api.cmdb.ethernet_oam`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Ethernet OAM endpoints
   result = fgt.api.cmdb.ethernet_oam.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
