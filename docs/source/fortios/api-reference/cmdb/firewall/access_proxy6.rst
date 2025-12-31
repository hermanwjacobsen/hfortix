AccessProxy6
============

Configuration endpoint for firewall/access_proxy6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.access_proxy6

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
   items = fgt.api.cmdb.firewall.access_proxy6.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.access_proxy6.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy6.post(
       nkey='value',  # optional
       name='value',  # optional
       vip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy6.put(
       name='updated-value',
       vip='updated-value',
       auth_portal='updated-value',
       auth_virtual_host='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy6.delete(name='item-name')


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
       auth_portal=None,
       auth_virtual_host=None,
       log_blocked_traffic=None,
       add_vhost_domain_to_dnsdb=None,
       svr_pool_multiplex=None,
       svr_pool_ttl=None,
       svr_pool_server_max_request=None,
       svr_pool_server_max_concurrent_request=None,
       decrypted_traffic_mirror=None,
       api_gateway=None,
       api_gateway6=None,
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
       auth_portal=None,
       auth_virtual_host=None,
       log_blocked_traffic=None,
       add_vhost_domain_to_dnsdb=None,
       svr_pool_multiplex=None,
       svr_pool_ttl=None,
       svr_pool_server_max_request=None,
       svr_pool_server_max_concurrent_request=None,
       decrypted_traffic_mirror=None,
       api_gateway=None,
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

