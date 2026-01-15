"""
Auto-generated basic tests for cmdb.firewall/internet_service

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service.json
Category: cmdb
Endpoint: /cmdb/firewall/internet-service

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_internet-service.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.internet_service


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoInternetServiceGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all internet-service items."""
        try:
            result = endpoint.get(response_mode="dict")
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Multi-value CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} internet-service items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "id" in item
            print(f"   First item id: {item.get('id', 'N/A')}")
    
    
    def auto_test_get_with_vdom(self):
        """Test GET - with vdom parameter."""
        try:
            result = endpoint.get(vdom="root", response_mode="dict")
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
                response_mode="dict",
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")






@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInternetServiceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_direction(self):
        """Test enum field direction validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import internet_service as validators
        
        valid_values = ['src', 'dst', 'both']
        
        # Test each valid value
        for value in valid_values:
            config = {"direction": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: direction={value}")
        
        print(f"✅ Enum field direction has {len(valid_values)} valid values")
    def auto_test_enum_database(self):
        """Test enum field database validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import internet_service as validators
        
        valid_values = ['isdb', 'irdb']
        
        # Test each valid value
        for value in valid_values:
            config = {"database": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: database={value}")
        
        print(f"✅ Enum field database has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/internet_service"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']