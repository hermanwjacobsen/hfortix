InterController
===============

Configuration endpoint for wireless_controller/inter_controller.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.inter_controller

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
   items = fgt.api.cmdb.wireless_controller.inter_controller.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.inter_controller.put(
       inter_controller_mode='updated-value',
       l3_roaming='updated-value',
       inter_controller_key='updated-value',
       inter_controller_pri='updated-value',
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
       inter_controller_mode=None,
       l3_roaming=None,
       inter_controller_key=None,
       inter_controller_pri=None,
       fast_failover_max=None,
       fast_failover_wait=None,
       inter_controller_peer=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

