ShapingPolicy
=============

Configuration endpoint for firewall/shaping_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.shaping_policy

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
   items = fgt.api.cmdb.firewall.shaping_policy.get()


   # Create new item
   result = fgt.api.cmdb.firewall.shaping_policy.post(
       nkey='value',  # optional
       id='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.shaping_policy.put(
       id='updated-value',
       uuid='updated-value',
       name='updated-value',
       comment='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.shaping_policy.delete()


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
       uuid=None,
       name=None,
       comment=None,
       status=None,
       ip_version=None,
       traffic_type=None,
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
       dstaddr6=None,
       internet_service=None,
       internet_service_name=None,
       # ... more parameters
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
       uuid=None,
       name=None,
       comment=None,
       status=None,
       ip_version=None,
       traffic_type=None,
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
       dstaddr6=None,
       internet_service=None,
       # ... more parameters
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

