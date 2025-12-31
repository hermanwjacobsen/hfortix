WebProxy
========

Configuration endpoint for ztna/web_proxy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ztna.web_proxy

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.ztna.web_proxy.get()

   # Get specific item by name
   item = fgt.api.cmdb.ztna.web_proxy.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.ztna.web_proxy.post(
       nkey='value',  # optional
       name='value',  # optional
       vip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ztna.web_proxy.put(
       name='updated-value',
       vip='updated-value',
       host='updated-value',
       decrypted_traffic_mirror='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ztna.web_proxy.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       name=None,
       vip=None,
       host=None,
       decrypted_traffic_mirror=None,
       log_blocked_traffic=None,
       auth_portal=None,
       auth_virtual_host=None,
       vip6=None,
       svr_pool_multiplex=None,
       svr_pool_ttl=None,
       svr_pool_server_max_request=None,
       svr_pool_server_max_concurrent_request=None,
       api_gateway=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       vip=None,
       host=None,
       decrypted_traffic_mirror=None,
       log_blocked_traffic=None,
       auth_portal=None,
       auth_virtual_host=None,
       vip6=None,
       svr_pool_multiplex=None,
       svr_pool_ttl=None,
       svr_pool_server_max_request=None,
       svr_pool_server_max_concurrent_request=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

