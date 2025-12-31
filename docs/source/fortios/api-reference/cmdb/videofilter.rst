Videofilter
===========

Configure video filter keywords configuration and management.

Overview
--------

The ``cmdb.videofilter`` category provides configuration management for:

- **Keyword** - Configure video filter keywords.
- **Profile** - Configure VideoFilter profile.
- **Youtube Key** - Configure YouTube API keys.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.videofilter

Available Endpoints
-------------------

**keyword**
   Configure video filter keywords.
   
   .. code-block:: python
   
      # List all keyword
      items = fgt.api.cmdb.videofilter.keyword.get()
      
      # Get specific keyword
      item = fgt.api.cmdb.videofilter.keyword.get(mkey='name')

**profile**
   Configure VideoFilter profile.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.videofilter.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.videofilter.profile.get(mkey='name')

**youtube-key**
   Configure YouTube API keys.
   
   .. code-block:: python
   
      # List all youtube-key
      items = fgt.api.cmdb.videofilter.youtube_key.get()
      
      # Get specific youtube-key
      item = fgt.api.cmdb.videofilter.youtube_key.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.videofilter.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.videofilter.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.videofilter.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.videofilter.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.videofilter.{endpoint}.delete(mkey='config-name')

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
