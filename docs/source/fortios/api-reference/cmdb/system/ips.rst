Ips
===

Configuration endpoint for system/ips.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ips

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
   items = fgt.api.cmdb.system.ips.get()


   # Update existing item
   result = fgt.api.cmdb.system.ips.put(
       signature_hold_time='updated-value',
       override_signature_hold_by_id='updated-value',
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
       signature_hold_time=None,
       override_signature_hold_by_id=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

