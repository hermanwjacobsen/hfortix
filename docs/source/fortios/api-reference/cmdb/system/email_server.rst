EmailServer
===========

Configuration endpoint for system/email_server.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.email_server

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
   items = fgt.api.cmdb.system.email_server.get()


   # Update existing item
   result = fgt.api.cmdb.system.email_server.put(
       type='updated-value',
       server='updated-value',
       port='updated-value',
       source_ip='updated-value',
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
       type=None,
       server=None,
       port=None,
       source_ip=None,
       source_ip6=None,
       authenticate=None,
       validate_server=None,
       username=None,
       password=None,
       security=None,
       ssl_min_proto_version=None,
       interface_select_method=None,
       # ... more parameters
   )

Update this specific resource.

