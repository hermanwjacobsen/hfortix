Address6Dynamic
===============

Configuration endpoint for firewall/address6_dynamic.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.address6_dynamic

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.address6_dynamic.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List of IPv6 Fabric Connector address objects and the IPs they resolve

