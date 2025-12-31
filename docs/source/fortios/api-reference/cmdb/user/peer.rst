Peer
====

Configuration endpoint for user/peer.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.peer

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
   items = fgt.api.cmdb.user.peer.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.peer.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.peer.post(
       nkey='value',  # optional
       name='value',  # optional
       mandatory_ca_verify='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.peer.put(
       name='updated-value',
       mandatory_ca_verify='updated-value',
       ca='updated-value',
       subject='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.peer.delete(name='item-name')


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
       mandatory_ca_verify=None,
       ca=None,
       subject=None,
       cn=None,
       cn_type=None,
       mfa_mode=None,
       mfa_server=None,
       mfa_username=None,
       mfa_password=None,
       ocsp_override_server=None,
       two_factor=None,
       passwd=None,
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
       mandatory_ca_verify=None,
       ca=None,
       subject=None,
       cn=None,
       cn_type=None,
       mfa_mode=None,
       mfa_server=None,
       mfa_username=None,
       mfa_password=None,
       ocsp_override_server=None,
       two_factor=None,
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

