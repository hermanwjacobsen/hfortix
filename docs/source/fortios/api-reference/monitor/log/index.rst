Log
===

Overview
--------

The ``monitor.log`` namespace provides configuration management for:

- :doc:`Av Archive <av_archive>` - Av Archive configuration endpoint.
- :doc:`Current Disk Usage <current_disk_usage>` - Current Disk Usage configuration endpoint.
- :doc:`Device <device>` - Device configuration endpoint.
- :doc:`Feature Set <feature_set>` - Feature Set configuration endpoint.
- :doc:`Fortianalyzer <fortianalyzer>` - Fortianalyzer configuration endpoint.
- :doc:`Fortianalyzer Queue <fortianalyzer_queue>` - Fortianalyzer Queue configuration endpoint.
- :doc:`Forticloud <forticloud>` - Forticloud configuration endpoint.
- :doc:`Forticloud Report <forticloud_report>` - Forticloud Report configuration endpoint.
- :doc:`Forticloud Report List <forticloud_report_list>` - Forticloud Report List configuration endpoint.
- :doc:`Historic Daily Remote Logs <historic_daily_remote_logs>` - Historic Daily Remote Logs configuration endpoint.
- :doc:`Hourly Disk Usage <hourly_disk_usage>` - Hourly Disk Usage configuration endpoint.
- :doc:`Local Report <local_report>` - Local Report configuration endpoint.
- :doc:`Local Report List <local_report_list>` - Local Report List configuration endpoint.
- :doc:`Policy Archive <policy_archive>` - Policy Archive configuration endpoint.
- :doc:`Stats <stats>` - Stats configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.log.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   av_archive
   current_disk_usage
   device
   feature_set
   fortianalyzer
   fortianalyzer_queue
   forticloud
   forticloud_report
   forticloud_report_list
   historic_daily_remote_logs
   hourly_disk_usage
   local_report
   local_report_list
   policy_archive
   stats

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
