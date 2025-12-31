Report
======

Report layout configuration configuration and management.

Overview
--------

The ``cmdb.report`` category provides configuration management for:

- :ref:`Layout <report-layout>` - Report layout configuration.
- :ref:`Setting <report-setting>` - Report setting configuration.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.report

Available Endpoints
-------------------

.. _report-layout:

layout
~~~~~~

Report layout configuration.

**Python attribute:** ``layout``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.report.layout.get()
   
   # Get specific item
   item = fgt.api.cmdb.report.layout.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.report.layout.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.report.layout.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.report.layout.delete(mkey='item-name')

.. _report-setting:

setting
~~~~~~~

Report setting configuration.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.report.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.report.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.report.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.report.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.report.setting.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.report.layout.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.report.layout.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.report.layout.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.report.layout.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.report.layout.delete(mkey='config-name')

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
