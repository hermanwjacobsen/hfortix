Select
======

Configuration endpoint for geoip/geoip_query.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.geoip.geoip_query

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.geoip.geoip_query.post(
       ip_addresses='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       ip_addresses=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve location details for IPs queried against FortiGuard's geoip

