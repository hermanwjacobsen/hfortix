FortiView
=========

FortiView statistics.

.. automodule:: hfortix_fortios.api.v2.monitor.fortiview
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS FortiView configuration through
   the ``fgt.api.monitor.fortiview`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access FortiView endpoints
   result = fgt.api.monitor.fortiview.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
