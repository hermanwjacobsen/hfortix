Setting
=======

Configuration endpoint for log/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.setting

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
   items = fgt.api.cmdb.log.setting.get()


   # Update existing item
   result = fgt.api.cmdb.log.setting.put(
       resolve_ip='updated-value',
       resolve_port='updated-value',
       log_user_in_upper='updated-value',
       fwpolicy_implicit_log='updated-value',
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
       resolve_ip=None,
       resolve_port=None,
       log_user_in_upper=None,
       fwpolicy_implicit_log=None,
       fwpolicy6_implicit_log=None,
       extended_log=None,
       local_in_allow=None,
       local_in_deny_unicast=None,
       local_in_deny_broadcast=None,
       local_in_policy_log=None,
       local_out=None,
       local_out_ioc_detection=None,
       # ... more parameters
   )

Update this specific resource.

