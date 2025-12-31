Status
======

Configuration endpoint for switch_controller/isl_lockdown.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.isl_lockdown

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.switch_controller.isl_lockdown.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       fortilink,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get current status of ISL lockdown.

