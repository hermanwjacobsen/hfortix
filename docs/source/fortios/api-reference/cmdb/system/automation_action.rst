AutomationAction
================

Configuration endpoint for system/automation_action.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.automation_action

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
   items = fgt.api.cmdb.system.automation_action.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.automation_action.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.automation_action.post(
       nkey='value',  # optional
       name='value',  # optional
       description='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.automation_action.put(
       name='updated-value',
       description='updated-value',
       action_type='updated-value',
       system_action='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.automation_action.delete(name='item-name')


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
       description=None,
       action_type=None,
       system_action=None,
       tls_certificate=None,
       forticare_email=None,
       email_to=None,
       email_from=None,
       email_subject=None,
       minimum_interval=None,
       aws_api_key=None,
       azure_function_authorization=None,
       azure_api_key=None,
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
       description=None,
       action_type=None,
       system_action=None,
       tls_certificate=None,
       forticare_email=None,
       email_to=None,
       email_from=None,
       email_subject=None,
       minimum_interval=None,
       aws_api_key=None,
       azure_function_authorization=None,
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

