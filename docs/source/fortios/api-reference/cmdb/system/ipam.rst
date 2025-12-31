Ipam
====

Configuration endpoint for system/ipam.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ipam

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
   items = fgt.api.cmdb.system.ipam.get()


   # Update existing item
   result = fgt.api.cmdb.system.ipam.put(
       status='updated-value',
       server_type='updated-value',
       automatic_conflict_resolution='updated-value',
       require_subnet_size_match='updated-value',
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
       status=None,
       server_type=None,
       automatic_conflict_resolution=None,
       require_subnet_size_match=None,
       manage_lan_addresses=None,
       manage_lan_extension_addresses=None,
       manage_ssid_addresses=None,
       pools=None,
       rules=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

