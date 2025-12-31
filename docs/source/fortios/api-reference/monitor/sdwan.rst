SD-WAN
======

SD-WAN monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.sdwan
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS SD-WAN configuration through
   the ``fgt.api.monitor.sdwan`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access SD-WAN endpoints
   result = fgt.api.monitor.sdwan.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
