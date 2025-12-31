SslSetting
==========

Configuration endpoint for firewall/ssl_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ssl_setting

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
   items = fgt.api.cmdb.firewall.ssl_setting.get()


   # Update existing item
   result = fgt.api.cmdb.firewall.ssl_setting.put(
       proxy_connect_timeout='updated-value',
       ssl_dh_bits='updated-value',
       ssl_send_empty_frags='updated-value',
       no_matching_cipher_action='updated-value',
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
       proxy_connect_timeout=None,
       ssl_dh_bits=None,
       ssl_send_empty_frags=None,
       no_matching_cipher_action=None,
       cert_manager_cache_timeout=None,
       resigned_short_lived_certificate=None,
       cert_cache_capacity=None,
       cert_cache_timeout=None,
       session_cache_capacity=None,
       session_cache_timeout=None,
       kxp_queue_threshold=None,
       ssl_queue_threshold=None,
       # ... more parameters
   )

Update this specific resource.

