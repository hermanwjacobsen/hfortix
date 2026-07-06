Installation
============

Install HFortix
---------------

The easiest way to get started is to install the complete suite:

.. code-block:: bash

   pip install hfortix

This installs the common HFortix components:

* ``hfortix-core`` - Core infrastructure
* ``hfortix-fortios`` - FortiOS/FortiGate API client

Optional Extras
---------------

The FortiCloud service clients are available as extras:

.. code-block:: bash

   pip install "hfortix[forticare]"   # + hfortix-forticare (asset management)
   pip install "hfortix[fortiztp]"    # + hfortix-fortiztp (zero-touch provisioning)
   pip install "hfortix[all]"         # fortios + forticare + fortiztp
   pip install "hfortix[docs]"        # Sphinx toolchain for building the docs

The FortiManager client is an alpha preview and is installed separately
(it is not an extra of the meta package):

.. code-block:: bash

   pip install hfortix-fortimanager   # 0.1.x alpha

``hfortix-fortianalyzer`` is coming soon and is not yet on PyPI.

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
