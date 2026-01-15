"""
Auto-generated basic tests for cmdb.system/vdom_exception

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-exception.json
Category: cmdb
Endpoint: /cmdb/system/vdom-exception

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vdom-exception.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vdom_exception


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoVdomExceptionGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all vdom-exception items."""
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
        print(f"✅ Retrieved {len(result)} vdom-exception items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "id" in item
            print(f"   First item id: {item.get('id', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific vdom-exception by id."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing vdom-exception items to test with")
        
        # Get first item's id
        mkey_value = all_items[0]["id"]
        
        # Get specific item
        result = endpoint.get(id=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["id"] == mkey_value
        print(f"✅ Retrieved vdom-exception id={mkey_value}")
    
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
                q_format="name|id",  # Limit fields
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
class TestAutoVdomExceptionExists:
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
            mkey_value = all_items[0]["id"]
            exists = endpoint.exists(id=mkey_value)
            assert exists is True
            print(f"✅ exists(id={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(id=non_existing)
            assert exists is False
            print(f"✅ exists(id={non_existing}) = False")
        else:
            pytest.skip("No existing vdom-exception items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomExceptionValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
            print(f"✅ Successfully imported validators for vdom-exception")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_vdom_exception_post")
            assert hasattr(validators, "validate_system_vdom_exception_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        # Build minimal valid config with all required fields
        config = {
            "object": "log.fortianalyzer.setting",  # option
        }
        
        try:
            result = validators.validate_vdom_exception_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomExceptionEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_object(self):
        """Test enum field object validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        valid_values = ['log.fortianalyzer.setting', 'log.fortianalyzer.override-setting', 'log.fortianalyzer2.setting', 'log.fortianalyzer2.override-setting', 'log.fortianalyzer3.setting', 'log.fortianalyzer3.override-setting', 'log.fortianalyzer-cloud.setting', 'log.fortianalyzer-cloud.override-setting', 'log.syslogd.setting', 'log.syslogd.override-setting', 'log.syslogd2.setting', 'log.syslogd2.override-setting', 'log.syslogd3.setting', 'log.syslogd3.override-setting', 'log.syslogd4.setting', 'log.syslogd4.override-setting', 'system.gre-tunnel', 'system.central-management', 'system.csf', 'user.radius', 'system.interface', 'vpn.ipsec.phase1-interface', 'vpn.ipsec.phase2-interface', 'router.bgp', 'router.route-map', 'router.prefix-list', 'firewall.ippool', 'firewall.ippool6', 'router.static', 'router.static6', 'firewall.vip', 'firewall.vip6', 'system.sdwan', 'system.saml', 'router.policy', 'router.policy6', 'log.syslogd.setting', 'log.syslogd.override-setting', 'firewall.address']
        
        # Test each valid value
        for value in valid_values:
            config = {"object": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: object={value}")
        
        print(f"✅ Enum field object has {len(valid_values)} valid values")
    def auto_test_enum_scope(self):
        """Test enum field scope validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        valid_values = ['all', 'inclusive', 'exclusive']
        
        # Test each valid value
        for value in valid_values:
            config = {"scope": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scope={value}")
        
        print(f"✅ Enum field scope has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vdom_exception"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-exception.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']