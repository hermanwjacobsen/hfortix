Log
===

Overview
--------

The ``cmdb.log`` namespace provides configuration management for:

- :doc:`Custom Field <custom_field>` - Custom Field configuration endpoint.
- :doc:`Disk Filter <disk_filter>` - Disk Filter configuration endpoint.
- :doc:`Disk Setting <disk_setting>` - Disk Setting configuration endpoint.
- :doc:`Eventfilter <eventfilter>` - Eventfilter configuration endpoint.
- :doc:`Fortianalyzer2 Filter <fortianalyzer2_filter>` - Fortianalyzer2 Filter configuration endpoint.
- :doc:`Fortianalyzer2 Override Filter <fortianalyzer2_override_filter>` - Fortianalyzer2 Override Filter configuration endpoint.
- :doc:`Fortianalyzer2 Override Setting <fortianalyzer2_override_setting>` - Fortianalyzer2 Override Setting configuration endpoint.
- :doc:`Fortianalyzer2 Setting <fortianalyzer2_setting>` - Fortianalyzer2 Setting configuration endpoint.
- :doc:`Fortianalyzer3 Filter <fortianalyzer3_filter>` - Fortianalyzer3 Filter configuration endpoint.
- :doc:`Fortianalyzer3 Override Filter <fortianalyzer3_override_filter>` - Fortianalyzer3 Override Filter configuration endpoint.
- :doc:`Fortianalyzer3 Override Setting <fortianalyzer3_override_setting>` - Fortianalyzer3 Override Setting configuration endpoint.
- :doc:`Fortianalyzer3 Setting <fortianalyzer3_setting>` - Fortianalyzer3 Setting configuration endpoint.
- :doc:`Fortianalyzer Cloud Filter <fortianalyzer_cloud_filter>` - Fortianalyzer Cloud Filter configuration endpoint.
- :doc:`Fortianalyzer Cloud Override Filter <fortianalyzer_cloud_override_filter>` - Fortianalyzer Cloud Override Filter configuration endpoint.
- :doc:`Fortianalyzer Cloud Override Setting <fortianalyzer_cloud_override_setting>` - Fortianalyzer Cloud Override Setting configuration endpoint.
- :doc:`Fortianalyzer Cloud Setting <fortianalyzer_cloud_setting>` - Fortianalyzer Cloud Setting configuration endpoint.
- :doc:`Fortianalyzer Filter <fortianalyzer_filter>` - Fortianalyzer Filter configuration endpoint.
- :doc:`Fortianalyzer Override Filter <fortianalyzer_override_filter>` - Fortianalyzer Override Filter configuration endpoint.
- :doc:`Fortianalyzer Override Setting <fortianalyzer_override_setting>` - Fortianalyzer Override Setting configuration endpoint.
- :doc:`Fortianalyzer Setting <fortianalyzer_setting>` - Fortianalyzer Setting configuration endpoint.
- :doc:`Fortiguard Filter <fortiguard_filter>` - Fortiguard Filter configuration endpoint.
- :doc:`Fortiguard Override Filter <fortiguard_override_filter>` - Fortiguard Override Filter configuration endpoint.
- :doc:`Fortiguard Override Setting <fortiguard_override_setting>` - Fortiguard Override Setting configuration endpoint.
- :doc:`Fortiguard Setting <fortiguard_setting>` - Fortiguard Setting configuration endpoint.
- :doc:`Gui Display <gui_display>` - Gui Display configuration endpoint.
- :doc:`Memory Filter <memory_filter>` - Memory Filter configuration endpoint.
- :doc:`Memory Global Setting <memory_global_setting>` - Memory Global Setting configuration endpoint.
- :doc:`Memory Setting <memory_setting>` - Memory Setting configuration endpoint.
- :doc:`Null Device Filter <null_device_filter>` - Null Device Filter configuration endpoint.
- :doc:`Null Device Setting <null_device_setting>` - Null Device Setting configuration endpoint.
- :doc:`Setting <setting>` - Setting configuration endpoint.
- :doc:`Syslogd2 Filter <syslogd2_filter>` - Syslogd2 Filter configuration endpoint.
- :doc:`Syslogd2 Override Filter <syslogd2_override_filter>` - Syslogd2 Override Filter configuration endpoint.
- :doc:`Syslogd2 Override Setting <syslogd2_override_setting>` - Syslogd2 Override Setting configuration endpoint.
- :doc:`Syslogd2 Setting <syslogd2_setting>` - Syslogd2 Setting configuration endpoint.
- :doc:`Syslogd3 Filter <syslogd3_filter>` - Syslogd3 Filter configuration endpoint.
- :doc:`Syslogd3 Override Filter <syslogd3_override_filter>` - Syslogd3 Override Filter configuration endpoint.
- :doc:`Syslogd3 Override Setting <syslogd3_override_setting>` - Syslogd3 Override Setting configuration endpoint.
- :doc:`Syslogd3 Setting <syslogd3_setting>` - Syslogd3 Setting configuration endpoint.
- :doc:`Syslogd4 Filter <syslogd4_filter>` - Syslogd4 Filter configuration endpoint.
- :doc:`Syslogd4 Override Filter <syslogd4_override_filter>` - Syslogd4 Override Filter configuration endpoint.
- :doc:`Syslogd4 Override Setting <syslogd4_override_setting>` - Syslogd4 Override Setting configuration endpoint.
- :doc:`Syslogd4 Setting <syslogd4_setting>` - Syslogd4 Setting configuration endpoint.
- :doc:`Syslogd Filter <syslogd_filter>` - Syslogd Filter configuration endpoint.
- :doc:`Syslogd Override Filter <syslogd_override_filter>` - Syslogd Override Filter configuration endpoint.
- :doc:`Syslogd Override Setting <syslogd_override_setting>` - Syslogd Override Setting configuration endpoint.
- :doc:`Syslogd Setting <syslogd_setting>` - Syslogd Setting configuration endpoint.
- :doc:`Tacacs Plus Accounting2 Filter <tacacs_plus_accounting2_filter>` - Tacacs Plus Accounting2 Filter configuration endpoint.
- :doc:`Tacacs Plus Accounting2 Setting <tacacs_plus_accounting2_setting>` - Tacacs Plus Accounting2 Setting configuration endpoint.
- :doc:`Tacacs Plus Accounting3 Filter <tacacs_plus_accounting3_filter>` - Tacacs Plus Accounting3 Filter configuration endpoint.
- :doc:`Tacacs Plus Accounting3 Setting <tacacs_plus_accounting3_setting>` - Tacacs Plus Accounting3 Setting configuration endpoint.
- :doc:`Tacacs Plus Accounting Filter <tacacs_plus_accounting_filter>` - Tacacs Plus Accounting Filter configuration endpoint.
- :doc:`Tacacs Plus Accounting Setting <tacacs_plus_accounting_setting>` - Tacacs Plus Accounting Setting configuration endpoint.
- :doc:`Threat Weight <threat_weight>` - Threat Weight configuration endpoint.
- :doc:`Webtrends Filter <webtrends_filter>` - Webtrends Filter configuration endpoint.
- :doc:`Webtrends Setting <webtrends_setting>` - Webtrends Setting configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.log.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   custom_field
   disk_filter
   disk_setting
   eventfilter
   fortianalyzer2_filter
   fortianalyzer2_override_filter
   fortianalyzer2_override_setting
   fortianalyzer2_setting
   fortianalyzer3_filter
   fortianalyzer3_override_filter
   fortianalyzer3_override_setting
   fortianalyzer3_setting
   fortianalyzer_cloud_filter
   fortianalyzer_cloud_override_filter
   fortianalyzer_cloud_override_setting
   fortianalyzer_cloud_setting
   fortianalyzer_filter
   fortianalyzer_override_filter
   fortianalyzer_override_setting
   fortianalyzer_setting
   fortiguard_filter
   fortiguard_override_filter
   fortiguard_override_setting
   fortiguard_setting
   gui_display
   memory_filter
   memory_global_setting
   memory_setting
   null_device_filter
   null_device_setting
   setting
   syslogd2_filter
   syslogd2_override_filter
   syslogd2_override_setting
   syslogd2_setting
   syslogd3_filter
   syslogd3_override_filter
   syslogd3_override_setting
   syslogd3_setting
   syslogd4_filter
   syslogd4_override_filter
   syslogd4_override_setting
   syslogd4_setting
   syslogd_filter
   syslogd_override_filter
   syslogd_override_setting
   syslogd_setting
   tacacs_plus_accounting2_filter
   tacacs_plus_accounting2_setting
   tacacs_plus_accounting3_filter
   tacacs_plus_accounting3_setting
   tacacs_plus_accounting_filter
   tacacs_plus_accounting_setting
   threat_weight
   webtrends_filter
   webtrends_setting

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
