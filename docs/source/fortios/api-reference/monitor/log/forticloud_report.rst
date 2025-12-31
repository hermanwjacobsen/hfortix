Download
========

Configuration endpoint for log/forticloud_report.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.forticloud_report

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.forticloud_report.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       report_name,
       inline=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download PDF report from FortiCloud.

