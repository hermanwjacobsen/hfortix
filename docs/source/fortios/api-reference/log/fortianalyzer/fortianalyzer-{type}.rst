.. _fortianalyzer_fortianalyzer_{type}:

Fortianalyzer_{Type}
====================

Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

Python Attribute
----------------

.. code-block:: python

   fgt.api.log.fortianalyzer.fortianalyzer_{type}

Quick Examples
--------------

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get()
   
   # With filters
   response = fgt.api.log.fortianalyzer.fortianalyzer_{type}.get(
       rows=100,
       start=0
   )


Parameters
----------

**mkey** (query) - *Optional*
   Type: ``integer``
   
   The checksum column from the virus log.

**type** (path) - **Required**
   Type: ``string``
   
   Type of log that can be retrieved

**mkey** (query) - *Optional*
   Type: ``integer``
   
   Archive identifier.

**type** (path) - **Required**
   Type: ``string``
   
   Type of log that can be retrieved

**mkey** (query) - *Optional*
   Type: ``integer``
   
   Archive identifier.

**type** (path) - **Required**
   Type: ``string``
   
   Type of log that can be retrieved

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**keep_session_alive** (query) - *Optional*
   Type: ``string``
   
   Keep the log session alive. Session needs to be manually aborted when this is true.

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**keep_session_alive** (query) - *Optional*
   Type: ``string``
   
   Keep the log session alive. Session needs to be manually aborted when this is true.

**subtype** (path) - **Required**
   Type: ``string``
   
   Select the subtype for the Traffic log category

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**keep_session_alive** (query) - *Optional*
   Type: ``string``
   
   Keep the log session alive. Session needs to be manually aborted when this is true.

**subtype** (path) - **Required**
   Type: ``string``
   
   Select the subtype for the Event log category

**type** (path) - **Required**
   Type: ``string``
   
   Type of log that can be retrieved

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**extra** (query) - *Optional*
   Type: ``string``
   
   Flag(s) for extra data to be included [reverse_lookup|country_id].

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**extra** (query) - *Optional*
   Type: ``string``
   
   Flag(s) for extra data to be included [reverse_lookup|country_id].

**subtype** (path) - **Required**
   Type: ``string``
   
   Select the subtype for the Traffic log category

**rows** (query) - *Optional*
   Type: ``integer``
   
   Number of rows to return.

**session_id** (query) - *Optional*
   Type: ``integer``
   
   Provide a session_id to continue getting data for that request.

**serial_no** (query) - *Optional*
   Type: ``string``
   
   Retrieve log from the specified device.

**is_ha_member** (query) - *Optional*
   Type: ``string``
   
   Is the specified device an HA member.

**filter** (query) - *Optional*
   Type: ``array``
   
   Filtering multiple key/value pairs
Operator     |   Description
==     |   Case insensitive match with pattern.
!=     |    Does not match with pattern (case insensitive).
=@     |    Pattern found in object value (case insensitive).
!@     |    ﻿Pattern not﻿ found in object value (case insensitive).
<=     |    Value must be less than or equal to ﻿pattern﻿.
<     |    Value must be less than pattern﻿.
.>=    |    Value must be greater than or equal to ﻿pattern﻿.
.>     |    Value must be greater than ﻿pattern﻿.
Logical OR using ,    |    Separate filters using commas ','
Logical AND using &   |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**extra** (query) - *Optional*
   Type: ``string``
   
   Flag(s) for extra data to be included [reverse_lookup|country_id].

**subtype** (path) - **Required**
   Type: ``string``
   
   Select the subtype for the Event log category


HTTP Methods
------------

- **GET**: Return a description of the quarantined virus file.
- **GET**: Return a list of archived items for the desired type. :type can be app-ctrl or ips
- **GET**: Download an archived file.
- **GET**: Log data for the given log type in raw format.
- **GET**: Log data for the given log type in raw format.
- **GET**: Log data for the given log type in raw format.
- **GET**: Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- **GET**: Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- **GET**: Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.


See Also
--------

- :doc:`index` - Fortianalyzer overview
- :doc:`/fortios/api-reference/log/index` - Log API reference
- :doc:`/fortios/guides/filtering` - Filtering guide
