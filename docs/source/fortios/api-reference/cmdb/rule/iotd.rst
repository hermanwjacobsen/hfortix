Iotd
====

Configuration endpoint for rule/iotd.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.rule.iotd

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
   items = fgt.api.cmdb.rule.iotd.get()

   # Get specific item by name
   item = fgt.api.cmdb.rule.iotd.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.rule.iotd.post(
       nkey='value',  # optional
       name='value',  # optional
       id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.rule.iotd.put(
       name='updated-value',
       id='updated-value',
       category='updated-value',
       popularity='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.rule.iotd.delete(name='item-name')


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
       id=None,
       category=None,
       popularity=None,
       risk=None,
       weight=None,
       protocol=None,
       technology=None,
       behavior=None,
       vendor=None,
       parameters=None,
       metadata=None,
       status=None,
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
       id=None,
       category=None,
       popularity=None,
       risk=None,
       weight=None,
       protocol=None,
       technology=None,
       behavior=None,
       vendor=None,
       parameters=None,
       metadata=None,
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

