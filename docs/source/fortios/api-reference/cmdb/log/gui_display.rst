GuiDisplay
==========

Configuration endpoint for log/gui_display.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.log.gui_display

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
   items = fgt.api.cmdb.log.gui_display.get()


   # Update existing item
   result = fgt.api.cmdb.log.gui_display.put(
       resolve_hosts='updated-value',
       resolve_apps='updated-value',
       fortiview_unscanned_apps='updated-value',
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
       resolve_hosts=None,
       resolve_apps=None,
       fortiview_unscanned_apps=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

