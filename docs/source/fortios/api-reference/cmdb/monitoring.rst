Monitoring
==========

Monitoring configuration.

.. automodule:: hfortix_fortios.api.v2.cmdb.monitoring
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Monitoring configuration through
   the ``fgt.api.cmdb.monitoring`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Monitoring endpoints
   result = fgt.api.cmdb.monitoring.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
