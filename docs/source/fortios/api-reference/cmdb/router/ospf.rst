Ospf
====

Configuration endpoint for router/ospf.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.ospf

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
   items = fgt.api.cmdb.router.ospf.get()


   # Update existing item
   result = fgt.api.cmdb.router.ospf.put(
       abr_type='updated-value',
       auto_cost_ref_bandwidth='updated-value',
       distance_external='updated-value',
       distance_inter_area='updated-value',
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
       distance_external=None,
       distance_inter_area=None,
       distance_intra_area=None,
       database_overflow=None,
       database_overflow_max_lsas=None,
       database_overflow_time_to_recover=None,
       default_information_originate=None,
       default_information_metric=None,
       default_information_metric_type=None,
       default_information_route_map=None,
       # ... more parameters
   )

Update this specific resource.

