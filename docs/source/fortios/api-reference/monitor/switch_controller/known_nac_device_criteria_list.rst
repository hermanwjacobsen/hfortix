KnownNacDeviceCriteriaList
==========================

Configuration endpoint for switch_controller/known_nac_device_criteria_list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.known_nac_device_criteria_list

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.switch_controller.known_nac_device_criteria_list.get()



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

Retrieve a list of commonly configured NAC devices.

