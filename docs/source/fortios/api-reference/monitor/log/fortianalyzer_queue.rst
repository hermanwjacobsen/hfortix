FortianalyzerQueue
==================

Configuration endpoint for log/fortianalyzer_queue.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.fortianalyzer_queue

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.fortianalyzer_queue.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve information on FortiAnalyzer's queue state.

