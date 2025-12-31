AutomationTrigger
=================

Configuration endpoint for system/automation_trigger.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.automation_trigger

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
   items = fgt.api.cmdb.system.automation_trigger.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.automation_trigger.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.automation_trigger.post(
       nkey='value',  # optional
       name='value',  # optional
       description='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.automation_trigger.put(
       name='updated-value',
       description='updated-value',
       trigger_type='updated-value',
       event_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.automation_trigger.delete(name='item-name')


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
       trigger_type=None,
       event_type=None,
       license_type=None,
       report_type=None,
       stitch_name=None,
       logid=None,
       trigger_frequency=None,
       trigger_weekday=None,
       trigger_day=None,
       trigger_hour=None,
       trigger_minute=None,
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
       trigger_type=None,
       event_type=None,
       license_type=None,
       report_type=None,
       stitch_name=None,
       logid=None,
       trigger_frequency=None,
       trigger_weekday=None,
       trigger_day=None,
       trigger_hour=None,
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

