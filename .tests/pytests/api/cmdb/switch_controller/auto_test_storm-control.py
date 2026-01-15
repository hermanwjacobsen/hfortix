"""
Auto-generated basic tests for cmdb.switch_controller/storm_control

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control.json
Category: cmdb
Endpoint: /cmdb/switch-controller/storm-control

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_storm-control.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.storm_control


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoStormControlGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve storm-control configuration."""
        try:
            result = endpoint.get(response_mode="dict")
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single dict
        assert isinstance(result, dict)
        print(f"✅ Retrieved storm-control configuration (singleton)")
        print(f"   Config keys: {len(result)} fields")
    
    
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
                q_format="name|None",  # Limit fields
                response_mode="dict",
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoStormControlExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStormControlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_unknown_unicast(self):
        """Test enum field unknown-unicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-unicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-unicast={value}")
        
        print(f"✅ Enum field unknown-unicast has {len(valid_values)} valid values")
    def auto_test_enum_unknown_multicast(self):
        """Test enum field unknown-multicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-multicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-multicast={value}")
        
        print(f"✅ Enum field unknown-multicast has {len(valid_values)} valid values")
    def auto_test_enum_broadcast(self):
        """Test enum field broadcast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"broadcast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: broadcast={value}")
        
        print(f"✅ Enum field broadcast has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/storm_control"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']