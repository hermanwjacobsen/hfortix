Test
====

Configuration endpoint for user/tacacs_plus.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.tacacs_plus

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.tacacs_plus.post(
       mkey='value',  # optional
       ordinal='value',  # optional
       server='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       ordinal=None,
       server=None,
       secret=None,
       port=None,
       source_ip=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Test the connectivity of the given TACACS+ server.

