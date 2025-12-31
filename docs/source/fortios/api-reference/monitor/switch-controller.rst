Switch Controller
=================

Switch monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.switch_controller
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Switch Controller configuration through
   the ``fgt.api.monitor.switch_controller`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Switch Controller endpoints
   result = fgt.api.monitor.switch_controller.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
