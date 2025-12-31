RealtimeProxyStatistics
=======================

Configuration endpoint for fortiview/realtime_proxy_statistics.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiview.realtime_proxy_statistics

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiview.realtime_proxy_statistics.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       report_by=None,
       sort_by=None,
       ip_version=None,
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
       dstaddr6=None,
       srcport=None,
       dstport=None,
       srcintf=None,
       dstintf=None,
       policyid=None,
       proxy_policyid=None,
       protocol=None,
       application=None,
       # ... more parameters
   )

Retrieve realtime drill-down and summary data for proxy session

