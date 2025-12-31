Web Proxy
=========

Web proxy settings.

.. automodule:: hfortix_fortios.api.v2.cmdb.web_proxy
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Web Proxy configuration through
   the ``fgt.api.cmdb.web_proxy`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Web Proxy endpoints
   result = fgt.api.cmdb.web_proxy.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
