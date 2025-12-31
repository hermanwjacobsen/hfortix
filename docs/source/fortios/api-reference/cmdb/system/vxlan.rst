Vxlan
=====

Configuration endpoint for system/vxlan.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.vxlan

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
   items = fgt.api.cmdb.system.vxlan.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.vxlan.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.vxlan.post(
       nkey='value',  # optional
       name='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.vxlan.put(
       name='updated-value',
       interface='updated-value',
       vni='updated-value',
       ip_version='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.vxlan.delete(name='item-name')


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
       vni=None,
       ip_version=None,
       remote_ip=None,
       local_ip=None,
       remote_ip6=None,
       local_ip6=None,
       dstport=None,
       multicast_ttl=None,
       evpn_id=None,
       learn_from_traffic=None,
       vdom=None,
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
       vni=None,
       ip_version=None,
       remote_ip=None,
       local_ip=None,
       remote_ip6=None,
       local_ip6=None,
       dstport=None,
       multicast_ttl=None,
       evpn_id=None,
       learn_from_traffic=None,
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

