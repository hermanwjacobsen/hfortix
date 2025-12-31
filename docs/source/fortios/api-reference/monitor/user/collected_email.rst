CollectedEmail
==============

Configuration endpoint for user/collected_email.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.collected_email

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.user.collected_email.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List email addresses collected from captive portal.

