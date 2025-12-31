Log
===

Configure filters for local disk logging configuration and management.

Overview
--------

The ``cmdb.log`` category provides configuration management for:

- :doc:`Custom Field <custom-field>` - Configure custom log fields.
- :doc:`Eventfilter <eventfilter>` - Configure log event filters.
- :doc:`Gui Display <gui-display>` - Configure how log messages are displayed on the GUI.
- :doc:`Setting <setting>` - Configure general log settings.
- :doc:`Threat Weight <threat-weight>` - Configure threat weight settings.


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
   
   custom-field
   eventfilter
   gui-display
   setting
   threat-weight

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
