Policy
======

Configuration endpoint for router/policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.policy

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.router.policy.get()


   # Create new item
   result = fgt.api.cmdb.router.policy.post(
       nkey='value',  # optional
       seq_num='value',  # optional
       input_device='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.router.policy.put(
       seq_num='updated-value',
       input_device='updated-value',
       input_device_negate='updated-value',
       src='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.router.policy.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       seq_num=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       seq_num=None,
       input_device=None,
       input_device_negate=None,
       src=None,
       srcaddr=None,
       src_negate=None,
       dst=None,
       dstaddr=None,
       dst_negate=None,
       protocol=None,
       start_port=None,
       end_port=None,
       start_source_port=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       seq_num=None,
       payload_dict=None,
       before=None,
       after=None,
       input_device=None,
       input_device_negate=None,
       src=None,
       srcaddr=None,
       src_negate=None,
       dst=None,
       dstaddr=None,
       dst_negate=None,
       protocol=None,
       start_port=None,
       end_port=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       seq_num=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

