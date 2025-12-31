RateBased
=========

Configuration endpoint for ips/rate_based.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.ips.rate_based

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.ips.rate_based.get()



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

Returns a list of rate-based signatures in IPS package.

