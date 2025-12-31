StationCapability
=================

Configuration endpoint for wifi/station_capability.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.station_capability

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.station_capability.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mac_address=None,
       min_age=None,
       max_age=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of stations and their capability to connect to detected

