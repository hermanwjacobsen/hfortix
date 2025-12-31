Set
===

Configuration endpoint for system/private_data_encryption.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.private_data_encryption

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.private_data_encryption.post(
       enable='value',  # optional
       password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       enable=None,
       password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Sets private data encryption.

