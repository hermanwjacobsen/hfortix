InternetServiceAppend
=====================

Configuration endpoint for firewall/internet_service_append.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.internet_service_append

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
   items = fgt.api.cmdb.firewall.internet_service_append.get()


   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_append.put(
       addr_mode='updated-value',
       match_port='updated-value',
       append_port='updated-value',
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
       addr_mode=None,
       match_port=None,
       append_port=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

