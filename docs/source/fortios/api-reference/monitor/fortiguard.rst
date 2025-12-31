FortiGuard
==========

FortiGuard services.

.. automodule:: hfortix_fortios.api.v2.monitor.fortiguard
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS FortiGuard configuration through
   the ``fgt.api.monitor.fortiguard`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access FortiGuard endpoints
   result = fgt.api.monitor.fortiguard.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
