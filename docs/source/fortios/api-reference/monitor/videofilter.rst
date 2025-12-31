Video Filter
============

Video filter monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.videofilter
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Video Filter configuration through
   the ``fgt.api.monitor.videofilter`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Video Filter endpoints
   result = fgt.api.monitor.videofilter.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
