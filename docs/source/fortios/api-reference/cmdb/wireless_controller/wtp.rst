Wtp
===

Configuration endpoint for wireless_controller/wtp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.wtp

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
   items = fgt.api.cmdb.wireless_controller.wtp.get()


   # Create new item
   result = fgt.api.cmdb.wireless_controller.wtp.post(
       nkey='value',  # optional
       wtp_id='value',  # optional
       index='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.wtp.put(
       wtp_id='updated-value',
       index='updated-value',
       uuid='updated-value',
       admin='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.wtp.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       wtp_id=None,
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
       wtp_id=None,
       index=None,
       uuid=None,
       admin=None,
       name=None,
       location=None,
       comment=None,
       region=None,
       region_x=None,
       region_y=None,
       firmware_provision=None,
       firmware_provision_latest=None,
       wtp_profile=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       wtp_id=None,
       payload_dict=None,
       before=None,
       after=None,
       index=None,
       uuid=None,
       admin=None,
       name=None,
       location=None,
       comment=None,
       region=None,
       region_x=None,
       region_y=None,
       firmware_provision=None,
       firmware_provision_latest=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       wtp_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

