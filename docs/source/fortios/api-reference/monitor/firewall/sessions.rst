Sessions
========

Configuration endpoint for firewall/sessions.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.sessions

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.sessions.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       count,
       ip_version=None,
       summary=None,
       srcport=None,
       policyid=None,
       security_policyid=None,
       application=None,
       protocol=None,
       dstport=None,
       srcintf=None,
       dstintf=None,
       srcintfrole=None,
       dstintfrole=None,
       srcaddr=None,
       srcaddr6=None,
       # ... more parameters
   )

List all active firewall sessions (optionally filtered).

