SnmpSysinfo
===========

Configuration endpoint for switch_controller/snmp_sysinfo.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.snmp_sysinfo

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.switch_controller.snmp_sysinfo.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.snmp_sysinfo.put(
       status='updated-value',
       engine_id='updated-value',
       description='updated-value',
       contact_info='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       engine_id=None,
       description=None,
       contact_info=None,
       location=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

