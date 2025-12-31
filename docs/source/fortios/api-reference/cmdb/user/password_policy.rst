PasswordPolicy
==============

Configuration endpoint for user/password_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.password_policy

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.user.password_policy.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.password_policy.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.password_policy.post(
       nkey='value',  # optional
       name='value',  # optional
       expire_status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.password_policy.put(
       name='updated-value',
       expire_status='updated-value',
       expire_days='updated-value',
       warn_days='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.password_policy.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       name=None,
       expire_status=None,
       expire_days=None,
       warn_days=None,
       expired_password_renewal=None,
       minimum_length=None,
       min_lower_case_letter=None,
       min_upper_case_letter=None,
       min_non_alphanumeric=None,
       min_number=None,
       min_change_characters=None,
       reuse_password=None,
       reuse_password_limit=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       expire_status=None,
       expire_days=None,
       warn_days=None,
       expired_password_renewal=None,
       minimum_length=None,
       min_lower_case_letter=None,
       min_upper_case_letter=None,
       min_non_alphanumeric=None,
       min_number=None,
       min_change_characters=None,
       reuse_password=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

