Select
======

Configuration endpoint for utm/rating_lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.utm.rating_lookup

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.utm.rating_lookup.post(
       url='value',  # optional
       lang='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       url=None,
       lang=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Lookup FortiGuard rating for a specific URL.

