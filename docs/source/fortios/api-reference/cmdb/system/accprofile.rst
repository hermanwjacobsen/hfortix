Accprofile
==========

Configuration endpoint for system/accprofile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.accprofile

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
   items = fgt.api.cmdb.system.accprofile.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.accprofile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.accprofile.post(
       nkey='value',  # optional
       name='value',  # optional
       comments='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.accprofile.put(
       name='updated-value',
       comments='updated-value',
       secfabgrp='updated-value',
       ftviewgrp='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.accprofile.delete(name='item-name')


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
       comments=None,
       secfabgrp=None,
       ftviewgrp=None,
       authgrp=None,
       sysgrp=None,
       netgrp=None,
       loggrp=None,
       fwgrp=None,
       vpngrp=None,
       utmgrp=None,
       wifi=None,
       netgrp_permission=None,
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
       comments=None,
       secfabgrp=None,
       ftviewgrp=None,
       authgrp=None,
       sysgrp=None,
       netgrp=None,
       loggrp=None,
       fwgrp=None,
       vpngrp=None,
       utmgrp=None,
       wifi=None,
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

