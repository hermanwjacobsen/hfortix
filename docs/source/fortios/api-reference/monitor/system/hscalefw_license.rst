Upload
======

Configuration endpoint for system/hscalefw_license.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.hscalefw_license

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.hscalefw_license.post(
       license_key='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       license_key=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Update Hyperscale firewall license for hardware acceleration using

