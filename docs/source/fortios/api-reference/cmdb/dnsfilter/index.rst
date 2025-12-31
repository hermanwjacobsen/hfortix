Dnsfilter
=========

Configure DNS domain filters configuration and management.

Overview
--------

The ``cmdb.dnsfilter`` category provides configuration management for:

- :doc:`Domain Filter <domain-filter>` - Configure DNS domain filters.
- :doc:`Profile <profile>` - Configure DNS domain filter profile.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.dnsfilter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   domain-filter
   profile

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
