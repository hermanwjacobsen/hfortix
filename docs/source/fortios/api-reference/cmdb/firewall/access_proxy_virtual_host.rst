AccessProxyVirtualHost
======================

Configuration endpoint for firewall/access_proxy_virtual_host.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.access_proxy_virtual_host

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
   items = fgt.api.cmdb.firewall.access_proxy_virtual_host.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.access_proxy_virtual_host.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.post(
       nkey='value',  # optional
       name='value',  # optional
       ssl_certificate='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.put(
       name='updated-value',
       ssl_certificate='updated-value',
       host='updated-value',
       host_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.delete(name='item-name')


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
       ssl_certificate=None,
       host=None,
       host_type=None,
       replacemsg_group=None,
       empty_cert_action=None,
       user_agent_detect=None,
       client_cert=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       ssl_certificate=None,
       host=None,
       host_type=None,
       replacemsg_group=None,
       empty_cert_action=None,
       user_agent_detect=None,
       client_cert=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

