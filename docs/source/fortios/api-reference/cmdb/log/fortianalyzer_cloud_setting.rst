FortianalyzerCloudSetting
=========================

Configuration endpoint for log/fortianalyzer_cloud_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.fortianalyzer_cloud_setting

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
   items = fgt.api.cmdb.log.fortianalyzer_cloud_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.fortianalyzer_cloud_setting.put(
       status='updated-value',
       ips_archive='updated-value',
       certificate_verification='updated-value',
       serial='updated-value',
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
       certificate_verification=None,
       serial=None,
       preshared_key=None,
       access_config=None,
       hmac_algorithm=None,
       enc_algorithm=None,
       ssl_min_proto_version=None,
       conn_timeout=None,
       monitor_keepalive_period=None,
       monitor_failure_retry_period=None,
       # ... more parameters
   )

Update this specific resource.

