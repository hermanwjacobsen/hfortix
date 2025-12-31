Security Rating
===============

Security posture assessment and scoring.

Overview
--------

The ``service.security_rating`` category provides security rating and assessment capabilities.

Python Usage
------------

**Get Security Rating:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get overall security rating
   rating = fgt.api.service.security_rating.report.get()
   print(f"Security score: {rating['overall_score']}")
   
   # Get security recommendations
   recommendations = fgt.api.service.security_rating.recommendations.get()

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
