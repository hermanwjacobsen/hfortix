Answers
=======

Configuration endpoint for fortiguard/answers.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiguard.answers

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiguard.answers.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       page=None,
       pagesize=None,
       sortkey=None,
       topics=None,
       limit=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of questions on answers.

