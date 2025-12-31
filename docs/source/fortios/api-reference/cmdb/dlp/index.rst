Dlp
===

Overview
--------

The ``cmdb.dlp`` namespace provides configuration management for:

- :doc:`Data Type <data_type>` - Data Type configuration endpoint.
- :doc:`Dictionary <dictionary>` - Dictionary configuration endpoint.
- :doc:`Exact Data Match <exact_data_match>` - Exact Data Match configuration endpoint.
- :doc:`Filepattern <filepattern>` - Filepattern configuration endpoint.
- :doc:`Label <label>` - Label configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Sensor <sensor>` - Sensor configuration endpoint.
- :doc:`Settings <settings>` - Settings configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.dlp.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   data_type
   dictionary
   exact_data_match
   filepattern
   label
   profile
   sensor
   settings

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
