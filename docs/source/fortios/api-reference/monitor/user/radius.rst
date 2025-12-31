GetTestConnect
==============

Configuration endpoint for user/radius.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.radius

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.user.radius.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       ordinal=None,
       server=None,
       secret=None,
       auth_type=None,
       user=None,
       password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Test the connectivity of the given RADIUS server and, optionally, the

