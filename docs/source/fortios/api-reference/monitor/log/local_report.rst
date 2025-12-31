Delete
======

Configuration endpoint for log/local_report.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.local_report

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.log.local_report.post(
       mkeys='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkeys=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Delete a local report.

