Hotspot20H2qpOsuProvider
========================

Configuration endpoint for wireless_controller/hotspot20_h2qp_osu_provider.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider

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
   items = fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider.post(
       nkey='value',  # optional
       name='value',  # optional
       friendly_name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider.put(
       name='updated-value',
       friendly_name='updated-value',
       server_uri='updated-value',
       osu_method='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.hotspot20_h2qp_osu_provider.delete(name='item-name')


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
       friendly_name=None,
       server_uri=None,
       osu_method=None,
       osu_nai=None,
       service_description=None,
       icon=None,
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
       friendly_name=None,
       server_uri=None,
       osu_method=None,
       osu_nai=None,
       service_description=None,
       icon=None,
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

