Antivirus
=========

Overview
--------

The ``cmdb.antivirus`` namespace provides configuration management for:

- :doc:`Exempt List <exempt_list>` - Exempt List configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Quarantine <quarantine>` - Quarantine configuration endpoint.
- :doc:`Settings <settings>` - Settings configuration endpoint.


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
   
   exempt_list
   profile
   quarantine
   settings

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
