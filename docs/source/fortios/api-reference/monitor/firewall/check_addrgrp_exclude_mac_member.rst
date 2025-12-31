CheckAddrgrpExcludeMacMember
============================

Configuration endpoint for firewall/check_addrgrp_exclude_mac_member.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       ip_version=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check if the IPv4 or IPv6 address group should exclude mac address type

