ProxyArp
========

Configuration endpoint for system/proxy_arp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.proxy_arp

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
   items = fgt.api.cmdb.system.proxy_arp.get()


   # Create new item
   result = fgt.api.cmdb.system.proxy_arp.post(
       nkey='value',  # optional
       id='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.proxy_arp.put(
       id='updated-value',
       interface='updated-value',
       ip='updated-value',
       end_ip='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.proxy_arp.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id=None,
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
       id=None,
       interface=None,
       ip=None,
       end_ip=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       id=None,
       payload_dict=None,
       before=None,
       after=None,
       interface=None,
       ip=None,
       end_ip=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

