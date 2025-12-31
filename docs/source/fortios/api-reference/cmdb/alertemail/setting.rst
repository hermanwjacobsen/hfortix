Setting
=======

Configuration endpoint for alertemail/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.alertemail.setting

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
   items = fgt.api.cmdb.alertemail.setting.get()


   # Update existing item
   result = fgt.api.cmdb.alertemail.setting.put(
       username='updated-value',
       mailto1='updated-value',
       mailto2='updated-value',
       mailto3='updated-value',
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
       username=None,
       mailto1=None,
       mailto2=None,
       mailto3=None,
       filter_mode=None,
       email_interval=None,
       IPS_logs=None,
       firewall_authentication_failure_logs=None,
       HA_logs=None,
       IPsec_errors_logs=None,
       FDS_update_logs=None,
       PPP_errors_logs=None,
       # ... more parameters
   )

Update this specific resource.

