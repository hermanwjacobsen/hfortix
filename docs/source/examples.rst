Examples
========

Firewall Management
-------------------

Create Address Objects
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import FortiOS

   with FortiOS(host="192.168.1.99", token="token") as fgt:
       # Single IP
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32"
       )
       
       # Subnet
       fgt.api.cmdb.firewall.address.post(
           name="office-network",
           subnet="10.0.0.0/24"
       )
       
       # FQDN
       fgt.api.cmdb.firewall.address.post(
           name="github",
           type="fqdn",
           fqdn="github.com"
       )

Create Address Groups
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fgt.api.cmdb.firewall.addrgrp.post(
       name="web-servers",
       member=["web-server", "office-network"]
   )

Create Firewall Policies
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Allow web traffic
   fgt.api.cmdb.firewall.policy.post(
       name="Allow-Web",
       srcintf=["internal"],
       dstintf=["wan1"],
       srcaddr=["all"],
       dstaddr=["web-servers"],
       service=["HTTP", "HTTPS"],
       action="accept",
       nat="enable"
   )

Monitoring
----------

System Status
~~~~~~~~~~~~~

.. code-block:: python

   status = fgt.api.monitor.system.status.get()
   print(f"Hostname: {status['hostname']}")
   print(f"Model: {status['model']}")
   print(f"Version: {status['version']}")

Interface Statistics
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   interfaces = fgt.api.monitor.system.interface.get()
   for iface in interfaces:
       print(f"{iface['name']}: {iface['status']}")

Active Sessions
~~~~~~~~~~~~~~~

.. code-block:: python

   sessions = fgt.api.monitor.firewall.session.get()
   print(f"Active sessions: {len(sessions)}")

Batch Operations
----------------

Atomic Transactions
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # All changes committed together or rolled back on error
   with fgt.transaction() as txn:
       for i in range(1, 11):
           txn.add(
               fgt.api.cmdb.firewall.address.post,
               name=f"server-{i}",
               subnet=f"10.0.1.{i}/32"
           )

Multiple Policies
~~~~~~~~~~~~~~~~~

.. code-block:: python

   with fgt.transaction() as txn:
       # Create addresses
       txn.add(fgt.api.cmdb.firewall.address.post,
               name="app-server", subnet="10.0.1.10/32")
       txn.add(fgt.api.cmdb.firewall.address.post,
               name="db-server", subnet="10.0.1.20/32")
       
       # Create policies
       txn.add(fgt.api.cmdb.firewall.policy.post,
               name="App-Access",
               srcintf=["internal"],
               dstintf=["dmz"],
               srcaddr=["all"],
               dstaddr=["app-server"],
               service=["HTTP", "HTTPS"],
               action="accept")

Async Operations
----------------

Concurrent Requests
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import AsyncFortiOS
   import asyncio

   async def get_all_info():
       async with AsyncFortiOS(host="192.168.1.99", token="token") as fgt:
           # Run concurrently
           status, addresses, policies = await asyncio.gather(
               fgt.api.monitor.system.status.get(),
               fgt.api.cmdb.firewall.address.get(),
               fgt.api.cmdb.firewall.policy.get()
           )
           return status, addresses, policies

   asyncio.run(get_all_info())

Error Handling
--------------

Graceful Failures
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import FortiOS, FortiOSError

   with FortiOS(host="192.168.1.99", token="token") as fgt:
       try:
           fgt.api.cmdb.firewall.address.post(
               name="existing-address",
               subnet="10.0.1.1/32"
           )
       except FortiOSError as e:
           if e.status_code == 424:
               print("Address already exists")
           else:
               raise

Retry Logic
~~~~~~~~~~~

.. code-block:: python

   # Built-in retry for transient failures
   fgt = FortiOS(
       host="192.168.1.99",
       token="token",
       max_retries=3,
       retry_delay=1.0
   )
