Webfilter
=========

Configure Web filter banned word table configuration and management.

Overview
--------

The ``cmdb.webfilter`` category provides configuration management for:

- **Content** - Configure Web filter banned word table.
- **Content Header** - Configure content types used by Web filter.
- **Fortiguard** - Configure FortiGuard Web Filter service.
- **Ftgd Local Cat** - Configure FortiGuard Web Filter local categories.
- **Ftgd Local Rating** - Configure local FortiGuard Web Filter local ratings.
- **Ftgd Local Risk** - Configure FortiGuard Web Filter local risk score.
- **Ftgd Risk Level** - Configure FortiGuard Web Filter risk level.
- **Ips Urlfilter Cache Setting** - Configure IPS URL filter cache settings.
- **Ips Urlfilter Setting** - Configure IPS URL filter settings.
- **Ips Urlfilter Setting6** - Configure IPS URL filter settings for IPv6.
- **Override** - Configure FortiGuard Web Filter administrative overrides.
- **Profile** - Configure Web filter profiles.
- **Search Engine** - Configure web filter search engines.
- **Urlfilter** - Configure URL filter lists.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.webfilter

Available Endpoints
-------------------

**content**
   Configure Web filter banned word table.
   
   .. code-block:: python
   
      # List all content
      items = fgt.api.cmdb.webfilter.content.get()
      
      # Get specific content
      item = fgt.api.cmdb.webfilter.content.get(mkey='name')

**content-header**
   Configure content types used by Web filter.
   
   .. code-block:: python
   
      # List all content-header
      items = fgt.api.cmdb.webfilter.content_header.get()
      
      # Get specific content-header
      item = fgt.api.cmdb.webfilter.content_header.get(mkey='name')

**fortiguard**
   Configure FortiGuard Web Filter service.
   
   .. code-block:: python
   
      # List all fortiguard
      items = fgt.api.cmdb.webfilter.fortiguard.get()
      
      # Get specific fortiguard
      item = fgt.api.cmdb.webfilter.fortiguard.get(mkey='name')

**ftgd-local-cat**
   Configure FortiGuard Web Filter local categories.
   
   .. code-block:: python
   
      # List all ftgd-local-cat
      items = fgt.api.cmdb.webfilter.ftgd_local_cat.get()
      
      # Get specific ftgd-local-cat
      item = fgt.api.cmdb.webfilter.ftgd_local_cat.get(mkey='name')

**ftgd-local-rating**
   Configure local FortiGuard Web Filter local ratings.
   
   .. code-block:: python
   
      # List all ftgd-local-rating
      items = fgt.api.cmdb.webfilter.ftgd_local_rating.get()
      
      # Get specific ftgd-local-rating
      item = fgt.api.cmdb.webfilter.ftgd_local_rating.get(mkey='name')

**ftgd-local-risk**
   Configure FortiGuard Web Filter local risk score.
   
   .. code-block:: python
   
      # List all ftgd-local-risk
      items = fgt.api.cmdb.webfilter.ftgd_local_risk.get()
      
      # Get specific ftgd-local-risk
      item = fgt.api.cmdb.webfilter.ftgd_local_risk.get(mkey='name')

**ftgd-risk-level**
   Configure FortiGuard Web Filter risk level.
   
   .. code-block:: python
   
      # List all ftgd-risk-level
      items = fgt.api.cmdb.webfilter.ftgd_risk_level.get()
      
      # Get specific ftgd-risk-level
      item = fgt.api.cmdb.webfilter.ftgd_risk_level.get(mkey='name')

**ips-urlfilter-cache-setting**
   Configure IPS URL filter cache settings.
   
   .. code-block:: python
   
      # List all ips-urlfilter-cache-setting
      items = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.get()
      
      # Get specific ips-urlfilter-cache-setting
      item = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.get(mkey='name')

**ips-urlfilter-setting**
   Configure IPS URL filter settings.
   
   .. code-block:: python
   
      # List all ips-urlfilter-setting
      items = fgt.api.cmdb.webfilter.ips_urlfilter_setting.get()
      
      # Get specific ips-urlfilter-setting
      item = fgt.api.cmdb.webfilter.ips_urlfilter_setting.get(mkey='name')

**ips-urlfilter-setting6**
   Configure IPS URL filter settings for IPv6.
   
   .. code-block:: python
   
      # List all ips-urlfilter-setting6
      items = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.get()
      
      # Get specific ips-urlfilter-setting6
      item = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.get(mkey='name')

**override**
   Configure FortiGuard Web Filter administrative overrides.
   
   .. code-block:: python
   
      # List all override
      items = fgt.api.cmdb.webfilter.override.get()
      
      # Get specific override
      item = fgt.api.cmdb.webfilter.override.get(mkey='name')

**profile**
   Configure Web filter profiles.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.webfilter.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.webfilter.profile.get(mkey='name')

**search-engine**
   Configure web filter search engines.
   
   .. code-block:: python
   
      # List all search-engine
      items = fgt.api.cmdb.webfilter.search_engine.get()
      
      # Get specific search-engine
      item = fgt.api.cmdb.webfilter.search_engine.get(mkey='name')

**urlfilter**
   Configure URL filter lists.
   
   .. code-block:: python
   
      # List all urlfilter
      items = fgt.api.cmdb.webfilter.urlfilter.get()
      
      # Get specific urlfilter
      item = fgt.api.cmdb.webfilter.urlfilter.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.webfilter.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.webfilter.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.webfilter.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.webfilter.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.webfilter.{endpoint}.delete(mkey='config-name')

HTTP Methods
------------

All CMDB endpoints support standard HTTP methods:

**.get()**
   HTTP GET - Retrieve configuration(s)

**.post()**
   HTTP POST - Create new configuration

**.put()**
   HTTP PUT - Update existing configuration

**.delete()**
   HTTP DELETE - Remove configuration

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
