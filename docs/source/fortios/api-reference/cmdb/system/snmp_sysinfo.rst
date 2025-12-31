SnmpSysinfo
===========

Configuration endpoint for system/snmp_sysinfo.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.snmp_sysinfo

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
   items = fgt.api.cmdb.system.snmp_sysinfo.get()


   # Update existing item
   result = fgt.api.cmdb.system.snmp_sysinfo.put(
       status='updated-value',
       engine_id_type='updated-value',
       engine_id='updated-value',
       description='updated-value',
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
       engine_id_type=None,
       engine_id=None,
       description=None,
       contact_info=None,
       location=None,
       trap_high_cpu_threshold=None,
       trap_low_memory_threshold=None,
       trap_log_full_threshold=None,
       trap_free_memory_threshold=None,
       trap_freeable_memory_threshold=None,
       append_index=None,
       # ... more parameters
   )

Update this specific resource.

