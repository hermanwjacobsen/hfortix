Interface
=========

Configuration endpoint for system/interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.interface

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
   items = fgt.api.cmdb.system.interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.interface.post(
       nkey='value',  # optional
       name='value',  # optional
       vrf='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.interface.put(
       name='updated-value',
       vrf='updated-value',
       cli_conn_status='updated-value',
       fortilink='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.interface.delete(name='item-name')


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
       vrf=None,
       cli_conn_status=None,
       fortilink=None,
       switch_controller_source_ip=None,
       mode=None,
       client_options=None,
       distance=None,
       priority=None,
       dhcp_relay_interface_select_method=None,
       dhcp_relay_interface=None,
       dhcp_relay_vrf_select=None,
       dhcp_broadcast_flag=None,
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
       vrf=None,
       cli_conn_status=None,
       fortilink=None,
       switch_controller_source_ip=None,
       mode=None,
       client_options=None,
       distance=None,
       priority=None,
       dhcp_relay_interface_select_method=None,
       dhcp_relay_interface=None,
       dhcp_relay_vrf_select=None,
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

