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
   
   # Step 1: Configure a packet capture via CMDB (firewall.sniffer)
   config = fgt.api.cmdb.firewall.sniffer.post(json={
       'name': 'my-capture',
       'interface': 'port1',
       'host': '192.168.1.100',
       'port': '443',
       'protocol': '6',  # TCP
       'max-packet-count': 1000
   })
   
   # Step 2: Start the packet capture
   result = fgt.api.service.sniffer.start.post(mkey='my-capture')
   
   # Step 3: List all packet captures and their status
   captures = fgt.api.service.sniffer.list.get()
   
   # Step 4: Get capture metadata
   meta = fgt.api.service.sniffer.meta.get()
   
   # Step 5: Stop the capture
   result = fgt.api.service.sniffer.stop.post(mkey='my-capture')
   
   # Step 6: Download PCAP file
   pcap_data = fgt.api.service.sniffer.download.post(mkey='my-capture')
   
   # Step 7: Delete the capture
   result = fgt.api.service.sniffer.delete.post(mkey='my-capture')

**Note**: Packet captures must be configured via CMDB (``firewall.sniffer`` or ``firewall.on_demand_sniffer``) 
before they can be started using the service API.

See Also
--------

- :doc:`/fortios/api-reference/service/index` - Service API overview
