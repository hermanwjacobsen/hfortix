FtgdLocalRisk
=============

Configuration endpoint for webfilter/ftgd_local_risk.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.webfilter.ftgd_local_risk

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.webfilter.ftgd_local_risk.get()


   # Create new item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.post(
       nkey='value',  # optional
       url='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.put(
       url='updated-value',
       status='updated-value',
       comment='updated-value',
       risk_score='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.webfilter.ftgd_local_risk.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       url=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       url=None,
       status=None,
       comment=None,
       risk_score=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       url=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       comment=None,
       risk_score=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       url=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

