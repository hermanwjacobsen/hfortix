HistoricalStatistics
====================

Configuration endpoint for fortiview/historical_statistics.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiview.historical_statistics

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiview.historical_statistics.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       filter=None,
       sessionid=None,
       device=None,
       report_by=None,
       sort_by=None,
       chart_only=None,
       end=None,
       ip_version=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve historical drill-down and summary data for FortiView.

