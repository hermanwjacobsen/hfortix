Reset
=====

Configuration endpoint for webfilter/category_quota.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.webfilter.category_quota

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.webfilter.category_quota.post(
       profile='value',  # optional
       user='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       profile=None,
       user=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset webfilter quota for user or IP.

