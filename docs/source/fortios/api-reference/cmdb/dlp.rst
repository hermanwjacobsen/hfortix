DLP
===

Data Loss Prevention.

.. automodule:: hfortix_fortios.api.v2.cmdb.dlp
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS DLP configuration through
   the ``fgt.api.cmdb.dlp`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access DLP endpoints
   result = fgt.api.cmdb.dlp.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
