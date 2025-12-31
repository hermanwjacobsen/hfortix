Sniffer
=======

Packet capture (sniffer) operations for network troubleshooting.

Overview
--------

The ``service.sniffer`` category provides control over packet capture operations on the FortiGate.

Python Usage
------------

**Packet Capture Operations:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # List available packet captures
   captures = fgt.api.service.sniffer.list.get()
   
   # Start a new capture (properties are lazy-loaded)
   result = fgt.api.service.sniffer.start.post(
       host='192.168.1.100',
       port=443,
       interface='port1'
   )
   
   # Or using payload_dict
   result = fgt.api.service.sniffer.start.post(payload_dict={
       'host': '192.168.1.100',
       'port': 443,
       'interface': 'port1'
   })
   
   # Get capture metadata
   meta = fgt.api.service.sniffer.meta.get(mkey='capture_id')
   
   # Stop capture
   result = fgt.api.service.sniffer.stop.post(mkey='capture_id')
   
   # Download PCAP file
   pcap_data = fgt.api.service.sniffer.download.get(mkey='capture_id')
   
   # Delete capture
   result = fgt.api.service.sniffer.delete.post(mkey='capture_id')

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
