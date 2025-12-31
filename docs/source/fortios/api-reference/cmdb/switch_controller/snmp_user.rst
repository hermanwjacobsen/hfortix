SnmpUser
========

Configuration endpoint for switch_controller/snmp_user.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.snmp_user

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
   items = fgt.api.cmdb.switch_controller.snmp_user.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.snmp_user.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.snmp_user.post(
       nkey='value',  # optional
       name='value',  # optional
       queries='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.snmp_user.put(
       name='updated-value',
       queries='updated-value',
       query_port='updated-value',
       security_level='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.snmp_user.delete(name='item-name')


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
       queries=None,
       query_port=None,
       security_level=None,
       auth_proto=None,
       auth_pwd=None,
       priv_proto=None,
       priv_pwd=None,
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
       queries=None,
       query_port=None,
       security_level=None,
       auth_proto=None,
       auth_pwd=None,
       priv_proto=None,
       priv_pwd=None,
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

