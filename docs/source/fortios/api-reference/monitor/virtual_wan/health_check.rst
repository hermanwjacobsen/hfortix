HealthCheck
===========

Configuration endpoint for virtual_wan/health_check.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.virtual_wan.health_check

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.virtual_wan.health_check.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       health_check_name=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve health-check statistics for each SD-WAN link.

