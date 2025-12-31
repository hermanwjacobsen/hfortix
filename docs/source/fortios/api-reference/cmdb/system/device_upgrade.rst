DeviceUpgrade
=============

Configuration endpoint for system/device_upgrade.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.device_upgrade

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
   items = fgt.api.cmdb.system.device_upgrade.get()


   # Create new item
   result = fgt.api.cmdb.system.device_upgrade.post(
       nkey='value',  # optional
       status='value',  # optional
       ha_reboot_controller='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.device_upgrade.put(
       serial='updated-value',
       status='updated-value',
       ha_reboot_controller='updated-value',
       next_path_index='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.device_upgrade.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       serial=None,
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
       status=None,
       ha_reboot_controller=None,
       next_path_index=None,
       known_ha_members=None,
       initial_version=None,
       starter_admin=None,
       serial=None,
       timing=None,
       maximum_minutes=None,
       time=None,
       setup_time=None,
       upgrade_path=None,
       device_type=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       serial=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       ha_reboot_controller=None,
       next_path_index=None,
       known_ha_members=None,
       initial_version=None,
       starter_admin=None,
       timing=None,
       maximum_minutes=None,
       time=None,
       setup_time=None,
       upgrade_path=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       serial=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

