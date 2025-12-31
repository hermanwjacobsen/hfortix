ExternalResource
================

Configuration endpoint for system/external_resource.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.external_resource

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
   items = fgt.api.cmdb.system.external_resource.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.external_resource.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.external_resource.post(
       nkey='value',  # optional
       name='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.external_resource.put(
       name='updated-value',
       uuid='updated-value',
       status='updated-value',
       type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.external_resource.delete(name='item-name')


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
       uuid=None,
       status=None,
       type=None,
       namespace=None,
       object_array_path=None,
       address_name_field=None,
       address_data_field=None,
       address_comment_field=None,
       update_method=None,
       category=None,
       username=None,
       password=None,
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
       uuid=None,
       status=None,
       type=None,
       namespace=None,
       object_array_path=None,
       address_name_field=None,
       address_data_field=None,
       address_comment_field=None,
       update_method=None,
       category=None,
       username=None,
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

