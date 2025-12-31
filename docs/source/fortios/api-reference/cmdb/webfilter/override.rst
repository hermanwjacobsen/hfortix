Override
========

Configuration endpoint for webfilter/override.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.webfilter.override

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
   items = fgt.api.cmdb.webfilter.override.get()


   # Create new item
   result = fgt.api.cmdb.webfilter.override.post(
       nkey='value',  # optional
       id='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.webfilter.override.put(
       id='updated-value',
       status='updated-value',
       ip='updated-value',
       user='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.webfilter.override.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id=None,
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
       id=None,
       status=None,
       ip=None,
       user=None,
       user_group=None,
       old_profile=None,
       new_profile=None,
       ip6=None,
       expires=None,
       initiator=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       id=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       ip=None,
       user=None,
       user_group=None,
       old_profile=None,
       new_profile=None,
       ip6=None,
       expires=None,
       initiator=None,
       vdom=None,
       raw_json=False,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

