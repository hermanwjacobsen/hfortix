ProbeResponse
=============

Configuration endpoint for system/probe_response.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.probe_response

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
   items = fgt.api.cmdb.system.probe_response.get()


   # Update existing item
   result = fgt.api.cmdb.system.probe_response.put(
       port='updated-value',
       http_probe_value='updated-value',
       ttl_mode='updated-value',
       mode='updated-value',
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
       port=None,
       http_probe_value=None,
       ttl_mode=None,
       mode=None,
       security_mode=None,
       password=None,
       timeout=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

