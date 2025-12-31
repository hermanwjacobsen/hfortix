Ldap
====

Configuration endpoint for user/ldap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.ldap

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
   items = fgt.api.cmdb.user.ldap.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.ldap.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.ldap.post(
       nkey='value',  # optional
       name='value',  # optional
       server='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.ldap.put(
       name='updated-value',
       server='updated-value',
       secondary_server='updated-value',
       tertiary_server='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.ldap.delete(name='item-name')


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
       server=None,
       secondary_server=None,
       tertiary_server=None,
       status_ttl=None,
       server_identity_check=None,
       source_ip=None,
       source_ip_interface=None,
       source_port=None,
       cnid=None,
       dn=None,
       type=None,
       two_factor=None,
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
       server=None,
       secondary_server=None,
       tertiary_server=None,
       status_ttl=None,
       server_identity_check=None,
       source_ip=None,
       source_ip_interface=None,
       source_port=None,
       cnid=None,
       dn=None,
       type=None,
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

