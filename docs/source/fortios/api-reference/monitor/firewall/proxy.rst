Sessions
========

Configuration endpoint for firewall/proxy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.proxy

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.proxy.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       count,
       ip_version=None,
       summary=None,
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
       dstaddr6=None,
       srcport=None,
       dstport=None,
       srcintf=None,
       dstintf=None,
       policyid=None,
       proxy_policyid=None,
       protocol=None,
       application=None,
       # ... more parameters
   )

List all active proxy sessions (optionally filtered).

