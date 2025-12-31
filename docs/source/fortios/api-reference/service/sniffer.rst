Service Sniffer
===============

Packet capture operations for network troubleshooting.

Overview
--------

The ``service.sniffer`` category provides control over FortiGate's built-in packet sniffer for capturing and analyzing network traffic.

Endpoint
--------

.. code-block:: python

   fgt.api.service.sniffer

Methods
-------

**.start()**
   Start packet capture

   .. code-block:: python
   
      # Start capture
      fgt.api.service.sniffer.start.post(json={
          'host': '192.168.1.100',
          'port': 443,
          'interface': 'port1'
      })

**.stop()**
   Stop packet capture

   .. code-block:: python
   
      # Stop capture
      fgt.api.service.sniffer.stop.post()

**.download()**
   Download captured packets

   .. code-block:: python
   
      # Download PCAP file
      pcap_data = fgt.api.service.sniffer.download.get(mkey='capture_id')

Usage Examples
--------------

Start Packet Capture
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Start capturing traffic on port1
   fgt.api.service.sniffer.start.post(json={
       'interface': 'port1',
       'host': '192.168.1.100',  # Optional: filter by host
       'port': 443,               # Optional: filter by port
       'count': 1000              # Max packets to capture
   })

Stop and Download
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Stop the capture
   fgt.api.service.sniffer.stop.post()
   
   # Download PCAP file
   pcap_data = fgt.api.service.sniffer.download.get()
   
   # Save to file
   with open('capture.pcap', 'wb') as f:
       f.write(pcap_data)

Filter Options
--------------

**interface** (str, optional)
   Interface to capture on ('port1', 'wan1', 'any')

**host** (str, optional)
   Filter by IP address

**port** (int, optional)
   Filter by TCP/UDP port

**protocol** (str, optional)
   Filter by protocol ('tcp', 'udp', 'icmp')

**count** (int, optional)
   Maximum number of packets to capture

Common Use Cases
----------------

Debug Connectivity Issues
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Capture traffic to specific destination
   fgt.api.service.sniffer.start.post(json={
       'interface': 'wan1',
       'host': '8.8.8.8',
       'count': 100
   })

Monitor Application Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Capture HTTPS traffic
   fgt.api.service.sniffer.start.post(json={
       'interface': 'any',
       'port': 443,
       'protocol': 'tcp',
       'count': 500
   })

Troubleshoot VPN
^^^^^^^^^^^^^^^^

.. code-block:: python

   # Capture IPsec traffic
   fgt.api.service.sniffer.start.post(json={
       'interface': 'wan1',
       'protocol': 'esp',
       'count': 200
   })

Best Practices
--------------

1. **Limit capture size** - Use 'count' parameter to avoid large files
2. **Use filters** - Narrow scope with host/port/protocol filters
3. **Stop captures** - Always stop captures when done
4. **Secure transfers** - PCAP files may contain sensitive data
5. **Performance impact** - Packet capture can impact FortiGate performance

See Also
--------

- :doc:`security-rating` - Security posture assessment
- :doc:`system` - System service operations
