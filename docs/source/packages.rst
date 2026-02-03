Package Comparison
==================

HFortix provides three packages that can be installed individually or together.

Package Overview
----------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 30 20

   * - Package
     - Purpose
     - Dependencies
     - Install When
   * - ``hfortix``
     - Meta-package
     - All packages
     - You want everything
   * - ``hfortix-fortios``
     - FortiOS API client
     - hfortix-core
     - FortiGate automation
   * - ``hfortix-core``
     - Core infrastructure
     - httpx, typing-extensions
     - Building custom clients

hfortix (Meta Package)
----------------------

The meta-package that installs everything.

**Installation:**

.. code-block:: bash

   pip install hfortix

**Use when:**

* Starting a new FortiGate automation project
* You want all available components
* Simplest installation option

hfortix-fortios
---------------

Complete FortiOS/FortiGate API client.

**Features:**

* 1,348 FortiOS 7.6.5 endpoints
* Full type hints and IDE support
* Async/await support
* Batch transactions
* Rate limiting and retry logic

**Installation:**

.. code-block:: bash

   pip install hfortix-fortios

**Use when:**

* You need FortiOS/FortiGate automation
* You want complete API coverage
* You need production-ready features

hfortix-core
------------

Foundation libraries and infrastructure.

**Features:**

* Observable HTTP client
* Event-driven monitoring
* Base abstractions and protocols
* Shared utilities

**Installation:**

.. code-block:: bash

   pip install hfortix-core

**Use when:**

* Building custom Fortinet API clients
* You need just the infrastructure
* Developing extensions to HFortix

Dependency Chain
----------------

.. code-block:: text

   hfortix (meta)
   └── hfortix-fortios
       └── hfortix-core
           └── httpx[http2]
           └── typing-extensions

Installing ``hfortix-fortios`` automatically installs ``hfortix-core``.
Installing ``hfortix`` automatically installs both component packages.
