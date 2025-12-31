Emailfilter
===========

Configure anti-spam block/allow list configuration and management.

Overview
--------

The ``cmdb.emailfilter`` category provides configuration management for:

- :ref:`Block Allow List <emailfilter-block-allow-list>` - Configure anti-spam block/allow list.
- :ref:`Bword <emailfilter-bword>` - Configure AntiSpam banned word list.
- :ref:`Dnsbl <emailfilter-dnsbl>` - Configure AntiSpam DNSBL/ORBL.
- :ref:`Fortishield <emailfilter-fortishield>` - Configure FortiGuard - AntiSpam.
- :ref:`Iptrust <emailfilter-iptrust>` - Configure AntiSpam IP trust.
- :ref:`Mheader <emailfilter-mheader>` - Configure AntiSpam MIME header.
- :ref:`Options <emailfilter-options>` - Configure AntiSpam options.
- :ref:`Profile <emailfilter-profile>` - Configure Email Filter profiles.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.emailfilter

Available Endpoints
-------------------

.. _emailfilter-block-allow-list:

block-allow-list
~~~~~~~~~~~~~~~~

Configure anti-spam block/allow list.

**Python attribute:** ``block_allow_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.block_allow_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.block_allow_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.block_allow_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.block_allow_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.block_allow_list.delete(mkey='item-name')

.. _emailfilter-bword:

bword
~~~~~

Configure AntiSpam banned word list.

**Python attribute:** ``bword``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.bword.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.bword.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.bword.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.bword.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.bword.delete(mkey='item-name')

.. _emailfilter-dnsbl:

dnsbl
~~~~~

Configure AntiSpam DNSBL/ORBL.

**Python attribute:** ``dnsbl``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.dnsbl.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.dnsbl.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.dnsbl.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.dnsbl.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.dnsbl.delete(mkey='item-name')

.. _emailfilter-fortishield:

fortishield
~~~~~~~~~~~

Configure FortiGuard - AntiSpam.

**Python attribute:** ``fortishield``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.fortishield.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.fortishield.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.fortishield.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.fortishield.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.fortishield.delete(mkey='item-name')

.. _emailfilter-iptrust:

iptrust
~~~~~~~

Configure AntiSpam IP trust.

**Python attribute:** ``iptrust``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.iptrust.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.iptrust.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.iptrust.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.iptrust.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.iptrust.delete(mkey='item-name')

.. _emailfilter-mheader:

mheader
~~~~~~~

Configure AntiSpam MIME header.

**Python attribute:** ``mheader``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.mheader.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.mheader.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.mheader.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.mheader.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.mheader.delete(mkey='item-name')

.. _emailfilter-options:

options
~~~~~~~

Configure AntiSpam options.

**Python attribute:** ``options``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.options.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.options.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.options.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.options.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.options.delete(mkey='item-name')

.. _emailfilter-profile:

profile
~~~~~~~

Configure Email Filter profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.emailfilter.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.emailfilter.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.emailfilter.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.emailfilter.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.emailfilter.profile.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.emailfilter.block_allow_list.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.emailfilter.block_allow_list.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.emailfilter.block_allow_list.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.emailfilter.block_allow_list.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.emailfilter.block_allow_list.delete(mkey='config-name')

HTTP Methods
------------

All CMDB endpoints support standard HTTP methods:

**.get()**
   HTTP GET - Retrieve configuration(s)

**.post()**
   HTTP POST - Create new configuration

**.put()**
   HTTP PUT - Update existing configuration

**.delete()**
   HTTP DELETE - Remove configuration

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
