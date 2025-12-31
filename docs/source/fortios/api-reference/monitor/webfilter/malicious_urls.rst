Stat
====

Configuration endpoint for webfilter/malicious_urls.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.webfilter.malicious_urls

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.webfilter.malicious_urls.get()



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

Retrieve statistics for the FortiSandbox malicious URL database.

