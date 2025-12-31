AcquiredDns
===========

Configuration endpoint for system/acquired_dns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.acquired_dns

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.acquired_dns.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of interfaces and their acquired DNS servers.

