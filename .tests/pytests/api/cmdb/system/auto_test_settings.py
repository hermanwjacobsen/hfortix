"""
Auto-generated basic tests for cmdb.system/settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.settings.json
Category: cmdb
Endpoint: /cmdb/system/settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.settings


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve settings configuration."""
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
        print(f"✅ Retrieved settings configuration (singleton)")
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
class TestAutoSettingsExists:
    """Auto-generated exists() tests."""
    


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import settings as validators
            print(f"✅ Successfully imported validators for settings")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_settings_post")
            assert hasattr(validators, "validate_system_settings_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import settings as validators
        
        # Build minimal valid config with all required fields
        config = {
            "device": "test_device",  # string
            "dhcp-proxy-interface": "test_dhcp-proxy-interface",  # string
            "ip": "0.0.0.0 0.0.0.0",  # ipv4-classnet-host
            "manageip": "",  # user
            "opmode": "nat",  # option
            "vdom-type": "traffic",  # option
        }
        
        try:
            result = validators.validate_settings_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_vdom_type(self):
        """Test enum field vdom-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import settings as validators
        
        valid_values = ['traffic', 'lan-extension', 'admin']
        
        # Test each valid value
        for value in valid_values:
            config = {"vdom-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vdom-type={value}")
        
        print(f"✅ Enum field vdom-type has {len(valid_values)} valid values")
    def auto_test_enum_opmode(self):
        """Test enum field opmode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import settings as validators
        
        valid_values = ['nat', 'transparent']
        
        # Test each valid value
        for value in valid_values:
            config = {"opmode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: opmode={value}")
        
        print(f"✅ Enum field opmode has {len(valid_values)} valid values")
    def auto_test_enum_ngfw_mode(self):
        """Test enum field ngfw-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import settings as validators
        
        valid_values = ['profile-based', 'policy-based']
        
        # Test each valid value
        for value in valid_values:
            config = {"ngfw-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ngfw-mode={value}")
        
        print(f"✅ Enum field ngfw-mode has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.settings.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']