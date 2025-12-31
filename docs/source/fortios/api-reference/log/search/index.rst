Search
======

Advanced log search operations across all log types.

Overview
--------

The ``log.search`` category provides advanced search capabilities across all log storage locations.

Python Usage
------------

**Free-Style Search:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Perform advanced search
   results = fgt.api.log.search.free_style.post(json={
       'logtype': 'traffic',
       'filters': [{
           'field': 'srcip',
           'operator': '==',
           'value': '192.168.1.100'
       }]
   })

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/guides/filtering` - Filtering guide
