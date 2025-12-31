ServiceCommunicationStats
=========================

Configuration endpoint for fortiguard/service_communication_stats.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiguard.service_communication_stats

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiguard.service_communication_stats.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       service_type=None,
       timeslot=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve historical statistics for communication with FortiGuard

