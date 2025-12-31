SdnConnectorFilters
===================

Configuration endpoint for firewall/sdn_connector_filters.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.sdn_connector_filters

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.sdn_connector_filters.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       connector,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List all available filters for a specified SDN Fabric Connector.

