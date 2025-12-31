Dlp
===

Configure predefined data type used by DLP blocking configuration and management.

Overview
--------

The ``cmdb.dlp`` category provides configuration management for:

- :doc:`Data Type <data-type>` - Configure predefined data type used by DLP blocking.
- :doc:`Dictionary <dictionary>` - Configure dictionaries used by DLP blocking.
- :doc:`Exact Data Match <exact-data-match>` - Configure exact-data-match template used by DLP scan.
- :doc:`Filepattern <filepattern>` - Configure file patterns used by DLP blocking.
- :doc:`Label <label>` - Configure labels used by DLP blocking.
- :doc:`Profile <profile>` - Configure DLP profiles.
- :doc:`Sensor <sensor>` - Configure sensors used by DLP blocking.
- :doc:`Settings <settings>` - Configure settings for DLP.


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
   
   data-type
   dictionary
   exact-data-match
   filepattern
   label
   profile
   sensor
   settings

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
