Casb
====

Configure CASB attribute match rule configuration and management.

Overview
--------

The ``cmdb.casb`` category provides configuration management for:

- :ref:`Attribute Match <casb-attribute-match>` - Configure CASB attribute match rule.
- :ref:`Profile <casb-profile>` - Configure CASB profile.
- :ref:`Saas Application <casb-saas-application>` - Configure CASB SaaS application.
- :ref:`User Activity <casb-user-activity>` - Configure CASB user activity.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.casb

Available Endpoints
-------------------

.. _casb-attribute-match:

attribute-match
~~~~~~~~~~~~~~~

Configure CASB attribute match rule.

**Python attribute:** ``attribute_match``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.casb.attribute_match.get()
   
   # Get specific item
   item = fgt.api.cmdb.casb.attribute_match.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.casb.attribute_match.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.casb.attribute_match.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.casb.attribute_match.delete(mkey='item-name')

.. _casb-profile:

profile
~~~~~~~

Configure CASB profile.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.casb.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.casb.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.casb.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.casb.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.casb.profile.delete(mkey='item-name')

.. _casb-saas-application:

saas-application
~~~~~~~~~~~~~~~~

Configure CASB SaaS application.

**Python attribute:** ``saas_application``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.casb.saas_application.get()
   
   # Get specific item
   item = fgt.api.cmdb.casb.saas_application.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.casb.saas_application.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.casb.saas_application.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.casb.saas_application.delete(mkey='item-name')

.. _casb-user-activity:

user-activity
~~~~~~~~~~~~~

Configure CASB user activity.

**Python attribute:** ``user_activity``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.casb.user_activity.get()
   
   # Get specific item
   item = fgt.api.cmdb.casb.user_activity.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.casb.user_activity.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.casb.user_activity.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.casb.user_activity.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.casb.attribute_match.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.casb.attribute_match.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.casb.attribute_match.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.casb.attribute_match.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.casb.attribute_match.delete(mkey='config-name')

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
