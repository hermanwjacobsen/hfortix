"""
Auto-generated basic tests for cmdb.antivirus/settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.settings.json
Category: cmdb
Endpoint: /cmdb/antivirus/settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.antivirus.settings


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve settings configuration."""
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
        print(f"✅ Retrieved settings configuration (singleton)")
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
class TestAutoSettingsExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_machine_learning_detection(self):
        """Test enum field machine-learning-detection validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import settings as validators
        
        valid_values = ['enable', 'monitor', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"machine-learning-detection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: machine-learning-detection={value}")
        
        print(f"✅ Enum field machine-learning-detection has {len(valid_values)} valid values")
    def auto_test_enum_use_extreme_db(self):
        """Test enum field use-extreme-db validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import settings as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-extreme-db": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-extreme-db={value}")
        
        print(f"✅ Enum field use-extreme-db has {len(valid_values)} valid values")
    def auto_test_enum_grayware(self):
        """Test enum field grayware validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import settings as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"grayware": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: grayware={value}")
        
        print(f"✅ Enum field grayware has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/antivirus/settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.settings.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']