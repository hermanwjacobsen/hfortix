Setting
=======

Configuration endpoint for authentication/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.authentication.setting

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
   items = fgt.api.cmdb.authentication.setting.get()


   # Update existing item
   result = fgt.api.cmdb.authentication.setting.put(
       active_auth_scheme='updated-value',
       sso_auth_scheme='updated-value',
       update_time='updated-value',
       persistent_cookie='updated-value',
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
       active_auth_scheme=None,
       sso_auth_scheme=None,
       update_time=None,
       persistent_cookie=None,
       ip_auth_cookie=None,
       cookie_max_age=None,
       cookie_refresh_div=None,
       captive_portal_type=None,
       captive_portal_ip=None,
       captive_portal_ip6=None,
       captive_portal=None,
       captive_portal6=None,
       # ... more parameters
   )

Update this specific resource.

