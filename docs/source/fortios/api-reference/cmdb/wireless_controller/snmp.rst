Snmp
====

Configuration endpoint for wireless_controller/snmp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.snmp

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
   items = fgt.api.cmdb.wireless_controller.snmp.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.snmp.put(
       engine_id='updated-value',
       contact_info='updated-value',
       trap_high_cpu_threshold='updated-value',
       trap_high_mem_threshold='updated-value',
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
       engine_id=None,
       contact_info=None,
       trap_high_cpu_threshold=None,
       trap_high_mem_threshold=None,
       community=None,
       user=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

