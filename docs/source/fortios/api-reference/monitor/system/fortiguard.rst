ClearStatistics
===============

Configuration endpoint for system/fortiguard.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.fortiguard

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.fortiguard.post(
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Immediately clear all FortiGuard statistics.

