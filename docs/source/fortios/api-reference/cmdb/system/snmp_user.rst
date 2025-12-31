SnmpUser
========

Configuration endpoint for system/snmp_user.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.snmp_user

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
   items = fgt.api.cmdb.system.snmp_user.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.snmp_user.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.snmp_user.post(
       nkey='value',  # optional
       name='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.snmp_user.put(
       name='updated-value',
       status='updated-value',
       trap_status='updated-value',
       trap_lport='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.snmp_user.delete(name='item-name')


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
       status=None,
       trap_status=None,
       trap_lport=None,
       trap_rport=None,
       queries=None,
       query_port=None,
       notify_hosts=None,
       notify_hosts6=None,
       source_ip=None,
       source_ipv6=None,
       ha_direct=None,
       events=None,
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
       status=None,
       trap_status=None,
       trap_lport=None,
       trap_rport=None,
       queries=None,
       query_port=None,
       notify_hosts=None,
       notify_hosts6=None,
       source_ip=None,
       source_ipv6=None,
       ha_direct=None,
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

