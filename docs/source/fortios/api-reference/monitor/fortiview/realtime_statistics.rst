RealtimeStatistics
==================

Configuration endpoint for fortiview/realtime_statistics.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiview.realtime_statistics

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiview.realtime_statistics.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
       dstaddr6=None,
       srcport=None,
       dstport=None,
       srcintf=None,
       srcintfrole=None,
       dstintf=None,
       dstintfrole=None,
       policyid=None,
       security_policyid=None,
       protocol=None,
       web_category=None,
       web_domain=None,
       # ... more parameters
   )

Retrieve realtime drill-down and summary data for FortiView.

