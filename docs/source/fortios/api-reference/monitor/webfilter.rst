Web Filter
==========

Web filter monitoring.

.. automodule:: hfortix_fortios.api.v2.monitor.webfilter
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Web Filter configuration through
   the ``fgt.api.monitor.webfilter`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Web Filter endpoints
   result = fgt.api.monitor.webfilter.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
