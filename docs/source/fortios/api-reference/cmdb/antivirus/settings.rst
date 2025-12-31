Settings
========

Configuration endpoint for antivirus/settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.antivirus.settings

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.antivirus.settings.get()


   # Update existing item
   result = fgt.api.cmdb.antivirus.settings.put(
       machine_learning_detection='updated-value',
       use_extreme_db='updated-value',
       grayware='updated-value',
       override_timeout='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       machine_learning_detection=None,
       use_extreme_db=None,
       grayware=None,
       override_timeout=None,
       cache_infected_result=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

