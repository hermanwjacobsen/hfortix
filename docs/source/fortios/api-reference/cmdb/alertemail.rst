Alert Email
===========

Email alerting configuration.

.. automodule:: hfortix_fortios.api.v2.cmdb.alertemail
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS Alert Email configuration through
   the ``fgt.api.cmdb.alertemail`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access Alert Email endpoints
   result = fgt.api.cmdb.alertemail.<endpoint>.list()

See Also
--------

- :doc:`index` - CMDB API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
