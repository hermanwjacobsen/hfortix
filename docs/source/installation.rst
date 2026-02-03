Installation
============

Install HFortix
---------------

The easiest way to get started is to install the complete suite:

.. code-block:: bash

   pip install hfortix

This installs all HFortix components:

* ``hfortix-core`` - Core infrastructure
* ``hfortix-fortios`` - FortiOS/FortiGate API client

Individual Packages
-------------------

You can also install packages individually:

FortiOS Client Only
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install hfortix-fortios

This automatically installs ``hfortix-core`` as a dependency.

Core Infrastructure Only
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install hfortix-core

Use this if you're building custom Fortinet API clients.

Requirements
------------

* Python 3.10 or higher
* httpx with HTTP/2 support
* typing-extensions for enhanced type hints

Virtual Environment
-------------------

We recommend using a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install hfortix

Verify Installation
-------------------

.. code-block:: bash

   python -c "from hfortix_fortios import FortiOS; print('✅ HFortix installed successfully')"
