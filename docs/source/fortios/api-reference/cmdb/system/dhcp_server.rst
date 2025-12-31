DhcpServer
==========

Configuration endpoint for system/dhcp_server.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.dhcp_server

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
   items = fgt.api.cmdb.system.dhcp_server.get()


   # Create new item
   result = fgt.api.cmdb.system.dhcp_server.post(
       nkey='value',  # optional
       id='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.dhcp_server.put(
       id='updated-value',
       status='updated-value',
       lease_time='updated-value',
       mac_acl_default_action='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.dhcp_server.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id=None,
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
       id=None,
       status=None,
       lease_time=None,
       mac_acl_default_action=None,
       forticlient_on_net_status=None,
       dns_service=None,
       dns_server1=None,
       dns_server2=None,
       dns_server3=None,
       dns_server4=None,
       wifi_ac_service=None,
       wifi_ac1=None,
       wifi_ac2=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       id=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       lease_time=None,
       mac_acl_default_action=None,
       forticlient_on_net_status=None,
       dns_service=None,
       dns_server1=None,
       dns_server2=None,
       dns_server3=None,
       dns_server4=None,
       wifi_ac_service=None,
       wifi_ac1=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

