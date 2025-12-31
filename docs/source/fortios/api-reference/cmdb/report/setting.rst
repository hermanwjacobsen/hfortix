Setting
=======

Configuration endpoint for report/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.report.setting

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
   items = fgt.api.cmdb.report.setting.get()


   # Update existing item
   result = fgt.api.cmdb.report.setting.put(
       pdf_report='updated-value',
       fortiview='updated-value',
       report_source='updated-value',
       web_browsing_threshold='updated-value',
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
       pdf_report=None,
       fortiview=None,
       report_source=None,
       web_browsing_threshold=None,
       top_n=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

