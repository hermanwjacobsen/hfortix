Rule
====

Configuration endpoint for ips/rule.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ips.rule

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
   items = fgt.api.cmdb.ips.rule.get()

   # Get specific item by name
   item = fgt.api.cmdb.ips.rule.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.ips.rule.post(
       nkey='value',  # optional
       name='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ips.rule.put(
       name='updated-value',
       status='updated-value',
       log='updated-value',
       log_packet='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ips.rule.delete(name='item-name')


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
       status=None,
       log=None,
       log_packet=None,
       group=None,
       severity=None,
       location=None,
       os=None,
       application=None,
       service=None,
       rule_id=None,
       rev=None,
       date=None,
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
       status=None,
       log=None,
       log_packet=None,
       group=None,
       severity=None,
       location=None,
       os=None,
       application=None,
       service=None,
       rule_id=None,
       rev=None,
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

