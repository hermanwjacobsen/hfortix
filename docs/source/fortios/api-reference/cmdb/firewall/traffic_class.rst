TrafficClass
============

Configuration endpoint for firewall/traffic_class.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.traffic_class

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
   items = fgt.api.cmdb.firewall.traffic_class.get()


   # Create new item
   result = fgt.api.cmdb.firewall.traffic_class.post(
       nkey='value',  # optional
       class_id='value',  # optional
       class_name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.traffic_class.put(
       class_id='updated-value',
       class_name='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.traffic_class.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       class_id=None,
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
       class_id=None,
       class_name=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       class_id=None,
       payload_dict=None,
       before=None,
       after=None,
       class_name=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       class_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

