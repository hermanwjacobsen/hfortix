Settings
========

Configuration endpoint for system/settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.settings

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
   items = fgt.api.cmdb.system.settings.get()


   # Update existing item
   result = fgt.api.cmdb.system.settings.put(
       comments='updated-value',
       vdom_type='updated-value',
       lan_extension_controller_addr='updated-value',
       lan_extension_controller_port='updated-value',
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
       comments=None,
       vdom_type=None,
       lan_extension_controller_addr=None,
       lan_extension_controller_port=None,
       opmode=None,
       ngfw_mode=None,
       http_external_dest=None,
       firewall_session_dirty=None,
       manageip=None,
       gateway=None,
       ip=None,
       manageip6=None,
       # ... more parameters
   )

Update this specific resource.

