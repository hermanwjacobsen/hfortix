.. _system_system_fabric-time-in-sync:

System_Fabric Time In Sync
==========================

Checks whether the other FortiGate device's time in the Security Fabric is in sync with the specified utc timestamp (in seconds) 
 Access Group: any

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.system.system_fabric-time-in-sync

Quick Examples
--------------

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.system.system_fabric-time-in-sync.get()

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.system.system_fabric-time-in-sync.get()

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.system.system_fabric-time-in-sync.get()


Parameters
----------

**utc** (query) - *Optional*
   Type: ``string``
   
   UTC, in seconds, to check against to see if the device's current time is syncronized with.


HTTP Methods
------------

- **GET**: Retrieve a list of N number of PSIRT advisories that the Security Fabric is vulnerable to for a given severity. 
 Access Group: sysgrp.mnt
- **GET**: Checks whether the other FortiGate device's time in the Security Fabric is in sync with the specified utc timestamp (in seconds) 
 Access Group: any
- **GET**: Check if there exists a FortiGate in the Fabric that has an administrative user that will get locked out if firmware is updated to a version that does not support safer passwords. 
 Access Group: any


See Also
--------

- :doc:`index` - System overview
- :doc:`/fortios/api-reference/service/index` - Service API reference
