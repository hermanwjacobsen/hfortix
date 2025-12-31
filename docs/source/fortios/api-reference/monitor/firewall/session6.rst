CloseMultiple
=============

Configuration endpoint for firewall/session6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.session6

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.session6.post(
       proto='value',  # optional
       saddr='value',  # optional
       daddr='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       proto=None,
       saddr=None,
       daddr=None,
       sport=None,
       dport=None,
       policy=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Close multiple IPv6 firewall sessions which match the provided

