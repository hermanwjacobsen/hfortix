L2tp
====

Configuration endpoint for vpn/l2tp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.l2tp

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.vpn.l2tp.get()


   # Update existing item
   result = fgt.api.cmdb.vpn.l2tp.put(
       status='updated-value',
       eip='updated-value',
       sip='updated-value',
       usrgrp='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       eip=None,
       sip=None,
       usrgrp=None,
       enforce_ipsec=None,
       lcp_echo_interval=None,
       lcp_max_echo_fails=None,
       hello_interval=None,
       compress=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

