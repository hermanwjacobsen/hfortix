ShaperPerIpShaper
=================

Configuration endpoint for firewall/shaper_per_ip_shaper.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.shaper_per_ip_shaper

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
   items = fgt.api.cmdb.firewall.shaper_per_ip_shaper.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.shaper_per_ip_shaper.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.shaper_per_ip_shaper.post(
       nkey='value',  # optional
       name='value',  # optional
       max_bandwidth='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.shaper_per_ip_shaper.put(
       name='updated-value',
       max_bandwidth='updated-value',
       bandwidth_unit='updated-value',
       max_concurrent_session='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.shaper_per_ip_shaper.delete(name='item-name')


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
       max_bandwidth=None,
       bandwidth_unit=None,
       max_concurrent_session=None,
       max_concurrent_tcp_session=None,
       max_concurrent_udp_session=None,
       diffserv_forward=None,
       diffserv_reverse=None,
       diffservcode_forward=None,
       diffservcode_rev=None,
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
       max_bandwidth=None,
       bandwidth_unit=None,
       max_concurrent_session=None,
       max_concurrent_tcp_session=None,
       max_concurrent_udp_session=None,
       diffserv_forward=None,
       diffserv_reverse=None,
       diffservcode_forward=None,
       diffservcode_rev=None,
       vdom=None,
       raw_json=False,
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

