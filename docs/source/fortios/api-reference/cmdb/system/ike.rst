Ike
===

Configuration endpoint for system/ike.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ike

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
   items = fgt.api.cmdb.system.ike.get()


   # Update existing item
   result = fgt.api.cmdb.system.ike.put(
       embryonic_limit='updated-value',
       dh_multiprocess='updated-value',
       dh_worker_count='updated-value',
       dh_mode='updated-value',
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
       embryonic_limit=None,
       dh_multiprocess=None,
       dh_worker_count=None,
       dh_mode=None,
       dh_keypair_cache=None,
       dh_keypair_count=None,
       dh_keypair_throttle=None,
       dh_group_1=None,
       dh_group_2=None,
       dh_group_5=None,
       dh_group_14=None,
       dh_group_15=None,
       # ... more parameters
   )

Update this specific resource.

