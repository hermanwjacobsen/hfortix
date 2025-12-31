Ospf6
=====

Configuration endpoint for router/ospf6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.ospf6

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
   items = fgt.api.cmdb.router.ospf6.get()


   # Update existing item
   result = fgt.api.cmdb.router.ospf6.put(
       abr_type='updated-value',
       auto_cost_ref_bandwidth='updated-value',
       default_information_originate='updated-value',
       log_neighbour_changes='updated-value',
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
       abr_type=None,
       auto_cost_ref_bandwidth=None,
       default_information_originate=None,
       log_neighbour_changes=None,
       default_information_metric=None,
       default_information_metric_type=None,
       default_information_route_map=None,
       default_metric=None,
       router_id=None,
       spf_timers=None,
       bfd=None,
       restart_mode=None,
       # ... more parameters
   )

Update this specific resource.

