Upgrade
=======

Configuration endpoint for license/database.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.license.database

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.license.database.post(
       db_name='value',  # optional
       confirm_not_signed='value',  # optional
       confirm_not_ga_certified='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       db_name=None,
       confirm_not_signed=None,
       confirm_not_ga_certified=None,
       file_id=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Upgrade or downgrade UTM engine or signature package

