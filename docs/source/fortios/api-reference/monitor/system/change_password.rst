Select
======

Configuration endpoint for system/change_password.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.change_password

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.change_password.post(
       mkey='value',  # optional
       old_password='value',  # optional
       new_password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       old_password=None,
       new_password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Save admin and guest-admin passwords.

