Cancel
======

Configuration endpoint for fortiview/session.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiview.session

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.fortiview.session.post(
       sessionid='value',  # optional
       device='value',  # optional
       report_by='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       sessionid=None,
       device=None,
       report_by=None,
       view_level=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Cancel a FortiView request session.

