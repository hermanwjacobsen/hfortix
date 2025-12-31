HoldSignatures
==============

Configuration endpoint for ips/hold_signatures.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.ips.hold_signatures

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.ips.hold_signatures.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ips_sensor=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Return a list of IPS signatures that are on hold due to active hold

