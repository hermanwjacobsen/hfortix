Npu
===

Configuration endpoint for system/npu.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.npu

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
   items = fgt.api.cmdb.system.npu.get()


   # Update existing item
   result = fgt.api.cmdb.system.npu.put(
       dedicated_management_cpu='updated-value',
       dedicated_management_affinity='updated-value',
       capwap_offload='updated-value',
       ipsec_mtu_override='updated-value',
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
       dedicated_management_cpu=None,
       dedicated_management_affinity=None,
       capwap_offload=None,
       ipsec_mtu_override=None,
       ipsec_ordering=None,
       ipsec_enc_subengine_mask=None,
       ipsec_dec_subengine_mask=None,
       priority_protocol=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

