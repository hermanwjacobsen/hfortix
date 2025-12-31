IpsUrlfilterDns6
================

Configuration endpoint for system/ips_urlfilter_dns6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ips_urlfilter_dns6

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.ips_urlfilter_dns6.get()


   # Create new item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.post(
       nkey='value',  # optional
       address6='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.put(
       address6='updated-value',
       status='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       address6=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       address6=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       address6=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       address6=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

