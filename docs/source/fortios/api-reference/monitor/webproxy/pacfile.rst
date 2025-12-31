Download
========

Configuration endpoint for webproxy/pacfile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.webproxy.pacfile

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.webproxy.pacfile.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download webproxy PAC file.

