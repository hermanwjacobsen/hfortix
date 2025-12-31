HistoricDailyRemoteLogs
=======================

Configuration endpoint for log/historic_daily_remote_logs.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.historic_daily_remote_logs

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.historic_daily_remote_logs.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       server,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Returns the amount of logs in bytes sent daily to a remote logging

