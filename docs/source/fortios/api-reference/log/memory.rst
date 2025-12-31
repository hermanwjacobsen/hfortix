Log Memory
==========

Query logs stored in device memory for fast access.

Overview
--------

The ``log.memory`` category provides access to logs stored in the FortiGate's RAM. Memory logs are faster to query but have limited capacity compared to disk logs.

Endpoint
--------

.. code-block:: python

   fgt.api.log.memory

Methods
-------

**.get()**
   Query memory logs with filtering

   .. code-block:: python
   
      # Get recent traffic logs from memory
      logs = fgt.api.log.memory.traffic.get(rows=100)
      
      # Filter by source IP
      logs = fgt.api.log.memory.traffic.get(
          filter='srcip==192.168.1.100',
          rows=50
      )

Parameters
----------

**rows** (int, optional)
   Maximum number of log entries to return. Default: 100

**filter** (str, optional)
   Filter expression to limit results

**start** (int, optional)
   Starting row number for pagination

Log Types Available
-------------------

Same log types as disk logs:

- **traffic** - Traffic logs
- **event** - System event logs
- **virus** - Antivirus logs
- **ips** - IPS logs
- **webfilter** - Web filter logs
- And all other log types available in disk

Usage Examples
--------------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query memory logs (faster)
   logs = fgt.api.log.memory.traffic.get(rows=100)
   
   # Filter by criteria
   logs = fgt.api.log.memory.traffic.get(
       filter='action==deny',
       rows=50
   )

Performance Considerations
--------------------------

**Memory logs are faster** because they're stored in RAM, but:

- Limited capacity (typically stores recent logs only)
- Lost on reboot
- Recommended for real-time monitoring

**Disk logs** persist and have larger capacity but are slower to query.

See Also
--------

- :doc:`disk` - Disk logs (persistent storage)
- :doc:`/fortios/guides/filtering` - Log filtering guide
