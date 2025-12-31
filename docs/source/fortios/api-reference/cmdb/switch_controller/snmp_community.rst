SnmpCommunity
=============

Configuration endpoint for switch_controller/snmp_community.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.snmp_community

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
   items = fgt.api.cmdb.switch_controller.snmp_community.get()


   # Create new item
   result = fgt.api.cmdb.switch_controller.snmp_community.post(
       nkey='value',  # optional
       id='value',  # optional
       name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.snmp_community.put(
       id='updated-value',
       name='updated-value',
       status='updated-value',
       hosts='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.snmp_community.delete()


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
       name=None,
       status=None,
       hosts=None,
       query_v1_status=None,
       query_v1_port=None,
       query_v2c_status=None,
       query_v2c_port=None,
       trap_v1_status=None,
       trap_v1_lport=None,
       trap_v1_rport=None,
       trap_v2c_status=None,
       trap_v2c_lport=None,
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
       name=None,
       status=None,
       hosts=None,
       query_v1_status=None,
       query_v1_port=None,
       query_v2c_status=None,
       query_v2c_port=None,
       trap_v1_status=None,
       trap_v1_lport=None,
       trap_v1_rport=None,
       trap_v2c_status=None,
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

