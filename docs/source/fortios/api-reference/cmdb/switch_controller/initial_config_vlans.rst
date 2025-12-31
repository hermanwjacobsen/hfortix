InitialConfigVlans
==================

Configuration endpoint for switch_controller/initial_config_vlans.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.initial_config_vlans

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
   items = fgt.api.cmdb.switch_controller.initial_config_vlans.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.initial_config_vlans.put(
       optional_vlans='updated-value',
       default_vlan='updated-value',
       quarantine='updated-value',
       rspan='updated-value',
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
       optional_vlans=None,
       default_vlan=None,
       quarantine=None,
       rspan=None,
       voice=None,
       video=None,
       nac=None,
       nac_segment=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

