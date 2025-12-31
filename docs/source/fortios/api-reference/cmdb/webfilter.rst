Webfilter
=========

Configure Web filter banned word table configuration and management.

Overview
--------

The ``cmdb.webfilter`` category provides configuration management for:

- :ref:`Content <webfilter-content>` - Configure Web filter banned word table.
- :ref:`Content Header <webfilter-content-header>` - Configure content types used by Web filter.
- :ref:`Fortiguard <webfilter-fortiguard>` - Configure FortiGuard Web Filter service.
- :ref:`Ftgd Local Cat <webfilter-ftgd-local-cat>` - Configure FortiGuard Web Filter local categories.
- :ref:`Ftgd Local Rating <webfilter-ftgd-local-rating>` - Configure local FortiGuard Web Filter local ratings.
- :ref:`Ftgd Local Risk <webfilter-ftgd-local-risk>` - Configure FortiGuard Web Filter local risk score.
- :ref:`Ftgd Risk Level <webfilter-ftgd-risk-level>` - Configure FortiGuard Web Filter risk level.
- :ref:`Ips Urlfilter Cache Setting <webfilter-ips-urlfilter-cache-setting>` - Configure IPS URL filter cache settings.
- :ref:`Ips Urlfilter Setting <webfilter-ips-urlfilter-setting>` - Configure IPS URL filter settings.
- :ref:`Ips Urlfilter Setting6 <webfilter-ips-urlfilter-setting6>` - Configure IPS URL filter settings for IPv6.
- :ref:`Override <webfilter-override>` - Configure FortiGuard Web Filter administrative overrides.
- :ref:`Profile <webfilter-profile>` - Configure Web filter profiles.
- :ref:`Search Engine <webfilter-search-engine>` - Configure web filter search engines.
- :ref:`Urlfilter <webfilter-urlfilter>` - Configure URL filter lists.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.webfilter

Available Endpoints
-------------------

.. _webfilter-content:

content
~~~~~~~

Configure Web filter banned word table.

**Python attribute:** ``content``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.content.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.content.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.content.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.content.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.content.delete(mkey='item-name')

.. _webfilter-content-header:

content-header
~~~~~~~~~~~~~~

Configure content types used by Web filter.

**Python attribute:** ``content_header``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.content_header.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.content_header.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.content_header.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.content_header.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.content_header.delete(mkey='item-name')

.. _webfilter-fortiguard:

fortiguard
~~~~~~~~~~

Configure FortiGuard Web Filter service.

**Python attribute:** ``fortiguard``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.fortiguard.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.fortiguard.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.fortiguard.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.fortiguard.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.fortiguard.delete(mkey='item-name')

.. _webfilter-ftgd-local-cat:

ftgd-local-cat
~~~~~~~~~~~~~~

Configure FortiGuard Web Filter local categories.

**Python attribute:** ``ftgd_local_cat``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ftgd_local_cat.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ftgd_local_cat.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ftgd_local_cat.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ftgd_local_cat.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ftgd_local_cat.delete(mkey='item-name')

.. _webfilter-ftgd-local-rating:

ftgd-local-rating
~~~~~~~~~~~~~~~~~

Configure local FortiGuard Web Filter local ratings.

**Python attribute:** ``ftgd_local_rating``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ftgd_local_rating.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ftgd_local_rating.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ftgd_local_rating.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ftgd_local_rating.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ftgd_local_rating.delete(mkey='item-name')

.. _webfilter-ftgd-local-risk:

ftgd-local-risk
~~~~~~~~~~~~~~~

Configure FortiGuard Web Filter local risk score.

**Python attribute:** ``ftgd_local_risk``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ftgd_local_risk.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ftgd_local_risk.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.delete(mkey='item-name')

.. _webfilter-ftgd-risk-level:

ftgd-risk-level
~~~~~~~~~~~~~~~

Configure FortiGuard Web Filter risk level.

**Python attribute:** ``ftgd_risk_level``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ftgd_risk_level.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ftgd_risk_level.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ftgd_risk_level.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ftgd_risk_level.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ftgd_risk_level.delete(mkey='item-name')

.. _webfilter-ips-urlfilter-cache-setting:

ips-urlfilter-cache-setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure IPS URL filter cache settings.

**Python attribute:** ``ips_urlfilter_cache_setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_cache_setting.delete(mkey='item-name')

.. _webfilter-ips-urlfilter-setting:

ips-urlfilter-setting
~~~~~~~~~~~~~~~~~~~~~

Configure IPS URL filter settings.

**Python attribute:** ``ips_urlfilter_setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ips_urlfilter_setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ips_urlfilter_setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting.delete(mkey='item-name')

.. _webfilter-ips-urlfilter-setting6:

ips-urlfilter-setting6
~~~~~~~~~~~~~~~~~~~~~~

Configure IPS URL filter settings for IPv6.

**Python attribute:** ``ips_urlfilter_setting6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.ips_urlfilter_setting6.delete(mkey='item-name')

.. _webfilter-override:

override
~~~~~~~~

Configure FortiGuard Web Filter administrative overrides.

**Python attribute:** ``override``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.override.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.override.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.override.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.override.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.override.delete(mkey='item-name')

.. _webfilter-profile:

profile
~~~~~~~

Configure Web filter profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.profile.delete(mkey='item-name')

.. _webfilter-search-engine:

search-engine
~~~~~~~~~~~~~

Configure web filter search engines.

**Python attribute:** ``search_engine``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.search_engine.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.search_engine.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.search_engine.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.search_engine.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.search_engine.delete(mkey='item-name')

.. _webfilter-urlfilter:

urlfilter
~~~~~~~~~

Configure URL filter lists.

**Python attribute:** ``urlfilter``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.webfilter.urlfilter.get()
   
   # Get specific item
   item = fgt.api.cmdb.webfilter.urlfilter.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.webfilter.urlfilter.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.webfilter.urlfilter.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.webfilter.urlfilter.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.webfilter.content.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.webfilter.content.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.webfilter.content.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.webfilter.content.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.webfilter.content.delete(mkey='config-name')

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
