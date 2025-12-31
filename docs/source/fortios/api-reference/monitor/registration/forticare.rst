AddLicense
==========

Configuration endpoint for registration/forticare.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.registration.forticare

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.registration.forticare.post(
       registration_code='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       registration_code=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Add a FortiCare license.

