Eventfilter
===========

Configuration endpoint for log/eventfilter.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.eventfilter

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
   items = fgt.api.cmdb.log.eventfilter.get()


   # Update existing item
   result = fgt.api.cmdb.log.eventfilter.put(
       event='updated-value',
       system='updated-value',
       vpn='updated-value',
       user='updated-value',
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
       event=None,
       system=None,
       vpn=None,
       user=None,
       router=None,
       wireless_activity=None,
       wan_opt=None,
       endpoint=None,
       ha=None,
       security_rating=None,
       fortiextender=None,
       connector=None,
       # ... more parameters
   )

Update this specific resource.

