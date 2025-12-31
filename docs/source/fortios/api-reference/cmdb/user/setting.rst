Setting
=======

Configuration endpoint for user/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.setting

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
   items = fgt.api.cmdb.user.setting.get()


   # Update existing item
   result = fgt.api.cmdb.user.setting.put(
       auth_type='updated-value',
       auth_cert='updated-value',
       auth_ca_cert='updated-value',
       auth_secure_http='updated-value',
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
       auth_type=None,
       auth_cert=None,
       auth_ca_cert=None,
       auth_secure_http=None,
       auth_http_basic=None,
       auth_ssl_allow_renegotiation=None,
       auth_src_mac=None,
       auth_on_demand=None,
       auth_timeout=None,
       auth_timeout_type=None,
       auth_portal_timeout=None,
       radius_ses_timeout_act=None,
       # ... more parameters
   )

Update this specific resource.

