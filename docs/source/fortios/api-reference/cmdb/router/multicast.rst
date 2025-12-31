Multicast
=========

Configuration endpoint for router/multicast.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.multicast

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
   items = fgt.api.cmdb.router.multicast.get()


   # Update existing item
   result = fgt.api.cmdb.router.multicast.put(
       route_threshold='updated-value',
       route_limit='updated-value',
       multicast_routing='updated-value',
       pim_sm_global='updated-value',
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
       route_threshold=None,
       route_limit=None,
       multicast_routing=None,
       pim_sm_global=None,
       pim_sm_global_vrf=None,
       interface=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

