SyslogdSetting
==============

Configuration endpoint for log/syslogd_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.syslogd_setting

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
   items = fgt.api.cmdb.log.syslogd_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.syslogd_setting.put(
       status='updated-value',
       server='updated-value',
       mode='updated-value',
       port='updated-value',
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
       server=None,
       mode=None,
       port=None,
       facility=None,
       source_ip_interface=None,
       source_ip=None,
       priority=None,
       max_log_rate=None,
       enc_algorithm=None,
       ssl_min_proto_version=None,
       certificate=None,
       # ... more parameters
   )

Update this specific resource.

