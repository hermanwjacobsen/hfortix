Csf
===

Configuration endpoint for system/csf.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.csf

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
   items = fgt.api.cmdb.system.csf.get()


   # Update existing item
   result = fgt.api.cmdb.system.csf.put(
       status='updated-value',
       uid='updated-value',
       upstream='updated-value',
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
       uid=None,
       upstream=None,
       source_ip=None,
       upstream_interface_select_method=None,
       upstream_interface=None,
       upstream_port=None,
       group_name=None,
       group_password=None,
       accept_auth_by_cert=None,
       log_unification=None,
       authorization_request_type=None,
       # ... more parameters
   )

Update this specific resource.

