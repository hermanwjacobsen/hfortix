FssoPolling
===========

Configuration endpoint for user/fsso_polling.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.fsso_polling

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
   items = fgt.api.cmdb.user.fsso_polling.get()


   # Create new item
   result = fgt.api.cmdb.user.fsso_polling.post(
       nkey='value',  # optional
       id='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.fsso_polling.put(
       id='updated-value',
       status='updated-value',
       server='updated-value',
       default_domain='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.fsso_polling.delete()


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
       server=None,
       default_domain=None,
       port=None,
       user=None,
       password=None,
       ldap_server=None,
       logon_history=None,
       polling_frequency=None,
       adgrp=None,
       smbv1=None,
       smb_ntlmv1_auth=None,
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
       server=None,
       default_domain=None,
       port=None,
       user=None,
       password=None,
       ldap_server=None,
       logon_history=None,
       polling_frequency=None,
       adgrp=None,
       smbv1=None,
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

