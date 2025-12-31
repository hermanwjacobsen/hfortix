StormControl
============

Configuration endpoint for switch_controller/storm_control.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.storm_control

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
   items = fgt.api.cmdb.switch_controller.storm_control.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.storm_control.put(
       rate='updated-value',
       burst_size_level='updated-value',
       unknown_unicast='updated-value',
       unknown_multicast='updated-value',
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
       rate=None,
       burst_size_level=None,
       unknown_unicast=None,
       unknown_multicast=None,
       broadcast=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

