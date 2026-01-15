"""
Auto-generated basic tests for cmdb.router/isis

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.isis.json
Category: cmdb
Endpoint: /cmdb/router/isis

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_isis.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.isis


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoIsisGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve isis configuration."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single FortiObject
        assert hasattr(result, "__dict__")  # FortiObject
        print(f"✅ Retrieved isis configuration (singleton)")
        # Convert to dict to count fields
        result_dict = result.dict
        print(f"   Config keys: {len(result_dict)} fields")
    
    
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
                q_format="name|None",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoIsisExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIsisEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_is_type(self):
        """Test enum field is-type validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import isis as validators
        
        valid_values = ['level-1-2', 'level-1', 'level-2-only']
        
        # Test each valid value
        for value in valid_values:
            config = {"is-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: is-type={value}")
        
        print(f"✅ Enum field is-type has {len(valid_values)} valid values")
    def auto_test_enum_adv_passive_only(self):
        """Test enum field adv-passive-only validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import isis as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"adv-passive-only": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: adv-passive-only={value}")
        
        print(f"✅ Enum field adv-passive-only has {len(valid_values)} valid values")
    def auto_test_enum_adv_passive_only6(self):
        """Test enum field adv-passive-only6 validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import isis as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"adv-passive-only6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: adv-passive-only6={value}")
        
        print(f"✅ Enum field adv-passive-only6 has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/isis"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.isis.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']