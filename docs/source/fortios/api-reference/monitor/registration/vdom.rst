AddLicense
==========

Configuration endpoint for registration/vdom.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.registration.vdom

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.registration.vdom.post(
       license='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       license=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Add a VDOM license.

