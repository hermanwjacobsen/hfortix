License
=======

Overview
--------

The ``monitor.license`` namespace provides configuration management for:

- :doc:`Database <database>` - Database configuration endpoint.
- :doc:`Fortianalyzer Status <fortianalyzer_status>` - Fortianalyzer Status configuration endpoint.
- :doc:`Forticare Org List <forticare_org_list>` - Forticare Org List configuration endpoint.
- :doc:`Forticare Resellers <forticare_resellers>` - Forticare Resellers configuration endpoint.
- :doc:`Status <status>` - Status configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.license.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   database
   fortianalyzer_status
   forticare_org_list
   forticare_resellers
   status

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
