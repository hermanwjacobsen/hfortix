MobileTunnel
============

Configuration endpoint for system/mobile_tunnel.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.mobile_tunnel

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
   items = fgt.api.cmdb.system.mobile_tunnel.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.mobile_tunnel.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.mobile_tunnel.post(
       nkey='value',  # optional
       name='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.mobile_tunnel.put(
       name='updated-value',
       status='updated-value',
       roaming_interface='updated-value',
       home_agent='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.mobile_tunnel.delete(name='item-name')


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
       status=None,
       roaming_interface=None,
       home_agent=None,
       home_address=None,
       renew_interval=None,
       lifetime=None,
       reg_interval=None,
       reg_retry=None,
       n_mhae_spi=None,
       n_mhae_key_type=None,
       n_mhae_key=None,
       hash_algorithm=None,
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
       status=None,
       roaming_interface=None,
       home_agent=None,
       home_address=None,
       renew_interval=None,
       lifetime=None,
       reg_interval=None,
       reg_retry=None,
       n_mhae_spi=None,
       n_mhae_key_type=None,
       n_mhae_key=None,
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

