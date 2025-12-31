SnmpTrapThreshold
=================

Configuration endpoint for switch_controller/snmp_trap_threshold.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.snmp_trap_threshold

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
   items = fgt.api.cmdb.switch_controller.snmp_trap_threshold.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.snmp_trap_threshold.put(
       trap_high_cpu_threshold='updated-value',
       trap_low_memory_threshold='updated-value',
       trap_log_full_threshold='updated-value',
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
       trap_high_cpu_threshold=None,
       trap_low_memory_threshold=None,
       trap_log_full_threshold=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

