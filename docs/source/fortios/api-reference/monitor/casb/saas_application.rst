Details
=======

Configuration endpoint for casb/saas_application.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.casb.saas_application

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.casb.saas_application.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve details for CASB SaaS applications.

