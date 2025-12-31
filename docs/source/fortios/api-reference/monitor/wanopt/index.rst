Wanopt
======

Overview
--------

The ``monitor.wanopt`` namespace provides configuration management for:

- :doc:`History <history>` - History configuration endpoint.
- :doc:`Peer Stats <peer_stats>` - Peer Stats configuration endpoint.
- :doc:`Webcache <webcache>` - Webcache configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.wanopt.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   history
   peer_stats
   webcache

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
