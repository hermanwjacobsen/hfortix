Service Security Rating
=======================

Security posture assessment and scoring.

Overview
--------

The ``service.security_rating`` category provides access to FortiGate's security rating feature, which assesses the overall security posture of your FortiGate configuration.

Endpoint
--------

.. code-block:: python

   fgt.api.service.security_rating

Methods
-------

**.get()**
   Get current security rating score

   .. code-block:: python
   
      # Get security rating
      rating = fgt.api.service.security_rating.get()
      print(f"Security Score: {rating['score']}")

Usage Examples
--------------

Get Security Rating
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get security rating
   rating = fgt.api.service.security_rating.get()
   
   print(f"Overall Score: {rating['score']}")
   print(f"Rating: {rating['rating']}")  # 'good', 'fair', 'poor'
   
   # Review recommendations
   for issue in rating.get('issues', []):
       print(f"Issue: {issue['description']}")
       print(f"Impact: {issue['impact']}")
       print(f"Recommendation: {issue['recommendation']}")

Response Format
---------------

.. code-block:: python

   {
       'score': 85,
       'rating': 'good',  # 'excellent', 'good', 'fair', 'poor'
       'issues': [
           {
               'category': 'security_fabric',
               'description': 'Security Fabric not configured',
               'impact': 'medium',
               'recommendation': 'Configure Security Fabric for enhanced protection'
           },
           {
               'category': 'utm',
               'description': 'Antivirus not enabled on all policies',
               'impact': 'high',
               'recommendation': 'Enable AV scanning on internet-facing policies'
           }
       ],
       'categories': {
           'firewall': 90,
           'utm': 75,
           'ips': 80,
           'vpn': 95,
           'security_fabric': 60
       }
   }

Rating Categories
-----------------

The security rating evaluates multiple areas:

**Firewall**
   Policy configuration, address objects, service objects

**UTM (Unified Threat Management)**
   Antivirus, web filtering, application control

**IPS (Intrusion Prevention)**
   IPS signatures, profiles, and coverage

**VPN**
   VPN configuration security

**Security Fabric**
   Security Fabric integration and features

**SSL Inspection**
   SSL/TLS inspection configuration

Understanding Scores
--------------------

**90-100: Excellent**
   Optimal security configuration

**75-89: Good**
   Strong security with minor improvements possible

**60-74: Fair**
   Adequate security but significant improvements recommended

**< 60: Poor**
   Critical security issues require immediate attention

Common Recommendations
----------------------

1. **Enable UTM features** - Enable AV, web filtering, IPS on policies
2. **Configure Security Fabric** - Link with FortiAnalyzer/FortiManager
3. **SSL Inspection** - Inspect encrypted traffic for threats
4. **Update signatures** - Ensure IPS/AV signatures are current
5. **Review policies** - Remove unused or overly permissive rules

Monitoring Security Rating
--------------------------

.. code-block:: python

   import schedule
   import time
   
   def check_security_rating():
       fgt = FortiOS(host='192.168.1.99', token='token')
       rating = fgt.api.service.security_rating.get()
       
       if rating['score'] < 75:
           send_alert(f"Security rating dropped to {rating['score']}")
   
   # Check daily
   schedule.every().day.at("09:00").do(check_security_rating)
   
   while True:
       schedule.run_pending()
       time.sleep(3600)

See Also
--------

- :doc:`sniffer` - Packet capture operations
- :doc:`/fortios/guides/index` - Security best practices
