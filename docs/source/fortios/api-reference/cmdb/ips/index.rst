IPS
===

Overview
--------

The ``cmdb.ips`` namespace provides configuration management for:

- :doc:`Custom <custom>` - Custom configuration endpoint.
- :doc:`Decoder <decoder>` - Decoder configuration endpoint.
- :doc:`Global <global_>` - Global configuration endpoint.
- :doc:`Rule <rule>` - Rule configuration endpoint.
- :doc:`Rule Settings <rule_settings>` - Rule Settings configuration endpoint.
- :doc:`Sensor <sensor>` - Sensor configuration endpoint.
- :doc:`Settings <settings>` - Settings configuration endpoint.
- :doc:`View Map <view_map>` - View Map configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.ips.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   custom
   decoder
   global_
   rule
   rule_settings
   sensor
   settings
   view_map

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
