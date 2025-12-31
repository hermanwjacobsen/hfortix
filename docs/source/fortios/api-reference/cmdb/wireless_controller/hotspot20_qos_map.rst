Hotspot20QosMap
===============

Configuration endpoint for wireless_controller/hotspot20_qos_map.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.hotspot20_qos_map

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
   items = fgt.api.cmdb.wireless_controller.hotspot20_qos_map.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.hotspot20_qos_map.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.hotspot20_qos_map.post(
       nkey='value',  # optional
       name='value',  # optional
       dscp_except='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.hotspot20_qos_map.put(
       name='updated-value',
       dscp_except='updated-value',
       dscp_range='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.hotspot20_qos_map.delete(name='item-name')


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
       dscp_except=None,
       dscp_range=None,
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
       dscp_except=None,
       dscp_range=None,
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

