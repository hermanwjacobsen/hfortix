Set
===

Configuration endpoint for system/time.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.time

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.time.post(
       year='value',  # optional
       month='value',  # optional
       day='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       year=None,
       month=None,
       day=None,
       hour=None,
       minute=None,
       second=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Sets current system time stamp.

