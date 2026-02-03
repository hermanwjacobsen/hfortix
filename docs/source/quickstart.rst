Quickstart
==========

Connect to FortiGate
--------------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect using context manager (recommended)
   with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
       status = fgt.api.monitor.system.status.get()
       print(f"Connected to {status['hostname']}")

Basic Operations
----------------

Create Firewall Address
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fgt.api.cmdb.firewall.address.post(
       name="web-server",
       subnet="10.0.1.100/32",
       comment="Production web server"
   )

Query with Filters
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get addresses in a specific subnet
   addresses = fgt.api.cmdb.firewall.address.get(
       filter="subnet==10.0.0.0/8"
   )

Create Firewall Policy
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fgt.api.cmdb.firewall.policy.post(
       name="Allow-Web",
       srcintf=["internal"],
       dstintf=["wan1"],
       srcaddr=["all"],
       dstaddr=["web-server"],
       service=["HTTP", "HTTPS"],
       action="accept"
   )

Batch Operations
----------------

Use transactions for atomic changes:

.. code-block:: python

   with fgt.transaction() as txn:
       txn.add(fgt.api.cmdb.firewall.address.post, 
               name="server1", subnet="10.0.1.1/32")
       txn.add(fgt.api.cmdb.firewall.address.post, 
               name="server2", subnet="10.0.1.2/32")
       # Both created or both rolled back

Async Support
-------------

.. code-block:: python

   from hfortix_fortios import AsyncFortiOS

   async with AsyncFortiOS(host="192.168.1.99", token="token") as fgt:
       status = await fgt.api.monitor.system.status.get()
       addresses = await fgt.api.cmdb.firewall.address.get()

Next Steps
----------

* Read the `FortiOS API documentation <https://hfortix-fortios.readthedocs.io/>`_
* See :doc:`examples` for more use cases
* Check :doc:`packages` for package comparison
