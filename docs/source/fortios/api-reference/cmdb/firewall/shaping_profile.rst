ShapingProfile
==============

Configuration endpoint for firewall/shaping_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.shaping_profile

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
   items = fgt.api.cmdb.firewall.shaping_profile.get()


   # Create new item
   result = fgt.api.cmdb.firewall.shaping_profile.post(
       nkey='value',  # optional
       profile_name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.shaping_profile.put(
       profile_name='updated-value',
       comment='updated-value',
       type='updated-value',
       npu_offloading='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.shaping_profile.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       profile_name=None,
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
       profile_name=None,
       comment=None,
       type=None,
       npu_offloading=None,
       default_class_id=None,
       shaping_entries=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       profile_name=None,
       payload_dict=None,
       before=None,
       after=None,
       comment=None,
       type=None,
       npu_offloading=None,
       default_class_id=None,
       shaping_entries=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       profile_name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

