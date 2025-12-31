ResolveFqdn
===========

Configuration endpoint for system/resolve_fqdn.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.resolve_fqdn

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.resolve_fqdn.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       fqdn,
       ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Resolves the provided FQDNs to FQDN -> IP mappings.

