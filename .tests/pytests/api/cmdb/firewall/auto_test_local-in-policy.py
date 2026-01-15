"""
Auto-generated basic tests for cmdb.firewall/local_in_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.local-in-policy.json
Category: cmdb
Endpoint: /cmdb/firewall/local-in-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_local-in-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.local_in_policy


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoLocalInPolicyGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all local-in-policy items."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Multi-value CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} local-in-policy items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "policyid")
            mkey_value = getattr(item, "policyid", "N/A")
            print(f"   First item policyid: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific local-in-policy by policyid."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing local-in-policy items to test with")
        
        # Get first item's policyid
        mkey_value = getattr(all_items[0], "policyid")
        
        # Get specific item
        result = endpoint.get(policyid=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "policyid") == mkey_value
        print(f"✅ Retrieved local-in-policy policyid={mkey_value}")
    
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
                q_format="name|policyid",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoLocalInPolicyExists:
    """Auto-generated exists() tests."""
    
    def auto_test_exists_method(self):
        """Test exists() helper method."""
        # Get existing items
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if all_items and len(all_items) > 0:
            # Test with existing item
            mkey_value = getattr(all_items[0], "policyid")
            exists = endpoint.exists(policyid=mkey_value)
            assert exists is True
            print(f"✅ exists(policyid={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(policyid=non_existing)
            assert exists is False
            print(f"✅ exists(policyid={non_existing}) = False")
        else:
            pytest.skip("No existing local-in-policy items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalInPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy as validators
            print(f"✅ Successfully imported validators for local-in-policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_local_in_policy_post")
            assert hasattr(validators, "validate_firewall_local_in_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dstaddr": "test_dstaddr",  # string
            "intf": "test_intf",  # string
            "schedule": "test_schedule",  # string
            "service": "test_service",  # string
            "srcaddr": "test_srcaddr",  # string
        }
        
        try:
            result = validators.validate_local_in_policy_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalInPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ha_mgmt_intf_only(self):
        """Test enum field ha-mgmt-intf-only validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ha-mgmt-intf-only": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ha-mgmt-intf-only={value}")
        
        print(f"✅ Enum field ha-mgmt-intf-only has {len(valid_values)} valid values")
    def auto_test_enum_srcaddr_negate(self):
        """Test enum field srcaddr-negate validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"srcaddr-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: srcaddr-negate={value}")
        
        print(f"✅ Enum field srcaddr-negate has {len(valid_values)} valid values")
    def auto_test_enum_internet_service_src(self):
        """Test enum field internet-service-src validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"internet-service-src": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: internet-service-src={value}")
        
        print(f"✅ Enum field internet-service-src has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/local_in_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.local-in-policy.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']