Antivirus
=========

Configure a list of hashes to be exempt from AV scanning configuration and management.

Overview
--------

The ``cmdb.antivirus`` category provides configuration management for:

- :doc:`Exempt List <exempt-list>` - Configure a list of hashes to be exempt from AV scanning.
- :doc:`Profile <profile>` - Configure AntiVirus profiles.
- :doc:`Quarantine <quarantine>` - Configure quarantine options.
- :doc:`Settings <settings>` - Configure AntiVirus settings.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.antivirus.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   exempt-list
   profile
   quarantine
   settings

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
