PasswordPolicy
==============

Configuration endpoint for system/password_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.password_policy

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
   items = fgt.api.cmdb.system.password_policy.get()


   # Update existing item
   result = fgt.api.cmdb.system.password_policy.put(
       status='updated-value',
       apply_to='updated-value',
       minimum_length='updated-value',
       min_lower_case_letter='updated-value',
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
       apply_to=None,
       minimum_length=None,
       min_lower_case_letter=None,
       min_upper_case_letter=None,
       min_non_alphanumeric=None,
       min_number=None,
       expire_status=None,
       expire_day=None,
       reuse_password=None,
       reuse_password_limit=None,
       login_lockout_upon_weaker_encryption=None,
       # ... more parameters
   )

Update this specific resource.

