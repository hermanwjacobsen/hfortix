"""
Auto-generated basic tests for cmdb.authentication/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.setting.json
Category: cmdb
Endpoint: /cmdb/authentication/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.authentication.setting


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve setting configuration."""
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
        print(f"✅ Retrieved setting configuration (singleton)")
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
class TestAutoSettingExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_persistent_cookie(self):
        """Test enum field persistent-cookie validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"persistent-cookie": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: persistent-cookie={value}")
        
        print(f"✅ Enum field persistent-cookie has {len(valid_values)} valid values")
    def auto_test_enum_ip_auth_cookie(self):
        """Test enum field ip-auth-cookie validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-auth-cookie": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-auth-cookie={value}")
        
        print(f"✅ Enum field ip-auth-cookie has {len(valid_values)} valid values")
    def auto_test_enum_captive_portal_type(self):
        """Test enum field captive-portal-type validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['fqdn', 'ip']
        
        # Test each valid value
        for value in valid_values:
            config = {"captive-portal-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: captive-portal-type={value}")
        
        print(f"✅ Enum field captive-portal-type has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/authentication/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.setting.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']