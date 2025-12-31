FileFilter
==========

Configuration endpoint for file_filter.

Python Attribute
----------------

.. code-block:: python

   fgt.api.log.file_filter

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.log.file_filter.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       rows=None,
       session_id=None,
       serial_no=None,
       is_ha_member=None,
       filter=None,
       extra=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get file-filter logs (formatted).

