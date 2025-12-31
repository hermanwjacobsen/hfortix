ApcfgProfile
============

Configuration endpoint for wireless_controller/apcfg_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.apcfg_profile

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
   items = fgt.api.cmdb.wireless_controller.apcfg_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.apcfg_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.apcfg_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       ap_family='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.apcfg_profile.put(
       name='updated-value',
       ap_family='updated-value',
       comment='updated-value',
       ac_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.apcfg_profile.delete(name='item-name')


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
       ap_family=None,
       comment=None,
       ac_type=None,
       ac_timer=None,
       ac_ip=None,
       ac_port=None,
       command_list=None,
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
       ap_family=None,
       comment=None,
       ac_type=None,
       ac_timer=None,
       ac_ip=None,
       ac_port=None,
       command_list=None,
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

