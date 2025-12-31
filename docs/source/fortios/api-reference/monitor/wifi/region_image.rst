Upload
======

Configuration endpoint for wifi/region_image.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.region_image

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.region_image.post(
       region_name='value',  # optional
       image_type='value',  # optional
       file_content='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       region_name=None,
       image_type=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Saves a floorplan/region image to an existing region.

