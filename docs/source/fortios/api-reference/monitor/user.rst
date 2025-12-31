User
====

User monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.user
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS User configuration through
   the ``fgt.api.monitor.user`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access User endpoints
   result = fgt.api.monitor.user.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
