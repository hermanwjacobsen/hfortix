FctemsOverride
==============

Configuration endpoint for endpoint_control/fctems_override.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.endpoint_control.fctems_override

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
   items = fgt.api.cmdb.endpoint_control.fctems_override.get()


   # Create new item
   result = fgt.api.cmdb.endpoint_control.fctems_override.post(
       nkey='value',  # optional
       ems_id='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.endpoint_control.fctems_override.put(
       ems_id='updated-value',
       status='updated-value',
       name='updated-value',
       dirty_reason='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.endpoint_control.fctems_override.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ems_id=None,
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
       ems_id=None,
       status=None,
       name=None,
       dirty_reason=None,
       fortinetone_cloud_authentication=None,
       cloud_authentication_access_key=None,
       server=None,
       https_port=None,
       serial_number=None,
       tenant_id=None,
       source_ip=None,
       pull_sysinfo=None,
       pull_vulnerabilities=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       ems_id=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       name=None,
       dirty_reason=None,
       fortinetone_cloud_authentication=None,
       cloud_authentication_access_key=None,
       server=None,
       https_port=None,
       serial_number=None,
       tenant_id=None,
       source_ip=None,
       pull_sysinfo=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       ems_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

