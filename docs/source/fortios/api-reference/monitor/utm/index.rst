UTM
===

Overview
--------

The ``monitor.utm`` namespace provides configuration management for:

- :doc:`Antivirus <antivirus>` - Antivirus configuration endpoint.
- :doc:`App Lookup <app_lookup>` - App Lookup configuration endpoint.
- :doc:`Application Categories <application_categories>` - Application Categories configuration endpoint.
- :doc:`Blacklisted Certificates <blacklisted_certificates>` - Blacklisted Certificates configuration endpoint.
- :doc:`Rating Lookup <rating_lookup>` - Rating Lookup configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.utm.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   antivirus
   app_lookup
   application_categories
   blacklisted_certificates
   rating_lookup

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
