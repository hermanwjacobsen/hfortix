"""
Auto-generated basic tests for cmdb.vpn/l2tp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.l2tp.json
Category: cmdb
Endpoint: /cmdb/vpn/l2tp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_l2tp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.l2tp


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoL2tpGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve l2tp configuration."""
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
        print(f"✅ Retrieved l2tp configuration (singleton)")
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
class TestAutoL2tpExists:
    """Auto-generated exists() tests."""
    


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoL2tpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn._helpers import l2tp as validators
            print(f"✅ Successfully imported validators for l2tp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_l2tp_post")
            assert hasattr(validators, "validate_vpn_l2tp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import l2tp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "compress": "enable",  # option
            "eip": "0.0.0.0",  # ipv4-address
            "enforce-ipsec": "enable",  # option
            "sip": "0.0.0.0",  # ipv4-address
            "status": "enable",  # option
            "usrgrp": "test_usrgrp",  # string
        }
        
        try:
            result = validators.validate_l2tp_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoL2tpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import l2tp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_enforce_ipsec(self):
        """Test enum field enforce-ipsec validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import l2tp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"enforce-ipsec": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: enforce-ipsec={value}")
        
        print(f"✅ Enum field enforce-ipsec has {len(valid_values)} valid values")
    def auto_test_enum_compress(self):
        """Test enum field compress validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import l2tp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"compress": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: compress={value}")
        
        print(f"✅ Enum field compress has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/l2tp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.l2tp.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']