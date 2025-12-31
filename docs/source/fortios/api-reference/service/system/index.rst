System
======

System service operations and management.

Overview
--------

The ``service.system`` category provides various system service operations and maintenance tasks.

Python Usage
------------

**System Operations:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Check PSIRT vulnerabilities
   vulns = fgt.api.service.system.psirt_vulnerabilities.get()
   
   # Check fabric time sync
   time_sync = fgt.api.service.system.fabric_time_in_sync.get()
   
   # Check fabric admin lockout
   lockout = fgt.api.service.system.fabric_admin_lockout_exists_on_firmware_update.get()

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
