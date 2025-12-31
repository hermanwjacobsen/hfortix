Close
=====

Configuration endpoint for firewall/session.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.session

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.session.post(
       pro='value',  # optional
       saddr='value',  # optional
       daddr='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       pro=None,
       saddr=None,
       daddr=None,
       sport=None,
       dport=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Close a single firewall session that matches all provided criteria.

