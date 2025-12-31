SdnConnector
============

Configuration endpoint for system/sdn_connector.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.sdn_connector

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.sdn_connector.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.sdn_connector.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.sdn_connector.post(
       nkey='value',  # optional
       name='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.sdn_connector.put(
       name='updated-value',
       status='updated-value',
       type='updated-value',
       proxy='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.sdn_connector.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       name=None,
       status=None,
       type=None,
       proxy=None,
       use_metadata_iam=None,
       microsoft_365=None,
       ha_status=None,
       verify_certificate=None,
       server=None,
       server_list=None,
       server_port=None,
       message_server_port=None,
       username=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       type=None,
       proxy=None,
       use_metadata_iam=None,
       microsoft_365=None,
       ha_status=None,
       verify_certificate=None,
       server=None,
       server_list=None,
       server_port=None,
       message_server_port=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

