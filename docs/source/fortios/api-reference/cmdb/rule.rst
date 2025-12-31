Rule
====

Show FMWP signatures configuration and management.

Overview
--------

The ``cmdb.rule`` category provides configuration management for:

- **Fmwp** - Show FMWP signatures.
- **Iotd** - Show IOT detection signatures.
- **Otdt** - Show OT detection signatures.
- **Otvp** - Show OT patch signatures.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.rule

Available Endpoints
-------------------

**fmwp**
   Show FMWP signatures.
   
   .. code-block:: python
   
      # List all fmwp
      items = fgt.api.cmdb.rule.fmwp.get()
      
      # Get specific fmwp
      item = fgt.api.cmdb.rule.fmwp.get(mkey='name')

**iotd**
   Show IOT detection signatures.
   
   .. code-block:: python
   
      # List all iotd
      items = fgt.api.cmdb.rule.iotd.get()
      
      # Get specific iotd
      item = fgt.api.cmdb.rule.iotd.get(mkey='name')

**otdt**
   Show OT detection signatures.
   
   .. code-block:: python
   
      # List all otdt
      items = fgt.api.cmdb.rule.otdt.get()
      
      # Get specific otdt
      item = fgt.api.cmdb.rule.otdt.get(mkey='name')

**otvp**
   Show OT patch signatures.
   
   .. code-block:: python
   
      # List all otvp
      items = fgt.api.cmdb.rule.otvp.get()
      
      # Get specific otvp
      item = fgt.api.cmdb.rule.otvp.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.rule.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.rule.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.rule.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.rule.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.rule.{endpoint}.delete(mkey='config-name')

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
