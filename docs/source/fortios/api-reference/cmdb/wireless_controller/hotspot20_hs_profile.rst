Hotspot20HsProfile
==================

Configuration endpoint for wireless_controller/hotspot20_hs_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.hotspot20_hs_profile

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
   items = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       release='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.put(
       name='updated-value',
       release='updated-value',
       access_network_type='updated-value',
       access_network_internet='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.hotspot20_hs_profile.delete(name='item-name')


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
       release=None,
       access_network_type=None,
       access_network_internet=None,
       access_network_asra=None,
       access_network_esr=None,
       access_network_uesa=None,
       venue_group=None,
       venue_type=None,
       hessid=None,
       proxy_arp=None,
       l2tif=None,
       pame_bi=None,
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
       release=None,
       access_network_type=None,
       access_network_internet=None,
       access_network_asra=None,
       access_network_esr=None,
       access_network_uesa=None,
       venue_group=None,
       venue_type=None,
       hessid=None,
       proxy_arp=None,
       l2tif=None,
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

