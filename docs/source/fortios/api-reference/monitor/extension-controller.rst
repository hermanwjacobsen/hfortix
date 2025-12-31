Extension Controller
====================

Extension controller monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.extension_controller
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Extension Controller configuration through
   the ``fgt.api.monitor.extension_controller`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Extension Controller endpoints
   result = fgt.api.monitor.extension_controller.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
