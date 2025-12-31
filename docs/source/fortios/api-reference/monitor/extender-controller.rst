Extender Controller
===================

FortiExtender monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.extender_controller
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Extender Controller configuration through
   the ``fgt.api.monitor.extender_controller`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Extender Controller endpoints
   result = fgt.api.monitor.extender_controller.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
