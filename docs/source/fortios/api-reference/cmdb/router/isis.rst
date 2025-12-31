Isis
====

Configuration endpoint for router/isis.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.isis

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
   items = fgt.api.cmdb.router.isis.get()


   # Update existing item
   result = fgt.api.cmdb.router.isis.put(
       is_type='updated-value',
       adv_passive_only='updated-value',
       adv_passive_only6='updated-value',
       auth_mode_l1='updated-value',
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
       is_type=None,
       adv_passive_only=None,
       adv_passive_only6=None,
       auth_mode_l1=None,
       auth_mode_l2=None,
       auth_password_l1=None,
       auth_password_l2=None,
       auth_keychain_l1=None,
       auth_keychain_l2=None,
       auth_sendonly_l1=None,
       auth_sendonly_l2=None,
       ignore_lsp_errors=None,
       # ... more parameters
   )

Update this specific resource.

