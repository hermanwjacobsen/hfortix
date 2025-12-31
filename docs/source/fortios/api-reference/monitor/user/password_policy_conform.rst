Select
======

Configuration endpoint for user/password_policy_conform.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.password_policy_conform

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.password_policy_conform.post(
       username='value',  # optional
       password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       username=None,
       password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check if password adheres to local user password policy.

