Download
========

Configuration endpoint for system/vmlicense.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.vmlicense

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.vmlicense.post(
       token='value',  # optional
       proxy_url='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       token=None,
       proxy_url=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download Flex-VM license and reboot immediately if successful.

