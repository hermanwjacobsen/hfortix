Service System
==============

System service operations and management.

Overview
--------

The ``service.system`` category provides control over various FortiGate system services and operations.

Endpoint
--------

.. code-block:: python

   fgt.api.service.system

Methods
-------

**.get()**
   Get system service status

   .. code-block:: python
   
      # Get service status
      status = fgt.api.service.system.get()

**.post()**
   Execute system service operations

   .. code-block:: python
   
      # Perform system operation
      result = fgt.api.service.system.post(json={'action': 'reboot'})

Usage Examples
--------------

Get Service Status
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get system service status
   status = fgt.api.service.system.get()
   
   print(f"Services: {status}")

Available Operations
--------------------

The specific operations available depend on the FortiOS version and configuration. Common operations include:

- System diagnostics
- Service restarts
- Configuration backups
- System maintenance tasks

.. warning::
   Some system service operations may be disruptive. Always verify the operation before executing in production environments.

See Also
--------

- :doc:`sniffer` - Packet capture operations
- :doc:`security-rating` - Security assessment
- :doc:`/fortios/api-reference/monitor/system` - System monitoring
