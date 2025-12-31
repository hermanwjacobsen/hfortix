FederatedUpgrade
================

Configuration endpoint for system/federated_upgrade.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.federated_upgrade

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.federated_upgrade.get()


   # Update existing item
   result = fgt.api.cmdb.system.federated_upgrade.put(
       status='updated-value',
       source='updated-value',
       failure_reason='updated-value',
       failure_device='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       source=None,
       failure_reason=None,
       failure_device=None,
       upgrade_id=None,
       next_path_index=None,
       ignore_signing_errors=None,
       ha_reboot_controller=None,
       known_ha_members=None,
       initial_version=None,
       starter_admin=None,
       node_list=None,
       # ... more parameters
   )

Update this specific resource.

