Layout
======

Configuration endpoint for report/layout.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.report.layout

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
   items = fgt.api.cmdb.report.layout.get()

   # Get specific item by name
   item = fgt.api.cmdb.report.layout.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.report.layout.post(
       nkey='value',  # optional
       name='value',  # optional
       title='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.report.layout.put(
       name='updated-value',
       title='updated-value',
       subtitle='updated-value',
       description='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.report.layout.delete(name='item-name')


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
       title=None,
       subtitle=None,
       description=None,
       style_theme=None,
       options=None,
       schedule_type=None,
       day=None,
       time=None,
       cutoff_option=None,
       cutoff_time=None,
       email_send=None,
       email_recipients=None,
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
       title=None,
       subtitle=None,
       description=None,
       style_theme=None,
       options=None,
       schedule_type=None,
       day=None,
       time=None,
       cutoff_option=None,
       cutoff_time=None,
       email_send=None,
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

