FortiguardOverrideFilter
========================

Configuration endpoint for log/fortiguard_override_filter.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.fortiguard_override_filter

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
   items = fgt.api.cmdb.log.fortiguard_override_filter.get()


   # Update existing item
   result = fgt.api.cmdb.log.fortiguard_override_filter.put(
       severity='updated-value',
       forward_traffic='updated-value',
       local_traffic='updated-value',
       multicast_traffic='updated-value',
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
       severity=None,
       forward_traffic=None,
       local_traffic=None,
       multicast_traffic=None,
       sniffer_traffic=None,
       ztna_traffic=None,
       http_transaction=None,
       anomaly=None,
       voip=None,
       forti_switch=None,
       free_style=None,
       vdom=None,
       # ... more parameters
   )

Update this specific resource.

