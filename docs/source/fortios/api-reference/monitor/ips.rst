Ips
===



Overview
--------

The ``monitor.ips`` category provides real-time monitoring for:



Endpoint
--------

.. code-block:: python

   fgt.api.monitor.ips

Available Endpoints
-------------------

Common Operations
-----------------

Get Status Information
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get monitoring data
   data = fgt.api.monitor.ips.{endpoint}.get()

Query with Parameters
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get monitoring data with filters
   data = fgt.api.monitor.ips.{endpoint}.get(
       param='value'
   )

HTTP Methods
------------

Monitor endpoints are **read-only** and only support:

**.get()**
   HTTP GET - Retrieve monitoring data and statistics

.. note::
   Monitor API endpoints do not support POST, PUT, or DELETE operations.
   Use the CMDB API for configuration changes.

See Also
--------

- :doc:`/fortios/api-reference/monitor/index` - Monitor API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
