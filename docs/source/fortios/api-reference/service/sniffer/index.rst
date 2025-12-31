Sniffer
=======

Sniffer service operations.

Overview
--------

The ``service.sniffer`` category provides service operations for:

- :doc:`Sniffer_List <sniffer-list>` - Returns list of all packet captures and their status information. 
 Access Group: netgrp.packet-capture
- :doc:`Sniffer_Start <sniffer-start>` - Creates a new packet capture and starts it. 
 Access Group: netgrp.packet-capture
- :doc:`Sniffer_Stop <sniffer-stop>` - Stop a running packet capture. 
 Access Group: netgrp.packet-capture
- :doc:`Sniffer_Download <sniffer-download>` - Returns a PCAP file of the packet capture. 
 Access Group: netgrp.packet-capture
- :doc:`Sniffer_Delete <sniffer-delete>` - Deletes a packet capture. 
 Access Group: netgrp.packet-capture
- :doc:`Sniffer_Meta <sniffer-meta>` - Returns system limitations & meta information of packet capture feature. 
 Access Group: netgrp.packet-capture


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.service.sniffer.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   sniffer-delete
   sniffer-download
   sniffer-list
   sniffer-meta
   sniffer-start
   sniffer-stop

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
