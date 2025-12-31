Delete
======

Configuration endpoint for sniffer/sniffer.

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.sniffer.sniffer

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.service.sniffer.sniffer.post(
       mkey='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       vdom=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Deletes a packet capture.

