Fortiguard
==========

Configuration endpoint for webfilter/fortiguard.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.webfilter.fortiguard

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
   items = fgt.api.cmdb.webfilter.fortiguard.get()


   # Update existing item
   result = fgt.api.cmdb.webfilter.fortiguard.put(
       cache_mode='updated-value',
       cache_prefix_match='updated-value',
       cache_mem_permille='updated-value',
       ovrd_auth_port_http='updated-value',
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
       cache_mode=None,
       cache_prefix_match=None,
       cache_mem_permille=None,
       ovrd_auth_port_http=None,
       ovrd_auth_port_https=None,
       ovrd_auth_port_https_flow=None,
       ovrd_auth_port_warning=None,
       ovrd_auth_https=None,
       warn_auth_https=None,
       close_ports=None,
       request_packet_size_limit=None,
       embed_image=None,
       # ... more parameters
   )

Update this specific resource.

