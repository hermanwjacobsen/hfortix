Authentication
==============

Authentication settings.

.. automodule:: hfortix_fortios.api.v2.cmdb.authentication
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Authentication configuration through
   the ``fgt.api.cmdb.authentication`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Authentication endpoints
   result = fgt.api.cmdb.authentication.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
