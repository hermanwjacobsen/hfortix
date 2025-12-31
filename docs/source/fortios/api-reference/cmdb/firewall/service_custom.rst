ServiceCustom
=============

Configuration endpoint for firewall/service_custom.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.service_custom

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
   items = fgt.api.cmdb.firewall.service_custom.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.service_custom.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.service_custom.post(
       nkey='value',  # optional
       name='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.service_custom.put(
       name='updated-value',
       uuid='updated-value',
       proxy='updated-value',
       category='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.service_custom.delete(name='item-name')


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
       uuid=None,
       proxy=None,
       category=None,
       protocol=None,
       helper=None,
       iprange=None,
       fqdn=None,
       protocol_number=None,
       icmptype=None,
       icmpcode=None,
       tcp_portrange=None,
       udp_portrange=None,
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
       uuid=None,
       proxy=None,
       category=None,
       protocol=None,
       helper=None,
       iprange=None,
       fqdn=None,
       protocol_number=None,
       icmptype=None,
       icmpcode=None,
       tcp_portrange=None,
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

