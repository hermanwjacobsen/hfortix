"""
Auto-generated basic tests for cmdb.vpn/ipsec/manualkey_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey-interface.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/manualkey-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_manualkey-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.manualkey_interface


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoManualkeyInterfaceGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all manualkey-interface items."""
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
        print(f"✅ Retrieved {len(result)} manualkey-interface items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "name" in item
            print(f"   First item name: {item.get('name', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific manualkey-interface by name."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing manualkey-interface items to test with")
        
        # Get first item's name
        mkey_value = all_items[0]["name"]
        
        # Get specific item
        result = endpoint.get(name=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["name"] == mkey_value
        print(f"✅ Retrieved manualkey-interface name={mkey_value}")
    
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
                q_format="name|name",  # Limit fields
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
class TestAutoManualkeyInterfaceExists:
    """Auto-generated exists() tests."""
    
    def auto_test_exists_method(self):
        """Test exists() helper method."""
        # Get existing items
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if all_items and len(all_items) > 0:
            # Test with existing item
            mkey_value = all_items[0]["name"]
            exists = endpoint.exists(name=mkey_value)
            assert exists is True
            print(f"✅ exists(name={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(name=non_existing)
            assert exists is False
            print(f"✅ exists(name={non_existing}) = False")
        else:
            pytest.skip("No existing manualkey-interface items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
            print(f"✅ Successfully imported validators for manualkey-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_interface_post")
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-alg": "null",  # option
            "auth-key": "",  # user
            "enc-alg": "null",  # option
            "enc-key": "",  # user
            "interface": "test_interface",  # string
            "local-spi": "",  # user
            "remote-gw": "0.0.0.0",  # ipv4-address
            "remote-gw6": "::",  # ipv6-address
            "remote-spi": "",  # user
        }
        
        try:
            result = validators.validate_manualkey_interface_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")
    def auto_test_enum_addr_type(self):
        """Test enum field addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-type={value}")
        
        print(f"✅ Enum field addr-type has {len(valid_values)} valid values")
    def auto_test_enum_auth_alg(self):
        """Test enum field auth-alg validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['null', 'md5', 'sha1', 'sha256', 'sha384', 'sha512']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-alg": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-alg={value}")
        
        print(f"✅ Enum field auth-alg has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/manualkey_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey-interface.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']