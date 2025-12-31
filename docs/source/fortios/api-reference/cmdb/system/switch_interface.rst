SwitchInterface
===============

Configuration endpoint for system/switch_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.switch_interface

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
   items = fgt.api.cmdb.system.switch_interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.switch_interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.switch_interface.post(
       nkey='value',  # optional
       name='value',  # optional
       span_dest_port='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.switch_interface.put(
       name='updated-value',
       span_dest_port='updated-value',
       span_source_port='updated-value',
       member='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.switch_interface.delete(name='item-name')


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
       span_dest_port=None,
       span_source_port=None,
       member=None,
       type=None,
       intra_switch_policy=None,
       mac_ttl=None,
       span=None,
       span_direction=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       span_dest_port=None,
       span_source_port=None,
       member=None,
       type=None,
       intra_switch_policy=None,
       mac_ttl=None,
       span=None,
       span_direction=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

