ThreatWeight
============

Configuration endpoint for log/threat_weight.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.threat_weight

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
   items = fgt.api.cmdb.log.threat_weight.get()


   # Update existing item
   result = fgt.api.cmdb.log.threat_weight.put(
       status='updated-value',
       level='updated-value',
       blocked_connection='updated-value',
       failed_connection='updated-value',
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
       status=None,
       level=None,
       blocked_connection=None,
       failed_connection=None,
       url_block_detected=None,
       botnet_connection_detected=None,
       malware=None,
       ips=None,
       web=None,
       geolocation=None,
       application=None,
       vdom=None,
       # ... more parameters
   )

Update this specific resource.

