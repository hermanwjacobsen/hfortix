Fortigate
=========

Configuration endpoint for extension_controller/fortigate.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.extension_controller.fortigate

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.extension_controller.fortigate.get()



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

Retrieve statistics for configured FortiGate LAN Extension Connectors.

