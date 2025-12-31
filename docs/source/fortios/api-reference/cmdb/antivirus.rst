Antivirus
=========

Configure a list of hashes to be exempt from AV scanning configuration and management.

Overview
--------

The ``cmdb.antivirus`` category provides configuration management for:

- :ref:`Exempt List <antivirus-exempt-list>` - Configure a list of hashes to be exempt from AV scanning.
- :ref:`Profile <antivirus-profile>` - Configure AntiVirus profiles.
- :ref:`Quarantine <antivirus-quarantine>` - Configure quarantine options.
- :ref:`Settings <antivirus-settings>` - Configure AntiVirus settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.antivirus

Available Endpoints
-------------------

.. _antivirus-exempt-list:

exempt-list
~~~~~~~~~~~

Configure a list of hashes to be exempt from AV scanning.

**Python attribute:** ``exempt_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.antivirus.exempt_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.antivirus.exempt_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.antivirus.exempt_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.antivirus.exempt_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.antivirus.exempt_list.delete(mkey='item-name')

.. _antivirus-profile:

profile
~~~~~~~

Configure AntiVirus profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.antivirus.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.antivirus.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.antivirus.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.antivirus.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.antivirus.profile.delete(mkey='item-name')

.. _antivirus-quarantine:

quarantine
~~~~~~~~~~

Configure quarantine options.

**Python attribute:** ``quarantine``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.antivirus.quarantine.get()
   
   # Get specific item
   item = fgt.api.cmdb.antivirus.quarantine.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.antivirus.quarantine.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.antivirus.quarantine.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.antivirus.quarantine.delete(mkey='item-name')

.. _antivirus-settings:

settings
~~~~~~~~

Configure AntiVirus settings.

**Python attribute:** ``settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.antivirus.settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.antivirus.settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.antivirus.settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.antivirus.settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.antivirus.settings.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.antivirus.exempt_list.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.antivirus.exempt_list.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.antivirus.exempt_list.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.antivirus.exempt_list.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.antivirus.exempt_list.delete(mkey='config-name')

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
