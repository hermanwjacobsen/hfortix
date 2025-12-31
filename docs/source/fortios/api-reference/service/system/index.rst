System
======

System service operations.

Overview
--------

The ``service.system`` category provides service operations for:

- :doc:`System_Psirt Vulnerabilities <system-psirt-vulnerabilities>` - Retrieve a list of N number of PSIRT advisories that the Security Fabric is vulnerable to for a given severity. 
 Access Group: sysgrp.mnt
- :doc:`System_Fabric Time In Sync <system-fabric-time-in-sync>` - Checks whether the other FortiGate device's time in the Security Fabric is in sync with the specified utc timestamp (in seconds) 
 Access Group: any
- :doc:`System_Fabric Admin Lockout Exists On Firmware Update <system-fabric-admin-lockout-exists-on-firmware-update>` - Check if there exists a FortiGate in the Fabric that has an administrative user that will get locked out if firmware is updated to a version that does not support safer passwords. 
 Access Group: any


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.service.system.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   system-fabric-admin-lockout-exists-on-firmware-update
   system-fabric-time-in-sync
   system-psirt-vulnerabilities

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
