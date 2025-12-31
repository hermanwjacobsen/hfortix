Ips
===

Configure IPS custom signature configuration and management.

Overview
--------

The ``cmdb.ips`` category provides configuration management for:

- :doc:`Custom <custom>` - Configure IPS custom signature.
- :doc:`Decoder <decoder>` - Configure IPS decoder.
- :doc:`Global <global>` - Configure IPS global parameter.
- :doc:`Rule <rule>` - Configure IPS rules.
- :doc:`Rule Settings <rule-settings>` - Configure IPS rule setting.
- :doc:`Sensor <sensor>` - Configure IPS sensor.
- :doc:`Settings <settings>` - Configure IPS VDOM parameter.
- :doc:`View Map <view-map>` - Configure IPS view-map.


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
   global
   rule
   rule-settings
   sensor
   settings
   view-map

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
