InternetServiceFqdnIconIds
==========================

Configuration endpoint for firewall/internet_service_fqdn_icon_ids.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.internet_service_fqdn_icon_ids

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.internet_service_fqdn_icon_ids.get()



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

Map of internet service FQDN icon IDs.

