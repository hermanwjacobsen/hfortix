TrafficSniffer
==============

Configuration endpoint for switch_controller/traffic_sniffer.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.traffic_sniffer

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
   items = fgt.api.cmdb.switch_controller.traffic_sniffer.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.traffic_sniffer.put(
       mode='updated-value',
       erspan_ip='updated-value',
       target_mac='updated-value',
       target_ip='updated-value',
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
       mode=None,
       erspan_ip=None,
       target_mac=None,
       target_ip=None,
       target_port=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

