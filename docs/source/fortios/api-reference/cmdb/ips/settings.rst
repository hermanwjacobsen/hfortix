Settings
========

Configuration endpoint for ips/settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ips.settings

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
   items = fgt.api.cmdb.ips.settings.get()


   # Update existing item
   result = fgt.api.cmdb.ips.settings.put(
       packet_log_history='updated-value',
       packet_log_post_attack='updated-value',
       packet_log_memory='updated-value',
       ips_packet_quota='updated-value',
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
       packet_log_history=None,
       packet_log_post_attack=None,
       packet_log_memory=None,
       ips_packet_quota=None,
       proxy_inline_ips=None,
       ha_session_pickup=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

