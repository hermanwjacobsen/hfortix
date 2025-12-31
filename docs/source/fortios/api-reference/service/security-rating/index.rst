Security Rating
===============

Security Rating service operations.

Overview
--------

The ``service.security-rating`` category provides service operations for:

- :doc:`Security Rating_Report <security-rating-report>` - Retrieve full report of all Security Rating tests. 
 Access Group: secfabgrp.csfsys
- :doc:`Security Rating_Recommendations <security-rating-recommendations>` - Retrieve recommendations for Security Rating tests. 
 Access Group: secfabgrp.csfsys


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.service.security-rating.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   security-rating-recommendations
   security-rating-report

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
