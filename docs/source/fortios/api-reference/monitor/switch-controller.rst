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
   result = fgt.api.monitor.switch_controller.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
