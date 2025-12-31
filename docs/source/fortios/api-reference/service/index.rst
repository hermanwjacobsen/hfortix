SERVICE
=======

SERVICE API Reference

This section contains all SERVICE endpoints for FortiOS configuration and monitoring.

Categories
----------

- :doc:`Security Rating <security_rating/index>` - 1 endpoints
- :doc:`Sniffer <sniffer/index>` - 1 endpoints
- :doc:`System <system/index>` - 1 endpoints


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access SERVICE endpoints via:
   fgt.api.service.<category>.<endpoint>

All Categories
---------------

.. toctree::
   :maxdepth: 1
   
   security_rating/index
   sniffer/index
   system/index
