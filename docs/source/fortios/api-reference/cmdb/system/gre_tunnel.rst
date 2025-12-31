GreTunnel
=========

Configuration endpoint for system/gre_tunnel.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.gre_tunnel

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
   items = fgt.api.cmdb.system.gre_tunnel.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.gre_tunnel.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.gre_tunnel.post(
       nkey='value',  # optional
       name='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.gre_tunnel.put(
       name='updated-value',
       interface='updated-value',
       ip_version='updated-value',
       remote_gw6='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.gre_tunnel.delete(name='item-name')


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
       interface=None,
       ip_version=None,
       remote_gw6=None,
       local_gw6=None,
       remote_gw=None,
       local_gw=None,
       use_sdwan=None,
       sequence_number_transmission=None,
       sequence_number_reception=None,
       checksum_transmission=None,
       checksum_reception=None,
       key_outbound=None,
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
       interface=None,
       ip_version=None,
       remote_gw6=None,
       local_gw6=None,
       remote_gw=None,
       local_gw=None,
       use_sdwan=None,
       sequence_number_transmission=None,
       sequence_number_reception=None,
       checksum_transmission=None,
       checksum_reception=None,
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

