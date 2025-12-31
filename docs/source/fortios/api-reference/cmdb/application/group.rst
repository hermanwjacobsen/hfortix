Group
=====

Configuration endpoint for application/group.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.application.group

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
   items = fgt.api.cmdb.application.group.get()

   # Get specific item by name
   item = fgt.api.cmdb.application.group.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.application.group.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.application.group.put(
       name='updated-value',
       comment='updated-value',
       type='updated-value',
       application='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.application.group.delete(name='item-name')


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
       comment=None,
       type=None,
       application=None,
       category=None,
       risk=None,
       protocols=None,
       vendor=None,
       technology=None,
       behavior=None,
       popularity=None,
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
       comment=None,
       type=None,
       application=None,
       category=None,
       risk=None,
       protocols=None,
       vendor=None,
       technology=None,
       behavior=None,
       popularity=None,
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

