System
======

System status and resources.

.. automodule:: hfortix_fortios.api.v2.monitor.system
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS System configuration through
   the ``fgt.api.monitor.system`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access System endpoints
   result = fgt.api.monitor.system.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
