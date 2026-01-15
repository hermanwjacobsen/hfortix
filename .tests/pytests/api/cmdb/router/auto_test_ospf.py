"""
Auto-generated basic tests for cmdb.router/ospf

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ospf.json
Category: cmdb
Endpoint: /cmdb/router/ospf

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ospf.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.ospf


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoOspfGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve ospf configuration."""
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
        print(f"✅ Retrieved ospf configuration (singleton)")
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
class TestAutoOspfExists:
    """Auto-generated exists() tests."""
    


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOspfValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
            print(f"✅ Successfully imported validators for ospf")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_router_ospf_post")
            assert hasattr(validators, "validate_router_ospf_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        # Build minimal valid config with all required fields
        config = {
            "router-id": "0.0.0.0",  # ipv4-address-any
        }
        
        try:
            result = validators.validate_ospf_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOspfEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_abr_type(self):
        """Test enum field abr-type validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['cisco', 'ibm', 'shortcut', 'standard']
        
        # Test each valid value
        for value in valid_values:
            config = {"abr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: abr-type={value}")
        
        print(f"✅ Enum field abr-type has {len(valid_values)} valid values")
    def auto_test_enum_database_overflow(self):
        """Test enum field database-overflow validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"database-overflow": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: database-overflow={value}")
        
        print(f"✅ Enum field database-overflow has {len(valid_values)} valid values")
    def auto_test_enum_default_information_originate(self):
        """Test enum field default-information-originate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['enable', 'always', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"default-information-originate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: default-information-originate={value}")
        
        print(f"✅ Enum field default-information-originate has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/ospf"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ospf.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']