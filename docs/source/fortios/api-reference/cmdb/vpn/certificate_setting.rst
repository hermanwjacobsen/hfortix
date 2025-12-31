CertificateSetting
==================

Configuration endpoint for vpn/certificate_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.certificate_setting

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
   items = fgt.api.cmdb.vpn.certificate_setting.get()


   # Update existing item
   result = fgt.api.cmdb.vpn.certificate_setting.put(
       ocsp_status='updated-value',
       ocsp_option='updated-value',
       proxy='updated-value',
       proxy_port='updated-value',
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
       ocsp_status=None,
       ocsp_option=None,
       proxy=None,
       proxy_port=None,
       proxy_username=None,
       proxy_password=None,
       source_ip=None,
       ocsp_default_server=None,
       interface_select_method=None,
       interface=None,
       vrf_select=None,
       check_ca_cert=None,
       # ... more parameters
   )

Update this specific resource.

