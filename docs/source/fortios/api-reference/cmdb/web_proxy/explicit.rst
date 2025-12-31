Explicit
========

Configuration endpoint for web_proxy/explicit.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.web_proxy.explicit

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
   items = fgt.api.cmdb.web_proxy.explicit.get()


   # Update existing item
   result = fgt.api.cmdb.web_proxy.explicit.put(
       status='updated-value',
       secure_web_proxy='updated-value',
       ftp_over_http='updated-value',
       socks='updated-value',
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
       secure_web_proxy=None,
       ftp_over_http=None,
       socks=None,
       http_incoming_port=None,
       http_connection_mode=None,
       https_incoming_port=None,
       secure_web_proxy_cert=None,
       client_cert=None,
       user_agent_detect=None,
       empty_cert_action=None,
       ssl_dh_bits=None,
       # ... more parameters
   )

Update this specific resource.

