CheckPortAvailability
=====================

Configuration endpoint for system/check_port_availability.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.check_port_availability

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.check_port_availability.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       port_ranges,
       service=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check whether a list of TCP port ranges is available for a certain

