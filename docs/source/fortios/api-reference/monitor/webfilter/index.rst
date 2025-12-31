Webfilter
=========

Overview
--------

The ``monitor.webfilter`` namespace provides configuration management for:

- :doc:`Category Quota <category_quota>` - Category Quota configuration endpoint.
- :doc:`Fortiguard Categories <fortiguard_categories>` - Fortiguard Categories configuration endpoint.
- :doc:`Malicious Urls <malicious_urls>` - Malicious Urls configuration endpoint.
- :doc:`Override <override>` - Override configuration endpoint.
- :doc:`Trusted Urls <trusted_urls>` - Trusted Urls configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.webfilter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   category_quota
   fortiguard_categories
   malicious_urls
   override
   trusted_urls

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
