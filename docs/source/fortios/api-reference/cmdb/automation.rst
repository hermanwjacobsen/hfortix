Automation
==========

Automation stitches and actions.

.. automodule:: hfortix_fortios.api.v2.cmdb.automation
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Automation configuration through
   the ``fgt.api.cmdb.automation`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Automation endpoints
   result = fgt.api.cmdb.automation.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
