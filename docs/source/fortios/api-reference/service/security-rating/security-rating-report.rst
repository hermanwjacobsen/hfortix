.. _security-rating_security-rating_report:

Security Rating_Report
======================

Retrieve full report of all Security Rating tests. 
 Access Group: secfabgrp.csfsys

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.security-rating.security-rating_report

Quick Examples
--------------

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.security-rating.security-rating_report.get()

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.security-rating.security-rating_report.get()


Parameters
----------

**scope** (query) - *Optional*
   Type: ``string``
   
   Scope of the request [global | vdom*].

**standalone** (query) - *Optional*
   Type: ``string``
   
   If enabled this will only return a report with checks for the current FortiGate.

**type** (query) - **Required**
   Type: ``string``
   
   The report sub-type to fetch ['psirt', 'insight'].

**checks** (query) - *Optional*
   Type: ``string``
   
   Retrieve a report with only the given Security Rating checks.

**show-hidden** (query) - *Optional*
   Type: ``string``
   
   Show hidden Security Rating controls in the report.

**checks** (query) - **Required**
   Type: ``string``
   
   Retrieve the recommendations for the given Security Rating checks.

**scope** (query) - *Optional*
   Type: ``string``
   
   Scope of the request [global | vdom*].


HTTP Methods
------------

- **GET**: Retrieve full report of all Security Rating tests. 
 Access Group: secfabgrp.csfsys
- **GET**: Retrieve recommendations for Security Rating tests. 
 Access Group: secfabgrp.csfsys


See Also
--------

- :doc:`index` - Security Rating overview
- :doc:`/fortios/api-reference/service/index` - Service API reference
