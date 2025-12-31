CentralManagement
=================

Configuration endpoint for system/central_management.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.central_management

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
   items = fgt.api.cmdb.system.central_management.get()


   # Update existing item
   result = fgt.api.cmdb.system.central_management.put(
       mode='updated-value',
       type='updated-value',
       fortigate_cloud_sso_default_profile='updated-value',
       schedule_config_restore='updated-value',
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
       mode=None,
       type=None,
       fortigate_cloud_sso_default_profile=None,
       schedule_config_restore=None,
       schedule_script_restore=None,
       allow_push_configuration=None,
       allow_push_firmware=None,
       allow_remote_firmware_upgrade=None,
       allow_monitor=None,
       serial_number=None,
       fmg=None,
       fmg_source_ip=None,
       # ... more parameters
   )

Update this specific resource.

