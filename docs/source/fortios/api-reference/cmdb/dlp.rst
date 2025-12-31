Dlp
===

Configure predefined data type used by DLP blocking configuration and management.

Overview
--------

The ``cmdb.dlp`` category provides configuration management for:

- :ref:`Data Type <dlp-data-type>` - Configure predefined data type used by DLP blocking.
- :ref:`Dictionary <dlp-dictionary>` - Configure dictionaries used by DLP blocking.
- :ref:`Exact Data Match <dlp-exact-data-match>` - Configure exact-data-match template used by DLP scan.
- :ref:`Filepattern <dlp-filepattern>` - Configure file patterns used by DLP blocking.
- :ref:`Label <dlp-label>` - Configure labels used by DLP blocking.
- :ref:`Profile <dlp-profile>` - Configure DLP profiles.
- :ref:`Sensor <dlp-sensor>` - Configure sensors used by DLP blocking.
- :ref:`Settings <dlp-settings>` - Configure settings for DLP.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.dlp

Available Endpoints
-------------------

.. _dlp-data-type:

data-type
~~~~~~~~~

Configure predefined data type used by DLP blocking.

**Python attribute:** ``data_type``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.data_type.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.data_type.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.data_type.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.data_type.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.data_type.delete(mkey='item-name')

.. _dlp-dictionary:

dictionary
~~~~~~~~~~

Configure dictionaries used by DLP blocking.

**Python attribute:** ``dictionary``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.dictionary.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.dictionary.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.dictionary.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.dictionary.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.dictionary.delete(mkey='item-name')

.. _dlp-exact-data-match:

exact-data-match
~~~~~~~~~~~~~~~~

Configure exact-data-match template used by DLP scan.

**Python attribute:** ``exact_data_match``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.exact_data_match.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.exact_data_match.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.exact_data_match.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.exact_data_match.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.exact_data_match.delete(mkey='item-name')

.. _dlp-filepattern:

filepattern
~~~~~~~~~~~

Configure file patterns used by DLP blocking.

**Python attribute:** ``filepattern``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.filepattern.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.filepattern.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.filepattern.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.filepattern.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.filepattern.delete(mkey='item-name')

.. _dlp-label:

label
~~~~~

Configure labels used by DLP blocking.

**Python attribute:** ``label``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.label.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.label.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.label.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.label.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.label.delete(mkey='item-name')

.. _dlp-profile:

profile
~~~~~~~

Configure DLP profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.profile.delete(mkey='item-name')

.. _dlp-sensor:

sensor
~~~~~~

Configure sensors used by DLP blocking.

**Python attribute:** ``sensor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.sensor.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.sensor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.sensor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.sensor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.sensor.delete(mkey='item-name')

.. _dlp-settings:

settings
~~~~~~~~

Configure settings for DLP.

**Python attribute:** ``settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.dlp.settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.dlp.settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.dlp.settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.dlp.settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.dlp.settings.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.dlp.data_type.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.dlp.data_type.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.dlp.data_type.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.dlp.data_type.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.dlp.data_type.delete(mkey='config-name')

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
