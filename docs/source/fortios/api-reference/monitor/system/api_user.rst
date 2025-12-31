GenerateKey
===========

Configuration endpoint for system/api_user.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.api_user

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.api_user.post(
       api_user='value',  # optional
       expiry='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       api_user=None,
       expiry=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Generate a new api-key for the specified api-key-auth admin.

