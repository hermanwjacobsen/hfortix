Web Ui
======

Overview
--------

The ``monitor.web_ui`` namespace provides configuration management for:

- :doc:`Custom Language <custom_language>` - Custom Language configuration endpoint.
- :doc:`Language <language>` - Language configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.web_ui.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   custom_language
   language

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
