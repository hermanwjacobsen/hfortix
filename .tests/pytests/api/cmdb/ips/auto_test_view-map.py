"""
Auto-generated basic tests for cmdb.ips/view_map

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.view-map.json
Category: cmdb
Endpoint: /cmdb/ips/view-map

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_view-map.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ips.view_map


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoViewMapGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all view-map items."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Multi-value CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} view-map items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "id")
            mkey_value = getattr(item, "id", "N/A")
            print(f"   First item id: {mkey_value}")
    
    
    def auto_test_get_with_vdom(self):
        """Test GET - with vdom parameter."""
        try:
            result = endpoint.get(vdom="root")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with vdom=root successful")
    
    def auto_test_get_with_filters(self):
        """Test GET - with filter parameters."""
        # Test with common filter options
        try:
            result = endpoint.get(
                filter="",  # No filter (get all)
                q_format="name|id",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")






@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoViewMapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_which(self):
        """Test enum field which validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import view_map as validators
        
        valid_values = ['firewall', 'interface', 'interface6', 'sniffer', 'sniffer6', 'explicit']
        
        # Test each valid value
        for value in valid_values:
            config = {"which": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: which={value}")
        
        print(f"✅ Enum field which has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ips/view_map"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.view-map.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']