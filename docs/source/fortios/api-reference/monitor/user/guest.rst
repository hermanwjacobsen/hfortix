Email
=====

Configuration endpoint for user/guest.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.guest

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.guest.post(
       group='value',  # optional
       guest='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       group=None,
       guest=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Sent guest login details via email.

