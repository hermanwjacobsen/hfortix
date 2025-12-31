Delete
======

Configuration endpoint for webfilter/override.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.webfilter.override

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.webfilter.override.post(
       mkey='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Delete a configured webfilter override.

