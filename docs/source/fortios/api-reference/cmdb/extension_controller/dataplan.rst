Dataplan
========

Configuration endpoint for extension_controller/dataplan.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.extension_controller.dataplan

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
   items = fgt.api.cmdb.extension_controller.dataplan.get()

   # Get specific item by name
   item = fgt.api.cmdb.extension_controller.dataplan.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.extension_controller.dataplan.post(
       nkey='value',  # optional
       name='value',  # optional
       modem_id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.extension_controller.dataplan.put(
       name='updated-value',
       modem_id='updated-value',
       type='updated-value',
       slot='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.extension_controller.dataplan.delete(name='item-name')


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
       modem_id=None,
       type=None,
       slot=None,
       iccid=None,
       carrier=None,
       apn=None,
       auth_type=None,
       username=None,
       password=None,
       pdn=None,
       signal_threshold=None,
       signal_period=None,
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
       modem_id=None,
       type=None,
       slot=None,
       iccid=None,
       carrier=None,
       apn=None,
       auth_type=None,
       username=None,
       password=None,
       pdn=None,
       signal_threshold=None,
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

