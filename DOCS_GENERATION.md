# Documentation Generation

## Overview

The API reference documentation is now **auto-generated from the actual Python code** in `packages/fortios/hfortix_fortios/api/v2/`. This ensures documentation accuracy and consistency with the implementation.

## Why Code-Generated Documentation?

### Previous Issues (Manual Documentation)
1. **Wrong Examples**: Showed `json={'parameter': 'value'}` instead of actual parameters
2. **Incorrect Paths**: Mixed up hierarchy like `api.cmdb.alertemail` vs `api.alertemail`
3. **Outdated**: Manual docs quickly became out of sync with code changes
4. **Inconsistent**: Different endpoints documented differently

### Current Approach (Auto-Generated)
1. **Accurate**: Examples show actual method signatures from code
2. **Consistent**: All endpoints documented the same way
3. **Maintainable**: Update code → regenerate docs → always in sync
4. **Complete**: Covers all 857+ endpoints automatically

## How It Works

### API Structure

The FortiOS API has this structure:

```text
fgt.api.{category}.{endpoint_path}.{method}()
         ^^^^^^^^   ^^^^^^^^^^^^^^^  ^^^^^^^^
         cmdb/      firewall/        get/post/
         monitor/   address          put/delete
         log/
         service/
```

**Important**: The `category` (cmdb/monitor/log/service) is an **API category**, not part of the endpoint path.

Examples:
- `fgt.api.cmdb.firewall.address.get()` → API: `/api/v2/cmdb/firewall/address`
- `fgt.api.cmdb.alertemail.setting.put()` → API: `/api/v2/cmdb/alertemail/setting`
- `fgt.api.service.sniffer.sniffer.post()` → API: `/api/v2/service/sniffer/sniffer`

### Method Signatures

All methods use **explicit parameters**, NOT `json={...}`:

```python
# ✅ CORRECT - Explicit parameters
result = fgt.api.cmdb.firewall.address.post(
    name='test-host',
    subnet='192.0.2.100/32',
    comment='Example host'
)

# ❌ WRONG - Never use json=
result = fgt.api.cmdb.firewall.address.post(json={
    'name': 'test-host',
    'subnet': '192.0.2.100/32'
})
```

The Python methods handle parameter transformation internally (converting Python naming like `start_ip` to API naming like `start-ip`).

## Generating Documentation

### Run the Generator

```bash
cd /app/dev/classes/fortinet
python3 generate_docs.py
```

This will:
1. Scan all Python files in `packages/fortios/hfortix_fortios/api/v2/`
2. Extract method signatures, parameters, and docstrings using AST parsing
3. Generate RST files in `docs/source/fortios/api-reference/`
4. Create proper examples with actual parameters
5. Build complete method reference with signatures

### What Gets Generated

For each endpoint (e.g., `firewall/address`), generates:

```rst
Address
=======

Configuration endpoint for firewall/address.

Python Attribute
----------------
fgt.api.cmdb.firewall.address

Available Methods
-----------------
- get() - GET operation
- post() - POST operation
- put() - PUT operation
- delete() - DELETE operation

Examples
--------
# Actual code examples with real parameters

Method Reference
----------------
# Full method signatures with all parameters
```

### Output Statistics

Current generation produces:
- **857 endpoints** documented
- Across 4 categories: cmdb (672), monitor (124), log (58), service (3)
- All with consistent, accurate examples

## File Locations

```text
generate_docs.py                                    # Generator script
packages/fortios/hfortix_fortios/api/v2/           # Source code (input)
  ├── cmdb/
  ├── monitor/
  ├── log/
  └── service/
docs/source/fortios/api-reference/                 # Generated docs (output)
  ├── cmdb/
  ├── monitor/
  ├── log/
  └── service/
```

## Maintaining Documentation

### When to Regenerate

Regenerate documentation when:
1. Adding new endpoints
2. Changing method signatures
3. Updating parameter names or types
4. Adding/removing methods
5. Updating docstrings

### Workflow

1. **Update the Python code** in `packages/fortios/hfortix_fortios/api/v2/`
2. **Run generator**: `python3 generate_docs.py`
3. **Build docs**: `cd docs && make html`
4. **Review**: Check `docs/build/html/`
5. **Commit both**: Code changes + generated RST files

### Customization

To customize generated documentation, edit `generate_docs.py`:
- `generate_method_example()`: Modify example code generation
- `generate_rst_file()`: Change RST structure/sections
- `parse_function_signature()`: Adjust parameter extraction
- `EndpointInfo`: Add more metadata to collect

## Benefits

### For Users
- ✅ See actual method signatures, not generic placeholders
- ✅ Copy-paste examples that actually work
- ✅ Understand real parameter names and types
- ✅ Navigate consistent documentation structure

### For Maintainers
- ✅ Single source of truth (the code)
- ✅ No manual doc updates needed
- ✅ Catch documentation bugs early
- ✅ Scale to hundreds of endpoints easily

## Example Comparison

### Before (Manual)
```python
# Get specific item by name
item = fgt.api.cmdb.firewall.address.get(mkey='item-name')

# Update existing item
result = fgt.api.cmdb.firewall.DoS_policy.put(
    mkey='item-name',
    json={'parameter': 'value'}  # ❌ WRONG!
)
```

### After (Auto-Generated)
```python
# Get specific item by name
item = fgt.api.cmdb.firewall.address.get(name='item-name')

# Update existing item
result = fgt.api.cmdb.firewall.dos_policy.put(
    name='updated-value',
    policyid='updated-value',
    interface='updated-value',
    status='updated-value',
)
```

## See Also

- `packages/fortios/hfortix_fortios/client.py` - Main FortiOS client
- `docs/fortios/ENDPOINT_METHODS.md` - Endpoint methods guide
- `docs/fortios/README.md` - FortiOS documentation overview
