WebPortal
=========

Configuration endpoint for ztna/web_portal.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ztna.web_portal

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
   items = fgt.api.cmdb.ztna.web_portal.get()

   # Get specific item by name
   item = fgt.api.cmdb.ztna.web_portal.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.ztna.web_portal.post(
       nkey='value',  # optional
       name='value',  # optional
       vip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ztna.web_portal.put(
       name='updated-value',
       vip='updated-value',
       host='updated-value',
       decrypted_traffic_mirror='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ztna.web_portal.delete(name='item-name')


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
       vip=None,
       host=None,
       decrypted_traffic_mirror=None,
       log_blocked_traffic=None,
       auth_portal=None,
       auth_virtual_host=None,
       vip6=None,
       auth_rule=None,
       display_bookmark=None,
       focus_bookmark=None,
       display_status=None,
       display_history=None,
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
       vip=None,
       host=None,
       decrypted_traffic_mirror=None,
       log_blocked_traffic=None,
       auth_portal=None,
       auth_virtual_host=None,
       vip6=None,
       auth_rule=None,
       display_bookmark=None,
       focus_bookmark=None,
       display_status=None,
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

