Ha
==

Configuration endpoint for system/ha.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ha

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.ha.get()


   # Update existing item
   result = fgt.api.cmdb.system.ha.put(
       group_id='updated-value',
       group_name='updated-value',
       mode='updated-value',
       sync_packet_balance='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       group_id=None,
       group_name=None,
       mode=None,
       sync_packet_balance=None,
       password=None,
       hbdev=None,
       auto_virtual_mac_interface=None,
       backup_hbdev=None,
       session_sync_dev=None,
       route_ttl=None,
       route_wait=None,
       route_hold=None,
       # ... more parameters
   )

Update this specific resource.

