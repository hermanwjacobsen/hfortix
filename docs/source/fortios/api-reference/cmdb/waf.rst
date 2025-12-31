WAF
===

Web Application Firewall.

.. automodule:: hfortix_fortios.api.v2.cmdb.waf
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS WAF configuration through
   the ``fgt.api.cmdb.waf`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access WAF endpoints
   result = fgt.api.cmdb.waf.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
