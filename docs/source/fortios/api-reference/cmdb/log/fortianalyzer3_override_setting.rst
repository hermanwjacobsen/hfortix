Fortianalyzer3OverrideSetting
=============================

Configuration endpoint for log/fortianalyzer3_override_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.fortianalyzer3_override_setting

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
   items = fgt.api.cmdb.log.fortianalyzer3_override_setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.fortianalyzer3_override_setting.put(
       use_management_vdom='updated-value',
       status='updated-value',
       ips_archive='updated-value',
       server='updated-value',
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
       use_management_vdom=None,
       status=None,
       ips_archive=None,
       server=None,
       alt_server=None,
       fallback_to_primary=None,
       certificate_verification=None,
       serial=None,
       server_cert_ca=None,
       preshared_key=None,
       access_config=None,
       hmac_algorithm=None,
       # ... more parameters
   )

Update this specific resource.

