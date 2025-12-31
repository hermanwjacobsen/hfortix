Explicit
========

Configuration endpoint for ftp_proxy/explicit.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ftp_proxy.explicit

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
   items = fgt.api.cmdb.ftp_proxy.explicit.get()


   # Update existing item
   result = fgt.api.cmdb.ftp_proxy.explicit.put(
       status='updated-value',
       incoming_port='updated-value',
       incoming_ip='updated-value',
       outgoing_ip='updated-value',
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
       incoming_port=None,
       incoming_ip=None,
       outgoing_ip=None,
       sec_default_action=None,
       server_data_mode=None,
       ssl=None,
       ssl_cert=None,
       ssl_dh_bits=None,
       ssl_algorithm=None,
       vdom=None,
       raw_json=False,
       # ... more parameters
   )

Update this specific resource.

