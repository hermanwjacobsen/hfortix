Profile
=======

Configuration endpoint for emailfilter/profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.emailfilter.profile

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
   items = fgt.api.cmdb.emailfilter.profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.emailfilter.profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.emailfilter.profile.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.emailfilter.profile.put(
       name='updated-value',
       comment='updated-value',
       feature_set='updated-value',
       replacemsg_group='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.emailfilter.profile.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
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
       name=None,
       comment=None,
       feature_set=None,
       replacemsg_group=None,
       spam_log=None,
       spam_log_fortiguard_response=None,
       spam_filtering=None,
       external=None,
       options=None,
       imap=None,
       pop3=None,
       smtp=None,
       other_webmails=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       comment=None,
       feature_set=None,
       replacemsg_group=None,
       spam_log=None,
       spam_log_fortiguard_response=None,
       spam_filtering=None,
       external=None,
       options=None,
       imap=None,
       pop3=None,
       smtp=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

