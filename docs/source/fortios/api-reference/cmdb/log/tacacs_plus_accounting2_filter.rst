TacacsPlusAccounting2Filter
===========================

Configuration endpoint for log/tacacs_plus_accounting2_filter.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.tacacs_plus_accounting2_filter

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
   items = fgt.api.cmdb.log.tacacs_plus_accounting2_filter.get()


   # Update existing item
   result = fgt.api.cmdb.log.tacacs_plus_accounting2_filter.put(
       login_audit='updated-value',
       config_change_audit='updated-value',
       cli_cmd_audit='updated-value',
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
       login_audit=None,
       config_change_audit=None,
       cli_cmd_audit=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

