Revoke
======

Configuration endpoint for system/dhcp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.dhcp

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.dhcp.post(
       ip='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       ip=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Revoke IPv4 DHCP leases.

