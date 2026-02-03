HFortix Documentation
=====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   packages
   examples

Welcome to HFortix
------------------

**HFortix** is the complete suite of Python SDKs for Fortinet automation. This meta-package installs all HFortix components.

What's Included
---------------

When you install ``hfortix``, you get:

* **hfortix-fortios** - Complete FortiOS/FortiGate API client
* **hfortix-core** - Foundation libraries and infrastructure

Features
--------

* 🎯 Complete API Coverage - 1,348 FortiOS endpoints
* 💪 Fully Typed - Complete type hints and IDE support
* ⚡ Modern & Fast - Async/await, HTTP/2, connection pooling
* 🛡️ Production Ready - Comprehensive error handling
* 🔄 Simplified Syntax - Auto-conversion to FortiOS format
* 📦 Batch Transactions - Atomic configuration changes

Installation
------------

.. code-block:: bash

   pip install hfortix

Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect to FortiGate
   with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
       # Get system status
       status = fgt.api.monitor.system.status.get()
       print(f"Hostname: {status['hostname']}")
       
       # Create firewall address
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32"
       )

Component Documentation
-----------------------

* `HFortix-FortiOS Documentation <https://hfortix-fortios.readthedocs.io/>`_
* `HFortix-Core Documentation <https://hfortix-core.readthedocs.io/>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
