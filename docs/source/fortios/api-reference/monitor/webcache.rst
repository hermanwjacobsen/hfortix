Web Cache
=========

Web cache monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.webcache
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Web Cache configuration through
   the ``fgt.api.monitor.webcache`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Web Cache endpoints
   result = fgt.api.monitor.webcache.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
