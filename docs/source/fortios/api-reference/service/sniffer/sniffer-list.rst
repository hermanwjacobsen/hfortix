.. _sniffer_sniffer_list:

Sniffer_List
============

Returns list of all packet captures and their status information. 
 Access Group: netgrp.packet-capture

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.sniffer.sniffer_list

Quick Examples
--------------

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.get()

**Execute Service (POST)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.post(data={})

**Execute Service (POST)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.post(data={})

**Execute Service (POST)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.post(data={})

**Execute Service (POST)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.post(data={})

**Query Service (GET)**

.. code-block:: python

   # Execute service operation
   response = fgt.api.service.sniffer.sniffer_list.get()


Parameters
----------

**mkey** (query) - *Optional*
   Type: ``string``
   
   Filters by packet capture name.

**body** (body) - **Required**
   Type: ``string``
   
   Possible parameters to go in the body for the request.

**body** (body) - **Required**
   Type: ``string``
   
   Possible parameters to go in the body for the request.

**body** (body) - **Required**
   Type: ``string``
   
   Possible parameters to go in the body for the request.

**body** (body) - **Required**
   Type: ``string``
   
   Possible parameters to go in the body for the request.


HTTP Methods
------------

- **GET**: Returns list of all packet captures and their status information. 
 Access Group: netgrp.packet-capture
- **POST**: Creates a new packet capture and starts it. 
 Access Group: netgrp.packet-capture
- **POST**: Stop a running packet capture. 
 Access Group: netgrp.packet-capture
- **POST**: Returns a PCAP file of the packet capture. 
 Access Group: netgrp.packet-capture
- **POST**: Deletes a packet capture. 
 Access Group: netgrp.packet-capture
- **GET**: Returns system limitations & meta information of packet capture feature. 
 Access Group: netgrp.packet-capture


See Also
--------

- :doc:`index` - Sniffer overview
- :doc:`/fortios/api-reference/service/index` - Service API reference
