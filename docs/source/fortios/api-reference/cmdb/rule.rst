Rule
====

Rule-based configuration.

.. automodule:: hfortix_fortios.api.v2.cmdb.rule
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Rule configuration through
   the ``fgt.api.cmdb.rule`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Rule endpoints
   result = fgt.api.cmdb.rule.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
