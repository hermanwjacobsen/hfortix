PseConfig
=========

Configuration endpoint for switch_controller/recommendation.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.recommendation

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.switch_controller.recommendation.post(
       fortilink='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       fortilink=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Execute switch recommendation for pse-config to prevent PSE-PSE

