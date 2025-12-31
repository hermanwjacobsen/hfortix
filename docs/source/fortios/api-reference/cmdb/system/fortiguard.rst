Fortiguard
==========

Configuration endpoint for system/fortiguard.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.fortiguard

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
   items = fgt.api.cmdb.system.fortiguard.get()


   # Update existing item
   result = fgt.api.cmdb.system.fortiguard.put(
       fortiguard_anycast='updated-value',
       fortiguard_anycast_source='updated-value',
       protocol='updated-value',
       port='updated-value',
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
       fortiguard_anycast=None,
       fortiguard_anycast_source=None,
       protocol=None,
       port=None,
       service_account_id=None,
       load_balance_servers=None,
       auto_join_forticloud=None,
       update_server_location=None,
       sandbox_region=None,
       update_ffdb=None,
       update_uwdb=None,
       update_dldb=None,
       # ... more parameters
   )

Update this specific resource.

