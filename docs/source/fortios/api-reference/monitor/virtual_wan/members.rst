Members
=======

Configuration endpoint for virtual_wan/members.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.virtual_wan.members

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.virtual_wan.members.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       interface=None,
       zone=None,
       sla=None,
       skip_vpn_child=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve interface statistics for each SD-WAN link.

