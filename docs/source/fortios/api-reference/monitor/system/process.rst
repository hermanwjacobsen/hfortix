Kill
====

Configuration endpoint for system/process.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.process

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.process.post(
       pid='value',  # optional
       signal='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       pid=None,
       signal=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Kill a running process.

