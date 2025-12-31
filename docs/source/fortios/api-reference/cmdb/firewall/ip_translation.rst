IpTranslation
=============

Configuration endpoint for firewall/ip_translation.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ip_translation

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
   items = fgt.api.cmdb.firewall.ip_translation.get()


   # Create new item
   result = fgt.api.cmdb.firewall.ip_translation.post(
       nkey='value',  # optional
       transid='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.ip_translation.put(
       transid='updated-value',
       type='updated-value',
       startip='updated-value',
       endip='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.ip_translation.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       transid=None,
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
       transid=None,
       type=None,
       startip=None,
       endip=None,
       map_startip=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       transid=None,
       payload_dict=None,
       before=None,
       after=None,
       type=None,
       startip=None,
       endip=None,
       map_startip=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       transid=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

