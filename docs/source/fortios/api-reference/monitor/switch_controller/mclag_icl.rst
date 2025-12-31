EligiblePeer
============

Configuration endpoint for switch_controller/mclag_icl.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.mclag_icl

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.switch_controller.mclag_icl.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       fortilink,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Find a pair of FortiSwitches that are eligible to form a tier-1 MC-LAG.

