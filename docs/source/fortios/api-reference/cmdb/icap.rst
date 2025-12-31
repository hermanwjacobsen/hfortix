ICAP
====

ICAP server configuration.

.. automodule:: hfortix_fortios.api.v2.cmdb.icap
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS ICAP configuration through
   the ``fgt.api.cmdb.icap`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access ICAP endpoints
   result = fgt.api.cmdb.icap.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
