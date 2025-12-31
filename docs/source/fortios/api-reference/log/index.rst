LOG
===

LOG API Reference

This section contains all LOG endpoints for FortiOS configuration and monitoring.

Categories
----------

- :doc:`Search <search/index>` - 1 endpoints


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access LOG endpoints via:
   fgt.api.log.<category>.<endpoint>

All Categories
---------------

.. toctree::
   :maxdepth: 1
   
   search/index
