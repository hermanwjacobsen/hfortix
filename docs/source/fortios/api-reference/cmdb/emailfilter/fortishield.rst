Fortishield
===========

Configuration endpoint for emailfilter/fortishield.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.emailfilter.fortishield

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
   items = fgt.api.cmdb.emailfilter.fortishield.get()


   # Update existing item
   result = fgt.api.cmdb.emailfilter.fortishield.put(
       spam_submit_srv='updated-value',
       spam_submit_force='updated-value',
       spam_submit_txt2htm='updated-value',
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
       spam_submit_srv=None,
       spam_submit_force=None,
       spam_submit_txt2htm=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

