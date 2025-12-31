FtmPush
=======

Configuration endpoint for system/ftm_push.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ftm_push

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
   items = fgt.api.cmdb.system.ftm_push.get()


   # Update existing item
   result = fgt.api.cmdb.system.ftm_push.put(
       proxy='updated-value',
       interface='updated-value',
       server='updated-value',
       server_port='updated-value',
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
       proxy=None,
       interface=None,
       server=None,
       server_port=None,
       server_cert=None,
       server_ip=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

