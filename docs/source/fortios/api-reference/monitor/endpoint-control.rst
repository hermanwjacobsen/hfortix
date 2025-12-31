Endpoint Control
================

Endpoint monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.endpoint_control
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Endpoint Control configuration through
   the ``fgt.api.monitor.endpoint_control`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Endpoint Control endpoints
   result = fgt.api.monitor.endpoint_control.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
