SecurityPolicyLocalAccess
=========================

Configuration endpoint for switch_controller/security_policy_local_access.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.security_policy_local_access

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
   items = fgt.api.cmdb.switch_controller.security_policy_local_access.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.security_policy_local_access.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.security_policy_local_access.post(
       nkey='value',  # optional
       name='value',  # optional
       mgmt_allowaccess='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.security_policy_local_access.put(
       name='updated-value',
       mgmt_allowaccess='updated-value',
       internal_allowaccess='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.security_policy_local_access.delete(name='item-name')


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
       mgmt_allowaccess=None,
       internal_allowaccess=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       mgmt_allowaccess=None,
       internal_allowaccess=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

