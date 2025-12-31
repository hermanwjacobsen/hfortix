Report
======

Configuration endpoint for sdwan/link_monitor_metrics.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.sdwan.link_monitor_metrics

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.sdwan.link_monitor_metrics.post(
       agent_ip='value',  # optional
       application_name='value',  # optional
       application_id='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       agent_ip=None,
       application_name=None,
       application_id=None,
       latency=None,
       jitter=None,
       packet_loss=None,
       ntt=None,
       srt=None,
       application_error=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Report the application-level performance metrics collected by other

