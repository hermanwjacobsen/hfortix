AccessProxySshClientCert
========================

Configuration endpoint for firewall/access_proxy_ssh_client_cert.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.access_proxy_ssh_client_cert

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
   items = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.post(
       nkey='value',  # optional
       name='value',  # optional
       source_address='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.put(
       name='updated-value',
       source_address='updated-value',
       permit_x11_forwarding='updated-value',
       permit_agent_forwarding='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.delete(name='item-name')


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
       source_address=None,
       permit_x11_forwarding=None,
       permit_agent_forwarding=None,
       permit_port_forwarding=None,
       permit_pty=None,
       permit_user_rc=None,
       cert_extension=None,
       auth_ca=None,
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
       source_address=None,
       permit_x11_forwarding=None,
       permit_agent_forwarding=None,
       permit_port_forwarding=None,
       permit_pty=None,
       permit_user_rc=None,
       cert_extension=None,
       auth_ca=None,
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

