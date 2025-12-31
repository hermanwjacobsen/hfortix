Firewall
========

Firewall statistics and sessions.

.. automodule:: hfortix_fortios.api.v2.monitor.firewall
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Firewall configuration through
   the ``fgt.api.monitor.firewall`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Firewall endpoints
   result = fgt.api.monitor.firewall.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
