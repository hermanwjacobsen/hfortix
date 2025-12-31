DataType
========

Configuration endpoint for dlp/data_type.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.dlp.data_type

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
   items = fgt.api.cmdb.dlp.data_type.get()

   # Get specific item by name
   item = fgt.api.cmdb.dlp.data_type.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.dlp.data_type.post(
       nkey='value',  # optional
       name='value',  # optional
       verify='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.dlp.data_type.put(
       name='updated-value',
       verify='updated-value',
       verify2='updated-value',
       match_around='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.dlp.data_type.delete(name='item-name')


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
       verify=None,
       verify2=None,
       match_around=None,
       look_back=None,
       look_ahead=None,
       match_back=None,
       match_ahead=None,
       transform=None,
       verify_transformed_pattern=None,
       comment=None,
       vdom=None,
       raw_json=False,
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
       verify=None,
       verify2=None,
       match_around=None,
       look_back=None,
       look_ahead=None,
       match_back=None,
       match_ahead=None,
       transform=None,
       verify_transformed_pattern=None,
       comment=None,
       vdom=None,
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

