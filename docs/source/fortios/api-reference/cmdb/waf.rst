Waf
===

Hidden table for datasource configuration and management.

Overview
--------

The ``cmdb.waf`` category provides configuration management for:

- :ref:`Main Class <waf-main-class>` - Hidden table for datasource.
- :ref:`Profile <waf-profile>` - Configure Web application firewall configuration.
- :ref:`Signature <waf-signature>` - Hidden table for datasource.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.waf

Available Endpoints
-------------------

.. _waf-main-class:

main-class
~~~~~~~~~~

Hidden table for datasource.

**Python attribute:** ``main_class``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.waf.main_class.get()
   
   # Get specific item
   item = fgt.api.cmdb.waf.main_class.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.waf.main_class.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.waf.main_class.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.waf.main_class.delete(mkey='item-name')

.. _waf-profile:

profile
~~~~~~~

Configure Web application firewall configuration.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.waf.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.waf.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.waf.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.waf.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.waf.profile.delete(mkey='item-name')

.. _waf-signature:

signature
~~~~~~~~~

Hidden table for datasource.

**Python attribute:** ``signature``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.waf.signature.get()
   
   # Get specific item
   item = fgt.api.cmdb.waf.signature.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.waf.signature.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.waf.signature.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.waf.signature.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.waf.main_class.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.waf.main_class.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.waf.main_class.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.waf.main_class.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.waf.main_class.delete(mkey='config-name')

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
