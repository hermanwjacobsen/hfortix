FlowTracking
============

Configuration endpoint for switch_controller/flow_tracking.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.flow_tracking

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
   items = fgt.api.cmdb.switch_controller.flow_tracking.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.flow_tracking.put(
       sample_mode='updated-value',
       sample_rate='updated-value',
       collectors='updated-value',
       level='updated-value',
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
       sample_mode=None,
       sample_rate=None,
       collectors=None,
       level=None,
       max_export_pkt_size=None,
       template_export_period=None,
       timeout_general=None,
       timeout_icmp=None,
       timeout_max=None,
       timeout_tcp=None,
       timeout_tcp_fin=None,
       timeout_tcp_rst=None,
       # ... more parameters
   )

Update this specific resource.

