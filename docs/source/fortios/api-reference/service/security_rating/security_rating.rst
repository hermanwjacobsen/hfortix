Recommendations
===============

Configuration endpoint for security_rating/security_rating.

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.security_rating.security_rating

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.service.security_rating.security_rating.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       checks,
       scope=None,
       vdom=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve recommendations for Security Rating tests.

