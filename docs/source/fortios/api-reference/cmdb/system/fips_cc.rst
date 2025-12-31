FipsCc
======

Configuration endpoint for system/fips_cc.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.fips_cc

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
   items = fgt.api.cmdb.system.fips_cc.get()


   # Update existing item
   result = fgt.api.cmdb.system.fips_cc.put(
       status='updated-value',
       self_test_period='updated-value',
       key_generation_self_test='updated-value',
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
       self_test_period=None,
       key_generation_self_test=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

