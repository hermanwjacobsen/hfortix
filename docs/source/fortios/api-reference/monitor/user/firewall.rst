Auth
====

Configuration endpoint for user/firewall.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.firewall

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.firewall.post(
       username='value',  # optional
       ip='value',  # optional
       server='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       username=None,
       ip=None,
       server=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Trigger authentication for a single firewall user.

