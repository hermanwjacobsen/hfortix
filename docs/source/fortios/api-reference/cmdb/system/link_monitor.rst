LinkMonitor
===========

Configuration endpoint for system/link_monitor.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.link_monitor

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
   items = fgt.api.cmdb.system.link_monitor.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.link_monitor.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.link_monitor.post(
       nkey='value',  # optional
       name='value',  # optional
       addr_mode='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.link_monitor.put(
       name='updated-value',
       addr_mode='updated-value',
       srcintf='updated-value',
       server_config='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.link_monitor.delete(name='item-name')


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
       addr_mode=None,
       srcintf=None,
       server_config=None,
       server_type=None,
       server=None,
       protocol=None,
       port=None,
       gateway_ip=None,
       gateway_ip6=None,
       route=None,
       source_ip=None,
       source_ip6=None,
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
       addr_mode=None,
       srcintf=None,
       server_config=None,
       server_type=None,
       server=None,
       protocol=None,
       port=None,
       gateway_ip=None,
       gateway_ip6=None,
       route=None,
       source_ip=None,
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

