IgmpSnooping
============

Configuration endpoint for switch_controller/igmp_snooping.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.igmp_snooping

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
   items = fgt.api.cmdb.switch_controller.igmp_snooping.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.igmp_snooping.put(
       aging_time='updated-value',
       flood_unknown_multicast='updated-value',
       query_interval='updated-value',
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
       aging_time=None,
       flood_unknown_multicast=None,
       query_interval=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

