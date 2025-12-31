ImportLanguage
==============

Configuration endpoint for web_ui/language.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.web_ui.language

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.web_ui.language.post(
       file_content='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Import localization language file to this FortiGate.

