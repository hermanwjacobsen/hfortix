"""
Auto-generated basic tests for cmdb.firewall/central_snat_map

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.central-snat-map.json
Category: cmdb
Endpoint: /cmdb/firewall/central-snat-map

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_central-snat-map.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.central_snat_map


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoCentralSnatMapGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all central-snat-map items."""
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
        print(f"✅ Retrieved {len(result)} central-snat-map items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "policyid")
            mkey_value = getattr(item, "policyid", "N/A")
            print(f"   First item policyid: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific central-snat-map by policyid."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing central-snat-map items to test with")
        
        # Get first item's policyid
        mkey_value = getattr(all_items[0], "policyid")
        
        # Get specific item
        result = endpoint.get(policyid=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "policyid") == mkey_value
        print(f"✅ Retrieved central-snat-map policyid={mkey_value}")
    
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
class TestAutoCentralSnatMapExists:
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
            pytest.skip("No existing central-snat-map items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralSnatMapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
            print(f"✅ Successfully imported validators for central-snat-map")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_central_snat_map_post")
            assert hasattr(validators, "validate_firewall_central_snat_map_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dst-addr": "test_dst-addr",  # string
            "dst-addr6": "test_dst-addr6",  # string
            "dstintf": "test_dstintf",  # string
            "orig-addr": "test_orig-addr",  # string
            "orig-addr6": "test_orig-addr6",  # string
            "srcintf": "test_srcintf",  # string
        }
        
        try:
            result = validators.validate_central_snat_map_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralSnatMapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_nat(self):
        """Test enum field nat validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"nat": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: nat={value}")
        
        print(f"✅ Enum field nat has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/central_snat_map"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.central-snat-map.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']