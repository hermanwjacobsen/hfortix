Global
======

Configuration endpoint for ips/global_.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ips.global_

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
   items = fgt.api.cmdb.ips.global_.get()


   # Update existing item
   result = fgt.api.cmdb.ips.global_.put(
       fail_open='updated-value',
       database='updated-value',
       traffic_submit='updated-value',
       anomaly_mode='updated-value',
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
       fail_open=None,
       database=None,
       traffic_submit=None,
       anomaly_mode=None,
       session_limit_mode=None,
       socket_size=None,
       engine_count=None,
       sync_session_ttl=None,
       np_accel_mode=None,
       ips_reserve_cpu=None,
       cp_accel_mode=None,
       deep_app_insp_timeout=None,
       # ... more parameters
   )

Update this specific resource.

