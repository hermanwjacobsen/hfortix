GtpStatistics
=============

Configuration endpoint for firewall/gtp_statistics.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.gtp_statistics

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.gtp_statistics.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve statistics for GTP.

