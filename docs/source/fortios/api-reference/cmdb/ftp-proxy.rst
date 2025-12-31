FTP Proxy
=========

FTP proxy settings.

.. automodule:: hfortix_fortios.api.v2.cmdb.ftp_proxy
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS FTP Proxy configuration through
   the ``fgt.api.cmdb.ftp_proxy`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access FTP Proxy endpoints
   result = fgt.api.cmdb.ftp_proxy.<endpoint>.get()

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
