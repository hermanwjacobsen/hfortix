Dlp
===

Configure predefined data type used by DLP blocking configuration and management.

Overview
--------

The ``cmdb.dlp`` category provides configuration management for:

- **Data Type** - Configure predefined data type used by DLP blocking.
- **Dictionary** - Configure dictionaries used by DLP blocking.
- **Exact Data Match** - Configure exact-data-match template used by DLP scan.
- **Filepattern** - Configure file patterns used by DLP blocking.
- **Label** - Configure labels used by DLP blocking.
- **Profile** - Configure DLP profiles.
- **Sensor** - Configure sensors used by DLP blocking.
- **Settings** - Configure settings for DLP.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.dlp

Available Endpoints
-------------------

**data-type**
   Configure predefined data type used by DLP blocking.
   
   .. code-block:: python
   
      # List all data-type
      items = fgt.api.cmdb.dlp.data_type.get()
      
      # Get specific data-type
      item = fgt.api.cmdb.dlp.data_type.get(mkey='name')

**dictionary**
   Configure dictionaries used by DLP blocking.
   
   .. code-block:: python
   
      # List all dictionary
      items = fgt.api.cmdb.dlp.dictionary.get()
      
      # Get specific dictionary
      item = fgt.api.cmdb.dlp.dictionary.get(mkey='name')

**exact-data-match**
   Configure exact-data-match template used by DLP scan.
   
   .. code-block:: python
   
      # List all exact-data-match
      items = fgt.api.cmdb.dlp.exact_data_match.get()
      
      # Get specific exact-data-match
      item = fgt.api.cmdb.dlp.exact_data_match.get(mkey='name')

**filepattern**
   Configure file patterns used by DLP blocking.
   
   .. code-block:: python
   
      # List all filepattern
      items = fgt.api.cmdb.dlp.filepattern.get()
      
      # Get specific filepattern
      item = fgt.api.cmdb.dlp.filepattern.get(mkey='name')

**label**
   Configure labels used by DLP blocking.
   
   .. code-block:: python
   
      # List all label
      items = fgt.api.cmdb.dlp.label.get()
      
      # Get specific label
      item = fgt.api.cmdb.dlp.label.get(mkey='name')

**profile**
   Configure DLP profiles.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.dlp.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.dlp.profile.get(mkey='name')

**sensor**
   Configure sensors used by DLP blocking.
   
   .. code-block:: python
   
      # List all sensor
      items = fgt.api.cmdb.dlp.sensor.get()
      
      # Get specific sensor
      item = fgt.api.cmdb.dlp.sensor.get(mkey='name')

**settings**
   Configure settings for DLP.
   
   .. code-block:: python
   
      # List all settings
      items = fgt.api.cmdb.dlp.settings.get()
      
      # Get specific settings
      item = fgt.api.cmdb.dlp.settings.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.dlp.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.dlp.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.dlp.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.dlp.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.dlp.{endpoint}.delete(mkey='config-name')

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
