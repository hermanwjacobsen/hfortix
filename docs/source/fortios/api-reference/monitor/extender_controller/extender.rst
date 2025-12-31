Diagnose
========

Configuration endpoint for extender_controller/extender.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.extender_controller.extender

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.extender_controller.extender.post(
       id='value',  # optional
       cmd='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       id=None,
       cmd=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Execute diagnotic commands.

