Status
======

Configuration endpoint for system/5g_modem.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.5g_modem

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.5g_modem.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       modem=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve the 5G modem status.

