ChangePassword
==============

Configuration endpoint for user/local.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.local

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.local.post(
       username='value',  # optional
       new_password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       username=None,
       new_password=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Change password for local user.

