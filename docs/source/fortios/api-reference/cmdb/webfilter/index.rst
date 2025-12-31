Webfilter
=========

Configure Web filter banned word table configuration and management.

Overview
--------

The ``cmdb.webfilter`` category provides configuration management for:

- :doc:`Content <content>` - Configure Web filter banned word table.
- :doc:`Content Header <content-header>` - Configure content types used by Web filter.
- :doc:`Fortiguard <fortiguard>` - Configure FortiGuard Web Filter service.
- :doc:`Ftgd Local Cat <ftgd-local-cat>` - Configure FortiGuard Web Filter local categories.
- :doc:`Ftgd Local Rating <ftgd-local-rating>` - Configure local FortiGuard Web Filter local ratings.
- :doc:`Ftgd Local Risk <ftgd-local-risk>` - Configure FortiGuard Web Filter local risk score.
- :doc:`Ftgd Risk Level <ftgd-risk-level>` - Configure FortiGuard Web Filter risk level.
- :doc:`Ips Urlfilter Cache Setting <ips-urlfilter-cache-setting>` - Configure IPS URL filter cache settings.
- :doc:`Ips Urlfilter Setting <ips-urlfilter-setting>` - Configure IPS URL filter settings.
- :doc:`Ips Urlfilter Setting6 <ips-urlfilter-setting6>` - Configure IPS URL filter settings for IPv6.
- :doc:`Override <override>` - Configure FortiGuard Web Filter administrative overrides.
- :doc:`Profile <profile>` - Configure Web filter profiles.
- :doc:`Search Engine <search-engine>` - Configure web filter search engines.
- :doc:`Urlfilter <urlfilter>` - Configure URL filter lists.


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
   content-header
   fortiguard
   ftgd-local-cat
   ftgd-local-rating
   ftgd-local-risk
   ftgd-risk-level
   ips-urlfilter-cache-setting
   ips-urlfilter-setting
   ips-urlfilter-setting6
   override
   profile
   search-engine
   urlfilter

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
