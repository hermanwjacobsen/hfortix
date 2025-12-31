Custom
======

Configuration endpoint for ips/custom.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ips.custom

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
   items = fgt.api.cmdb.ips.custom.get()


   # Create new item
   result = fgt.api.cmdb.ips.custom.post(
       nkey='value',  # optional
       tag='value',  # optional
       signature='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ips.custom.put(
       tag='updated-value',
       signature='updated-value',
       rule_id='updated-value',
       severity='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ips.custom.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       tag=None,
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
       tag=None,
       signature=None,
       rule_id=None,
       severity=None,
       location=None,
       os=None,
       application=None,
       protocol=None,
       status=None,
       log=None,
       log_packet=None,
       comment=None,
       vdom=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       tag=None,
       payload_dict=None,
       before=None,
       after=None,
       signature=None,
       rule_id=None,
       severity=None,
       location=None,
       os=None,
       application=None,
       protocol=None,
       status=None,
       log=None,
       log_packet=None,
       comment=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       tag=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

