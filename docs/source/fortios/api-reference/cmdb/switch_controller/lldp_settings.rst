LldpSettings
============

Configuration endpoint for switch_controller/lldp_settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.lldp_settings

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
   items = fgt.api.cmdb.switch_controller.lldp_settings.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.lldp_settings.put(
       tx_hold='updated-value',
       tx_interval='updated-value',
       fast_start_interval='updated-value',
       management_interface='updated-value',
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
       tx_hold=None,
       tx_interval=None,
       fast_start_interval=None,
       management_interface=None,
       device_detection=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

