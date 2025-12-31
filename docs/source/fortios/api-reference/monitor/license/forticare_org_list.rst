ForticareOrgList
================

Configuration endpoint for license/forticare_org_list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.license.forticare_org_list

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.license.forticare_org_list.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get FortiCare organization size and industry lists.

