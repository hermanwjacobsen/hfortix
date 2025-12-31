VneInterface
============

Configuration endpoint for system/vne_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.vne_interface

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
   items = fgt.api.cmdb.system.vne_interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.vne_interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.vne_interface.post(
       nkey='value',  # optional
       name='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.vne_interface.put(
       name='updated-value',
       interface='updated-value',
       ssl_certificate='updated-value',
       bmr_hostname='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.vne_interface.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
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
       name=None,
       interface=None,
       ssl_certificate=None,
       bmr_hostname=None,
       auto_asic_offload=None,
       ipv4_address=None,
       br=None,
       update_url=None,
       mode=None,
       http_username=None,
       http_password=None,
       vdom=None,
       raw_json=False,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       interface=None,
       ssl_certificate=None,
       bmr_hostname=None,
       auto_asic_offload=None,
       ipv4_address=None,
       br=None,
       update_url=None,
       mode=None,
       http_username=None,
       http_password=None,
       vdom=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

