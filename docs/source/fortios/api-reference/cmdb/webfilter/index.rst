Webfilter
=========

Overview
--------

The ``cmdb.webfilter`` namespace provides configuration management for:

- :doc:`Content <content>` - Content configuration endpoint.
- :doc:`Content Header <content_header>` - Content Header configuration endpoint.
- :doc:`Fortiguard <fortiguard>` - Fortiguard configuration endpoint.
- :doc:`Ftgd Local Cat <ftgd_local_cat>` - Ftgd Local Cat configuration endpoint.
- :doc:`Ftgd Local Rating <ftgd_local_rating>` - Ftgd Local Rating configuration endpoint.
- :doc:`Ftgd Local Risk <ftgd_local_risk>` - Ftgd Local Risk configuration endpoint.
- :doc:`Ftgd Risk Level <ftgd_risk_level>` - Ftgd Risk Level configuration endpoint.
- :doc:`IPS Urlfilter Cache Setting <ips_urlfilter_cache_setting>` - IPS Urlfilter Cache Setting configuration endpoint.
- :doc:`IPS Urlfilter Setting <ips_urlfilter_setting>` - IPS Urlfilter Setting configuration endpoint.
- :doc:`IPS Urlfilter Setting6 <ips_urlfilter_setting6>` - IPS Urlfilter Setting6 configuration endpoint.
- :doc:`Override <override>` - Override configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Search Engine <search_engine>` - Search Engine configuration endpoint.
- :doc:`Urlfilter <urlfilter>` - Urlfilter configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.webfilter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   content
   content_header
   fortiguard
   ftgd_local_cat
   ftgd_local_rating
   ftgd_local_risk
   ftgd_risk_level
   ips_urlfilter_cache_setting
   ips_urlfilter_setting
   ips_urlfilter_setting6
   override
   profile
   search_engine
   urlfilter

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
