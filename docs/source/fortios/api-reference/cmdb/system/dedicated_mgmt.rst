DedicatedMgmt
=============

Configuration endpoint for system/dedicated_mgmt.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.dedicated_mgmt

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
   items = fgt.api.cmdb.system.dedicated_mgmt.get()


   # Update existing item
   result = fgt.api.cmdb.system.dedicated_mgmt.put(
       status='updated-value',
       interface='updated-value',
       default_gateway='updated-value',
       dhcp_server='updated-value',
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
       interface=None,
       default_gateway=None,
       dhcp_server=None,
       dhcp_netmask=None,
       dhcp_start_ip=None,
       dhcp_end_ip=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

