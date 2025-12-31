Address6Template
================

Configuration endpoint for firewall/address6_template.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.address6_template

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
   items = fgt.api.cmdb.firewall.address6_template.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.address6_template.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.address6_template.post(
       nkey='value',  # optional
       name='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.address6_template.put(
       name='updated-value',
       uuid='updated-value',
       ip6='updated-value',
       subnet_segment_count='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.address6_template.delete(name='item-name')


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
       uuid=None,
       ip6=None,
       subnet_segment_count=None,
       subnet_segment=None,
       fabric_object=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       uuid=None,
       ip6=None,
       subnet_segment_count=None,
       subnet_segment=None,
       fabric_object=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

