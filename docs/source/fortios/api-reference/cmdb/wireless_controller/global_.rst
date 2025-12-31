Global
======

Configuration endpoint for wireless_controller/global_.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.global_

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
   items = fgt.api.cmdb.wireless_controller.global_.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.global_.put(
       name='updated-value',
       location='updated-value',
       acd_process_count='updated-value',
       wpad_process_count='updated-value',
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
       name=None,
       location=None,
       acd_process_count=None,
       wpad_process_count=None,
       image_download=None,
       rolling_wtp_upgrade=None,
       rolling_wtp_upgrade_threshold=None,
       max_retransmit=None,
       control_message_offload=None,
       data_ethernet_II=None,
       link_aggregation=None,
       mesh_eth_type=None,
       # ... more parameters
   )

Update this specific resource.

