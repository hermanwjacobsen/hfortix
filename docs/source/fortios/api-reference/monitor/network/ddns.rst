Lookup
======

Configuration endpoint for network/ddns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.network.ddns

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.network.ddns.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       domain,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check DDNS FQDN availability.

