Bios
====

Configuration endpoint for switch_controller/managed_switch.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.managed_switch

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.switch_controller.managed_switch.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get a list of BIOS info by managed FortiSwitches.

