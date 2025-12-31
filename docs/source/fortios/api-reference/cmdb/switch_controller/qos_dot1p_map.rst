QosDot1pMap
===========

Configuration endpoint for switch_controller/qos_dot1p_map.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.qos_dot1p_map

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
   items = fgt.api.cmdb.switch_controller.qos_dot1p_map.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.qos_dot1p_map.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.qos_dot1p_map.post(
       nkey='value',  # optional
       name='value',  # optional
       description='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.qos_dot1p_map.put(
       name='updated-value',
       description='updated-value',
       egress_pri_tagging='updated-value',
       priority_0='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.qos_dot1p_map.delete(name='item-name')


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
       description=None,
       egress_pri_tagging=None,
       priority_0=None,
       priority_1=None,
       priority_2=None,
       priority_3=None,
       priority_4=None,
       priority_5=None,
       priority_6=None,
       priority_7=None,
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
       description=None,
       egress_pri_tagging=None,
       priority_0=None,
       priority_1=None,
       priority_2=None,
       priority_3=None,
       priority_4=None,
       priority_5=None,
       priority_6=None,
       priority_7=None,
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

