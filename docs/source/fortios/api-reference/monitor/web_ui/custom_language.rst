Create
======

Configuration endpoint for web_ui/custom_language.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.web_ui.custom_language

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.web_ui.custom_language.post(
       lang_name='value',  # optional
       lang_comments='value',  # optional
       file_content='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       lang_name=None,
       lang_comments=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Upload custom language file to this Fortigate.

