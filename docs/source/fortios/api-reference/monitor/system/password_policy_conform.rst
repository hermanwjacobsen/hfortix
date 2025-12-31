Select
======

Configuration endpoint for system/password_policy_conform.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.password_policy_conform

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.password_policy_conform.post(
       mkey='value',  # optional
       apply_to='value',  # optional
       password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       apply_to=None,
       password=None,
       old_password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check whether password conforms to the password policy.

