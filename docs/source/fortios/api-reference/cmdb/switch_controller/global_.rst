Global
======

Configuration endpoint for switch_controller/global_.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.global_

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
   items = fgt.api.cmdb.switch_controller.global_.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.global_.put(
       mac_aging_interval='updated-value',
       https_image_push='updated-value',
       vlan_all_mode='updated-value',
       vlan_optimization='updated-value',
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
       mac_aging_interval=None,
       https_image_push=None,
       vlan_all_mode=None,
       vlan_optimization=None,
       vlan_identity=None,
       disable_discovery=None,
       mac_retention_period=None,
       default_virtual_switch_vlan=None,
       dhcp_server_access_list=None,
       dhcp_option82_format=None,
       dhcp_option82_circuit_id=None,
       dhcp_option82_remote_id=None,
       # ... more parameters
   )

Update this specific resource.

