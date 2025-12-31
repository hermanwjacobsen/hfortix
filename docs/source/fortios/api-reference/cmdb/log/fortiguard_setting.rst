FortiguardSetting
=================

Configuration endpoint for log/fortiguard_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.fortiguard_setting

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
   items = fgt.api.cmdb.log.fortiguard_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.fortiguard_setting.put(
       status='updated-value',
       upload_option='updated-value',
       upload_interval='updated-value',
       upload_day='updated-value',
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
       upload_option=None,
       upload_interval=None,
       upload_day=None,
       upload_time=None,
       priority=None,
       max_log_rate=None,
       access_config=None,
       enc_algorithm=None,
       ssl_min_proto_version=None,
       conn_timeout=None,
       source_ip=None,
       # ... more parameters
   )

Update this specific resource.

