Static6
=======

Configuration endpoint for router/static6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.static6

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
   items = fgt.api.cmdb.router.static6.get()


   # Create new item
   result = fgt.api.cmdb.router.static6.post(
       nkey='value',  # optional
       seq_num='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.router.static6.put(
       seq_num='updated-value',
       status='updated-value',
       dst='updated-value',
       gateway='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.router.static6.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       seq_num=None,
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
       seq_num=None,
       status=None,
       dst=None,
       gateway=None,
       device=None,
       devindex=None,
       distance=None,
       weight=None,
       priority=None,
       comment=None,
       blackhole=None,
       dynamic_gateway=None,
       sdwan_zone=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       seq_num=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       dst=None,
       gateway=None,
       device=None,
       devindex=None,
       distance=None,
       weight=None,
       priority=None,
       comment=None,
       blackhole=None,
       dynamic_gateway=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       seq_num=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

