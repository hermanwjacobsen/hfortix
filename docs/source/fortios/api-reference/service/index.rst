Service API Reference
======================

System service operations (sniffer, security rating, etc.).

Overview
--------

The Service API provides control over FortiGate system services across 3 categories:

- :doc:`Sniffer <sniffer/index>` - Packet capture operations for network troubleshooting
- :doc:`Security Rating <security-rating/index>` - Security posture assessment and scoring
- :doc:`System <system/index>` - System service operations and management

.. toctree::
   :maxdepth: 2
   :caption: Service Categories

   sniffer/index
   security-rating/index
   system/index

Usage Examples
--------------

Packet Sniffer
^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Start packet capture
   fgt.service.sniffer.start(mkey='capture1')
   
   # Stop packet capture
   fgt.service.sniffer.stop(mkey='capture1')
   
   # Download capture file
   pcap = fgt.service.sniffer.download(mkey='capture1')

Security Rating
^^^^^^^^^^^^^^^

.. code-block:: python

   # Get security rating
   rating = fgt.service.security_rating.get()
   print(f"Security score: {rating['score']}")

See Also
--------

- :doc:`/fortios/user-guide/client` - FortiOS client reference
