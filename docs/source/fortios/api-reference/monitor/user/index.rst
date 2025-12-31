User
====

Overview
--------

The ``monitor.user`` namespace provides configuration management for:

- :doc:`Banned <banned>` - Banned configuration endpoint.
- :doc:`Collected Email <collected_email>` - Collected Email configuration endpoint.
- :doc:`Device <device>` - Device configuration endpoint.
- :doc:`Firewall <firewall>` - Firewall configuration endpoint.
- :doc:`Fortitoken <fortitoken>` - Fortitoken configuration endpoint.
- :doc:`Fortitoken Cloud <fortitoken_cloud>` - Fortitoken Cloud configuration endpoint.
- :doc:`FSSO <fsso>` - FSSO configuration endpoint.
- :doc:`Guest <guest>` - Guest configuration endpoint.
- :doc:`Info <info>` - Info configuration endpoint.
- :doc:`Local <local>` - Local configuration endpoint.
- :doc:`Password Policy Conform <password_policy_conform>` - Password Policy Conform configuration endpoint.
- :doc:`Proxy <proxy>` - Proxy configuration endpoint.
- :doc:`Query <query>` - Query configuration endpoint.
- :doc:`Radius <radius>` - Radius configuration endpoint.
- :doc:`Scim <scim>` - Scim configuration endpoint.
- :doc:`Tacacs Plus <tacacs_plus>` - Tacacs Plus configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.user.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   banned
   collected_email
   device
   firewall
   fortitoken
   fortitoken_cloud
   fsso
   guest
   info
   local
   password_policy_conform
   proxy
   query
   radius
   scim
   tacacs_plus

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
