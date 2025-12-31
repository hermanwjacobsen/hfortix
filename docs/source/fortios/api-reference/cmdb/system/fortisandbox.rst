Fortisandbox
============

Configuration endpoint for system/fortisandbox.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.fortisandbox

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
   items = fgt.api.cmdb.system.fortisandbox.get()


   # Update existing item
   result = fgt.api.cmdb.system.fortisandbox.put(
       status='updated-value',
       forticloud='updated-value',
       server='updated-value',
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
       status=None,
       forticloud=None,
       server=None,
       source_ip=None,
       interface_select_method=None,
       interface=None,
       vrf_select=None,
       enc_algorithm=None,
       ssl_min_proto_version=None,
       email=None,
       ca=None,
       cn=None,
       # ... more parameters
   )

Update this specific resource.

