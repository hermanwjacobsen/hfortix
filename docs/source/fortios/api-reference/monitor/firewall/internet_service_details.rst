InternetServiceDetails
======================

Configuration endpoint for firewall/internet_service_details.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.internet_service_details

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.internet_service_details.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id,
       country_id=None,
       region_id=None,
       city_id=None,
       summary_only=None,
       ipv6_only=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List all details for a given Internet Service ID.

