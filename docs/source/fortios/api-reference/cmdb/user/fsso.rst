Fsso
====

Configuration endpoint for user/fsso.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.fsso

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
   items = fgt.api.cmdb.user.fsso.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.fsso.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.fsso.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.fsso.put(
       name='updated-value',
       type='updated-value',
       server='updated-value',
       port='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.fsso.delete(name='item-name')


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
       type=None,
       server=None,
       port=None,
       password=None,
       server2=None,
       port2=None,
       password2=None,
       server3=None,
       port3=None,
       password3=None,
       server4=None,
       port4=None,
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
       type=None,
       server=None,
       port=None,
       password=None,
       server2=None,
       port2=None,
       password2=None,
       server3=None,
       port3=None,
       password3=None,
       server4=None,
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

