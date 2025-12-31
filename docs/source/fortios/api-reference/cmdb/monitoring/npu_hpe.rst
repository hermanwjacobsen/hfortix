NpuHpe
======

Configuration endpoint for monitoring/npu_hpe.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.monitoring.npu_hpe

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
   items = fgt.api.cmdb.monitoring.npu_hpe.get()


   # Update existing item
   result = fgt.api.cmdb.monitoring.npu_hpe.put(
       status='updated-value',
       interval='updated-value',
       multipliers='updated-value',
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
       status=None,
       interval=None,
       multipliers=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

