Videofilter
===========

Configure video filter keywords configuration and management.

Overview
--------

The ``cmdb.videofilter`` category provides configuration management for:

- :ref:`Keyword <videofilter-keyword>` - Configure video filter keywords.
- :ref:`Profile <videofilter-profile>` - Configure VideoFilter profile.
- :ref:`Youtube Key <videofilter-youtube-key>` - Configure YouTube API keys.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.videofilter

Available Endpoints
-------------------

.. _videofilter-keyword:

keyword
~~~~~~~

Configure video filter keywords.

**Python attribute:** ``keyword``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.videofilter.keyword.get()
   
   # Get specific item
   item = fgt.api.cmdb.videofilter.keyword.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.videofilter.keyword.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.videofilter.keyword.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.videofilter.keyword.delete(mkey='item-name')

.. _videofilter-profile:

profile
~~~~~~~

Configure VideoFilter profile.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.videofilter.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.videofilter.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.videofilter.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.videofilter.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.videofilter.profile.delete(mkey='item-name')

.. _videofilter-youtube-key:

youtube-key
~~~~~~~~~~~

Configure YouTube API keys.

**Python attribute:** ``youtube_key``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.videofilter.youtube_key.get()
   
   # Get specific item
   item = fgt.api.cmdb.videofilter.youtube_key.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.videofilter.youtube_key.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.videofilter.youtube_key.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.videofilter.youtube_key.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.videofilter.keyword.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.videofilter.keyword.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.videofilter.keyword.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.videofilter.keyword.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.videofilter.keyword.delete(mkey='config-name')

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
