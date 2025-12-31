Dynamic
=======

Configuration endpoint for system/external_resource.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.external_resource

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.external_resource.post(
       commands='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       commands=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Push updates to the specified external resource.

