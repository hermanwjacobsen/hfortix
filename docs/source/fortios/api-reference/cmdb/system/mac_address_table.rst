MacAddressTable
===============

Configuration endpoint for system/mac_address_table.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.mac_address_table

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
   items = fgt.api.cmdb.system.mac_address_table.get()


   # Create new item
   result = fgt.api.cmdb.system.mac_address_table.post(
       nkey='value',  # optional
       mac='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.mac_address_table.put(
       mac='updated-value',
       interface='updated-value',
       reply_substitute='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.mac_address_table.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mac=None,
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
       mac=None,
       interface=None,
       reply_substitute=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       mac=None,
       payload_dict=None,
       before=None,
       after=None,
       interface=None,
       reply_substitute=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       mac=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

