Ippool
======

Configure IPv4 IP pools.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ippool

Quick Examples
--------------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get all items
   items = fgt.api.cmdb.firewall.ippool.get()
   
   # Get specific item by name
   item = fgt.api.cmdb.firewall.ippool.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ippool.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ippool.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ippool.delete(mkey='item-name')


Parameters
----------

**attr** (query) - *Optional*
   Type: ``string``
   
   Attribute name that references other table

**count** (query) - *Optional*
   Type: ``integer``
   
   Maximum number of entries to return.

**skip_to_datasource** (query) - *Optional*
   Type: ``object``
   
   Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false}

**acs** (query) - *Optional*
   Type: ``integer``
   
   If true, returned result are in ascending order.

**search** (query) - *Optional*
   Type: ``string``
   
   If present, the objects will be filtered by the search value.

**scope** (query) - *Optional*
   Type: ``string``
   
   Scope [global|vdom|both*]

**datasource** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include datasource information for each linked object.

**with_meta** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include meta information about each object (type id, references, etc).

**skip** (query) - *Optional*
   Type: ``boolean``
   
   Enable to call CLI skip operator to hide skipped properties.

**format** (query) - *Optional*
   Type: ``array``
   
   List of property names to include in results, separated by | (i.e. policyid|srcintf).

**action** (query) - *Optional*
   Type: ``string``
   
   datasource: Return all applicable datasource entries for a specific attribute based on simulate data.
stats: Return CMDB aggregated statistics.
find-index: Return indexes of provided primary keys with respect to filter.
default: Return the CLI default values for this object type.
json-schema: Return the JSON Schema for this object type.
schema: Return the CLI schema for this object type.
revision: Return the CMDB revision for this object type.
transaction-list: List all configuration transaction(s).
transaction-show: Show the content of the configuration transaction by transcation ID.


**vdom** (query) - *Optional*
   Type: ``array``
   
   Specify the Virtual Domain(s) from which results are returned or changes are applied to. If this parameter is not provided, the management VDOM will be used. If the admin does not have access to the VDOM, a permission error will be returned.
The URL parameter is one of:
vdom=root (Single VDOM)
vdom=vdom1,vdom2 (Multiple VDOMs)
vdom=* (All VDOMs)


**name** (path) - **Required**
   Type: ``string``
   
   mkey

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


**start** (query) - *Optional*
   Type: ``integer``
   
   Starting entry index.

**skip_to** (query) - *Optional*
   Type: ``integer``
   
   Skip to Nth CMDB entry.

**with_contents_hash** (query) - *Optional*
   Type: ``boolean``
   
   Enable to include a checksum of each object's contents.

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

**nkey** (query) - *Optional*
   Type: ``string``
   
    If *action=clone*, use *nkey* to specify the ID for the new resource to be created.
For example, to clone `address1` to `address1_clone`, use:
__action=clone&nkey=address1_clone__
__*Note:*__ This parameter can only be used when the *action* parameter is set to *clone*.




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

- :doc:`/fortios/api-reference/cmdb/firewall/index` - Firewall overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Complete endpoint methods guide
