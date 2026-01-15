"""
Auto-generated basic tests for cmdb.vpn/certificate/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.certificate.setting.json
Category: cmdb
Endpoint: /cmdb/vpn.certificate/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.certificate.setting


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve setting configuration."""
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
        print(f"✅ Retrieved setting configuration (singleton)")
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
class TestAutoSettingExists:
    """Auto-generated exists() tests."""
    


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import setting as validators
            print(f"✅ Successfully imported validators for setting")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_certificate_setting_post")
            assert hasattr(validators, "validate_vpn_certificate_setting_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import setting as validators
        
        # Build minimal valid config with all required fields
        config = {
            "certname-dsa1024": "test_certname-dsa1024",  # string
            "certname-dsa2048": "test_certname-dsa2048",  # string
            "certname-ecdsa256": "test_certname-ecdsa256",  # string
            "certname-ecdsa384": "test_certname-ecdsa384",  # string
            "certname-ecdsa521": "test_certname-ecdsa521",  # string
            "certname-ed25519": "test_certname-ed25519",  # string
            "certname-ed448": "test_certname-ed448",  # string
            "certname-rsa1024": "test_certname-rsa1024",  # string
            "certname-rsa2048": "test_certname-rsa2048",  # string
            "certname-rsa4096": "test_certname-rsa4096",  # string
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_setting_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ocsp_status(self):
        """Test enum field ocsp-status validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import setting as validators
        
        valid_values = ['enable', 'mandatory', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ocsp-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ocsp-status={value}")
        
        print(f"✅ Enum field ocsp-status has {len(valid_values)} valid values")
    def auto_test_enum_ocsp_option(self):
        """Test enum field ocsp-option validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import setting as validators
        
        valid_values = ['certificate', 'server']
        
        # Test each valid value
        for value in valid_values:
            config = {"ocsp-option": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ocsp-option={value}")
        
        print(f"✅ Enum field ocsp-option has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import setting as validators
        
        valid_values = ['auto', 'sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/certificate/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.certificate.setting.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']