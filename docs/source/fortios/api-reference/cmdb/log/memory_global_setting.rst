MemoryGlobalSetting
===================

Configuration endpoint for log/memory_global_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.memory_global_setting

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
   items = fgt.api.cmdb.log.memory_global_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.memory_global_setting.put(
       max_size='updated-value',
       full_first_warning_threshold='updated-value',
       full_second_warning_threshold='updated-value',
       full_final_warning_threshold='updated-value',
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
       max_size=None,
       full_first_warning_threshold=None,
       full_second_warning_threshold=None,
       full_final_warning_threshold=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

