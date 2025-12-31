ForticareResellers
==================

Configuration endpoint for license/forticare_resellers.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.license.forticare_resellers

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.license.forticare_resellers.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       country_code=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get current FortiCare resellers for the requested country.

