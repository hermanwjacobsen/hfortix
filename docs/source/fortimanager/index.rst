FortiManager Package
====================

.. warning::
   **Coming Soon** - The FortiManager package is under development and not yet available.

Python SDK for FortiManager - Fortinet's centralized management platform.

Planned Features
----------------

**Device Management**
    Manage multiple FortiGate devices from a central location.

**Policy Packages**
    Create, modify, and deploy policy packages across device groups.

**Configuration Templates**
    Build reusable configuration templates for consistent deployments.

**Multi-Device Operations**
    Perform bulk operations across managed devices.

**ADOM Support**
    Full support for Administrative Domains (ADOMs).

**Script Management**
    Create and execute CLI scripts across devices.

**Workflow Automation**
    Automate approval workflows and change management.

Target API Coverage
-------------------

When released, the FortiManager package will provide:

- Device provisioning and onboarding
- Policy package management
- Configuration templates
- ADOM operations
- Device group management
- Script execution
- Backup and restore
- Log queries
- Report generation

Expected Structure
------------------

.. code-block:: python

    from hfortix_fortimanager import FortiManager

    # Connect to FortiManager
    fmg = FortiManager(
        host="fortimanager.example.com",
        username="admin",
        password="password"
    )

    # Manage devices
    fmg.devices.list(adom="root")
    fmg.devices.add(name="FGT-01", ip="192.168.1.99")

    # Policy packages
    fmg.policy_packages.create(
        name="Standard-Policy",
        adom="root"
    )

    # Install policy
    fmg.policy_packages.install(
        package="Standard-Policy",
        targets=["FGT-01", "FGT-02"]
    )

Timeline
--------

The FortiManager package is planned for a future release. Check the `GitHub repository <https://github.com/hermanwjacobsen/hfortix>`_ for updates.

Interested in Contributing?
----------------------------

If you're interested in contributing to FortiManager support, please reach out via:

- GitHub Issues: https://github.com/hermanwjacobsen/hfortix/issues
- GitHub Discussions: https://github.com/hermanwjacobsen/hfortix/discussions

Current Recommendations
-----------------------

Until ``hfortix-fortimanager`` is available, consider:

- **FortiManager API** - Use the REST API directly
- **Ansible** - FortiManager Ansible modules for automation
- **Terraform** - FortiManager Terraform provider

Return to Main
--------------

`← Back to HFortix Documentation <../index.html>`_
