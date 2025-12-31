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
   result = fgt.api.cmdb.automation.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
