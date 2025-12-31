Download
========

Configuration endpoint for log/av_archive.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.av_archive

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.av_archive.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download file quarantined by AntiVirus.

