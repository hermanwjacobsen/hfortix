DiskSetting
===========

Configuration endpoint for log/disk_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.disk_setting

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
   items = fgt.api.cmdb.log.disk_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.disk_setting.put(
       status='updated-value',
       ips_archive='updated-value',
       max_log_file_size='updated-value',
       max_policy_packet_capture_size='updated-value',
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
       ips_archive=None,
       max_log_file_size=None,
       max_policy_packet_capture_size=None,
       roll_schedule=None,
       roll_day=None,
       roll_time=None,
       diskfull=None,
       log_quota=None,
       dlp_archive_quota=None,
       report_quota=None,
       maximum_log_age=None,
       # ... more parameters
   )

Update this specific resource.

