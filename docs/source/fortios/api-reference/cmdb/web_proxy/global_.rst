Global
======

Configuration endpoint for web_proxy/global_.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.web_proxy.global_

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
   items = fgt.api.cmdb.web_proxy.global_.get()


   # Update existing item
   result = fgt.api.cmdb.web_proxy.global_.put(
       ssl_cert='updated-value',
       ssl_ca_cert='updated-value',
       fast_policy_match='updated-value',
       ldap_user_cache='updated-value',
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
       ssl_cert=None,
       ssl_ca_cert=None,
       fast_policy_match=None,
       ldap_user_cache=None,
       proxy_fqdn=None,
       max_request_length=None,
       max_message_length=None,
       http2_client_window_size=None,
       http2_server_window_size=None,
       auth_sign_timeout=None,
       strict_web_check=None,
       forward_proxy_auth=None,
       # ... more parameters
   )

Update this specific resource.

