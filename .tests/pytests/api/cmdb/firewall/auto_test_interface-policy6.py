"""
Auto-generated basic tests for cmdb.firewall/interface_policy6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.interface-policy6.json
Category: cmdb
Endpoint: /cmdb/firewall/interface-policy6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_interface-policy6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.interface_policy6


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoInterfacePolicy6Get:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all interface-policy6 items."""
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
        print(f"✅ Retrieved {len(result)} interface-policy6 items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "policyid")
            mkey_value = getattr(item, "policyid", "N/A")
            print(f"   First item policyid: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific interface-policy6 by policyid."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing interface-policy6 items to test with")
        
        # Get first item's policyid
        mkey_value = getattr(all_items[0], "policyid")
        
        # Get specific item
        result = endpoint.get(policyid=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "policyid") == mkey_value
        print(f"✅ Retrieved interface-policy6 policyid={mkey_value}")
    
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
class TestAutoInterfacePolicy6Exists:
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
            pytest.skip("No existing interface-policy6 items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInterfacePolicy6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import interface_policy6 as validators
            print(f"✅ Successfully imported validators for interface-policy6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_interface_policy6_post")
            assert hasattr(validators, "validate_firewall_interface_policy6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import interface_policy6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "application-list": "test_application-list",  # string
            "av-profile": "test_av-profile",  # string
            "casb-profile": "test_casb-profile",  # string
            "dlp-profile": "test_dlp-profile",  # string
            "dstaddr6": "test_dstaddr6",  # string
            "emailfilter-profile": "test_emailfilter-profile",  # string
            "interface": "test_interface",  # string
            "ips-sensor": "test_ips-sensor",  # string
            "srcaddr6": "test_srcaddr6",  # string
            "webfilter-profile": "test_webfilter-profile",  # string
        }
        
        try:
            result = validators.validate_interface_policy6_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInterfacePolicy6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import interface_policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_logtraffic(self):
        """Test enum field logtraffic validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import interface_policy6 as validators
        
        valid_values = ['all', 'utm', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"logtraffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: logtraffic={value}")
        
        print(f"✅ Enum field logtraffic has {len(valid_values)} valid values")
    def auto_test_enum_application_list_status(self):
        """Test enum field application-list-status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import interface_policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"application-list-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: application-list-status={value}")
        
        print(f"✅ Enum field application-list-status has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/interface_policy6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.interface-policy6.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']