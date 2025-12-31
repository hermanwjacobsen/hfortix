ClearCounters
=============

Configuration endpoint for firewall/acl.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.acl

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.acl.post(
       policy='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       policy=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset counters for one or more IPv4 ACLs by policy ID.

