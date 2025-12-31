Profile
=======

Configuration endpoint for webfilter/profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.webfilter.profile

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
   items = fgt.api.cmdb.webfilter.profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.webfilter.profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.webfilter.profile.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.webfilter.profile.put(
       name='updated-value',
       comment='updated-value',
       feature_set='updated-value',
       replacemsg_group='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.webfilter.profile.delete(name='item-name')


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
       comment=None,
       feature_set=None,
       replacemsg_group=None,
       options=None,
       https_replacemsg=None,
       web_flow_log_encoding=None,
       ovrd_perm=None,
       post_action=None,
       override=None,
       web=None,
       ftgd_wf=None,
       antiphish=None,
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
       comment=None,
       feature_set=None,
       replacemsg_group=None,
       options=None,
       https_replacemsg=None,
       web_flow_log_encoding=None,
       ovrd_perm=None,
       post_action=None,
       override=None,
       web=None,
       ftgd_wf=None,
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

