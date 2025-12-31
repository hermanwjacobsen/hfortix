NetworkServiceDynamic
=====================

Configuration endpoint for firewall/network_service_dynamic.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.network_service_dynamic

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.network_service_dynamic.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List of dynamic network service IP address and port pairs.

