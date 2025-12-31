Acme
====

Configure ACME client.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.acme

Quick Examples
--------------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get all items
   items = fgt.api.cmdb.system.acme.get()
   
   # Get specific item by name
   item = fgt.api.cmdb.system.acme.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.acme.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.acme.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.acme.delete(mkey='item-name')


Parameters
----------

**datasource** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include datasource information for each linked object.

**start** (query) - *Optional*
   Type: ``integer``
   
   Starting entry index.

**count** (query) - *Optional*
   Type: ``integer``
   
   Maximum number of entries to return.

**skip_to** (query) - *Optional*
   Type: ``integer``
   
   Skip to Nth CMDB entry.

**with_meta** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include meta information about each object (type id, references, etc).

**with_contents_hash** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include a checksum of each object's contents.

**skip** (query) - *Optional*
   Type: ``boolean``
   
   Enable to call CLI skip operator to hide skipped properties.

**format** (query) - *Optional*
   Type: ``array``
   
   List of property names to include in results, separated by | (i.e. policyid|srcintf).

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
Logical OR    |    Separate filters using commas ','
Logical AND    |    Filter strings can be combined to create logical AND queries by including multiple filters in the request.
Combining AND and OR    |    You can combine AND and OR filters together to create more complex filters.


**key** (query) - *Optional*
   Type: ``string``
   
   If present, objects will be filtered on property with this name.

**pattern** (query) - *Optional*
   Type: ``string``
   
   If present, objects will be filtered on property with this value.

**scope** (query) - *Optional*
   Type: ``string``
   
   Scope [global|vdom|both*]

**exclude-default-values** (query) - *Optional*
   Type: ``boolean``
   
   Exclude properties/objects with default value

**datasource_format** (query) - *Optional*
   Type: ``object``
   
   A map of datasources to a string of attributes, separated by | (ie: policyid|srcintf). If specified, this will add the attributes listed for any linked objects.

**unfiltered_count** (query) - *Optional*
   Type: ``integer``
   
   Maximum number of unfiltered entries to interate through.

**stat-items** (query) - *Optional*
   Type: ``string``
   
   Items to count occurrence in entire response (multiple items should be separated by '|').

**primary_keys** (query) - *Optional*
   Type: ``string``
   
   The primary key to find indexes for.

**action** (query) - *Optional*
   Type: ``string``
   
   default: Return the CLI default values for entire CLI tree.
meta: Return meta data for a specific object, table, or the entire CLI tree.
json-schema: Return JSON Schema for entire CLI tree.
schema: Return schema for entire CLI tree.


**vdom** (query) - *Optional*
   Type: ``array``
   
   Specify the Virtual Domain(s) from which results are returned or changes are applied to. If this parameter is not provided, the management VDOM will be used. If the admin does not have access to the VDOM, a permission error will be returned.
The URL parameter is one of:
vdom=root (Single VDOM)
vdom=vdom1,vdom2 (Multiple VDOMs)
vdom=* (All VDOMs)


**body** (body) - **Required**
   Type: ``string``
   
   Possible parameters to go in the body for the request

**before** (query) - *Optional*
   Type: ``string``
   
   If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before.
For example, to move `object 1` to before `object 2`, use:
__action=move&before=2__
__*Note:*__ This parameter can only be used when the *action* parameter is set to *move*.


**after** (query) - *Optional*
   Type: ``string``
   
   If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after.
For example, to move `object 1` to after `object 3`, use:
__action=move&after=3__
__*Note:*__ This parameter can only be used when the *action* parameter is set to *move*.




HTTP Methods
------------

This endpoint supports the following HTTP methods:

**.get(mkey=None, \*\*params)**
   Retrieve configuration(s). If ``mkey`` is provided, returns a specific item.
   Otherwise, returns all items.

**.post(json=data)**
   Create a new configuration item.

**.put(mkey, json=data)**
   Update an existing configuration item identified by ``mkey``.

**.delete(mkey)**
   Delete a configuration item identified by ``mkey``.

See Also
--------

- :doc:`/fortios/api-reference/cmdb/system/index` - System overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Complete endpoint methods guide
