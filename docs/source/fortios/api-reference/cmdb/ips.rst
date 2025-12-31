IPS
===

Intrusion Prevention System configuration and management.

Overview
--------

The ``cmdb.ips`` category provides comprehensive configuration for FortiGate's Intrusion Prevention System (IPS), including:

- **IPS Sensors** - Detection profiles with signatures and filters
- **Custom Signatures** - Custom attack definitions
- **Global Settings** - IPS engine configuration
- **Decoders** - Protocol decoders for deep packet inspection

Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ips

Available Endpoints
-------------------

**sensor**
   IPS sensor profiles with signature filtering and actions
   
   .. code-block:: python
   
      # List all IPS sensors
      sensors = fgt.api.cmdb.ips.sensor.get()
      
      # Get specific sensor
      sensor = fgt.api.cmdb.ips.sensor.get(mkey='default')

**custom**
   Custom IPS signatures for organization-specific threats
   
   .. code-block:: python
   
      # List custom signatures
      custom = fgt.api.cmdb.ips.custom.get()

**global**
   Global IPS engine settings and configuration
   
   .. code-block:: python
   
      # Get global IPS settings
      settings = fgt.api.cmdb.ips.global.get()

**decoder**
   Protocol decoders for deep packet inspection
   
   .. code-block:: python
   
      # List IPS decoders
      decoders = fgt.api.cmdb.ips.decoder.get()

Common Operations
-----------------

Create IPS Sensor
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new IPS sensor
   sensor = fgt.api.cmdb.ips.sensor.post(json={
       'name': 'strict-ips',
       'comment': 'Strict IPS protection for DMZ',
       'entries': [
           {
               'id': 1,
               'severity': ['critical', 'high'],
               'action': 'block',
               'log': 'enable'
           }
       ]
   })

Update IPS Sensor
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing sensor
   result = fgt.api.cmdb.ips.sensor.put(
       mkey='strict-ips',
       json={
           'comment': 'Updated IPS protection',
           'entries': [
               {
                   'id': 1,
                   'severity': ['critical', 'high', 'medium'],
                   'action': 'block',
                   'log': 'enable'
               }
           ]
       }
   )

Get IPS Sensor Details
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get specific sensor configuration
   sensor = fgt.api.cmdb.ips.sensor.get(mkey='default')
   
   print(f"Sensor: {sensor['name']}")
   print(f"Entries: {len(sensor['entries'])}")
   for entry in sensor['entries']:
       print(f"  - ID {entry['id']}: {entry['action']}")

Create Custom Signature
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Create custom IPS signature
   custom_sig = fgt.api.cmdb.ips.custom.post(json={
       'tag': 'custom-attack',
       'signature': 'F-SBID( --name "Custom.Attack"; --flow from_client; '
                    '--pattern "malicious"; --service HTTP; )',
       'comment': 'Detects custom attack pattern'
   })

Delete IPS Sensor
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete IPS sensor
   result = fgt.api.cmdb.ips.sensor.delete(mkey='old-sensor')

IPS Sensor Configuration
-------------------------

**Key Parameters:**

**name** (str, required)
   Sensor profile name

**comment** (str, optional)
   Description of the sensor

**entries** (list, required)
   List of IPS filter entries

**Entry Structure:**

- **id** - Entry ID number
- **severity** - List of severities to match: 'critical', 'high', 'medium', 'low', 'info'
- **action** - Action to take: 'block', 'monitor', 'pass', 'reset'
- **log** - Enable logging: 'enable' or 'disable'
- **log-packet** - Log full packet: 'enable' or 'disable'
- **status** - Entry status: 'enable' or 'disable'

Best Practices
--------------

1. **Start with Default Sensor** - Modify default sensor before creating custom ones
2. **Test in Monitor Mode** - Use 'monitor' action before switching to 'block'
3. **Severity-Based Filtering** - Block critical/high, monitor medium/low
4. **Enable Logging** - Always log blocked attacks for analysis
5. **Regular Updates** - Keep IPS signatures updated via FortiGuard
6. **Performance Impact** - Monitor CPU usage when enabling aggressive IPS
7. **Custom Signatures** - Test thoroughly before deploying to production

Common Use Cases
----------------

DMZ Protection
^^^^^^^^^^^^^^

.. code-block:: python

   # Strict IPS for DMZ servers
   fgt.api.cmdb.ips.sensor.post(json={
       'name': 'dmz-protection',
       'entries': [{
           'id': 1,
           'severity': ['critical', 'high'],
           'action': 'block',
           'log': 'enable',
           'log-packet': 'enable'
       }]
   })

Internal Network Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Monitor-only for internal network
   fgt.api.cmdb.ips.sensor.post(json={
       'name': 'internal-monitor',
       'entries': [{
           'id': 1,
           'severity': ['critical', 'high', 'medium'],
           'action': 'monitor',
           'log': 'enable'
       }]
   })

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`firewall` - Firewall policies (where IPS sensors are applied)
- :doc:`/fortios/user-guide/client` - FortiOS client reference
