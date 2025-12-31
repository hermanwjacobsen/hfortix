AddUsers
========

Configuration endpoint for user/banned.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.banned

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.banned.post(
       ip_addresses='value',  # optional
       expiry='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       ip_addresses=None,
       expiry=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Immediately add one or more users to the banned list.

