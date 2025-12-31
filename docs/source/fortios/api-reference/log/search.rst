Log Search
==========

Advanced log search and query operations across all log types.

Overview
--------

The ``log.search`` category provides powerful search capabilities across multiple log types and storage locations simultaneously.

Endpoint
--------

.. code-block:: python

   fgt.api.log.search

Methods
-------

**.get()**
   Execute advanced log searches

   .. code-block:: python
   
      # Search across all log types
      results = fgt.api.log.search.get(
          logtype='traffic',
          filter='srcip==192.168.1.100',
          rows=100
      )

Parameters
----------

**logtype** (str, required)
   Type of log to search: 'traffic', 'event', 'virus', 'ips', etc.

**filter** (str, optional)
   Filter expression to limit results

**rows** (int, optional)
   Maximum number of results to return

**start** (int, optional)
   Starting row for pagination

**srcintf** (str, optional)
   Filter by source interface

**dstintf** (str, optional)
   Filter by destination interface

Usage Examples
--------------

Basic Search
^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Search traffic logs
   results = fgt.api.log.search.get(
       logtype='traffic',
       rows=100
   )

Advanced Filtering
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Search with multiple criteria
   results = fgt.api.log.search.get(
       logtype='traffic',
       filter='srcip==192.168.1.100&dstport==443',
       rows=50
   )
   
   # Search by interface
   results = fgt.api.log.search.get(
       logtype='traffic',
       srcintf='port1',
       dstintf='wan1',
       rows=100
   )

Search Event Logs
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Search for admin login events
   events = fgt.api.log.search.get(
       logtype='event',
       filter='logdesc==Admin login',
       rows=50
   )

See Also
--------

- :doc:`disk` - Disk logs
- :doc:`memory` - Memory logs
- :doc:`/fortios/guides/filtering` - Advanced filtering guide
