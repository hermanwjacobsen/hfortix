ProfileGroup
============

Configuration endpoint for firewall/profile_group.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.profile_group

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
   items = fgt.api.cmdb.firewall.profile_group.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.profile_group.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.profile_group.post(
       nkey='value',  # optional
       name='value',  # optional
       profile_protocol_options='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.profile_group.put(
       name='updated-value',
       profile_protocol_options='updated-value',
       ssl_ssh_profile='updated-value',
       av_profile='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.profile_group.delete(name='item-name')


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
       profile_protocol_options=None,
       ssl_ssh_profile=None,
       av_profile=None,
       webfilter_profile=None,
       dnsfilter_profile=None,
       emailfilter_profile=None,
       dlp_profile=None,
       file_filter_profile=None,
       ips_sensor=None,
       application_list=None,
       voip_profile=None,
       ips_voip_filter=None,
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
       profile_protocol_options=None,
       ssl_ssh_profile=None,
       av_profile=None,
       webfilter_profile=None,
       dnsfilter_profile=None,
       emailfilter_profile=None,
       dlp_profile=None,
       file_filter_profile=None,
       ips_sensor=None,
       application_list=None,
       voip_profile=None,
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

