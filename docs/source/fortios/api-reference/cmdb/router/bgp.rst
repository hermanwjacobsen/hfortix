Bgp
===

Configuration endpoint for router/bgp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.bgp

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
   items = fgt.api.cmdb.router.bgp.get()


   # Update existing item
   result = fgt.api.cmdb.router.bgp.put(
       as_='updated-value',
       router_id='updated-value',
       keepalive_timer='updated-value',
       holdtime_timer='updated-value',
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
       as_=None,
       router_id=None,
       keepalive_timer=None,
       holdtime_timer=None,
       always_compare_med=None,
       bestpath_as_path_ignore=None,
       bestpath_cmp_confed_aspath=None,
       bestpath_cmp_routerid=None,
       bestpath_med_confed=None,
       bestpath_med_missing_as_worst=None,
       client_to_client_reflection=None,
       dampening=None,
       # ... more parameters
   )

Update this specific resource.

