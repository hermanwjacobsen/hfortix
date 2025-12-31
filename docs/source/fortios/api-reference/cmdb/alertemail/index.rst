Alertemail
==========

Configure alert email settings configuration and management.

Overview
--------

The ``cmdb.alertemail`` category provides configuration management for:

- :doc:`Setting <setting>` - Configure alert email settings.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.alertemail.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   setting

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
