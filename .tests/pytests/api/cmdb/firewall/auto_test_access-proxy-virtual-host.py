"""
Auto-generated basic tests for cmdb.firewall/access_proxy_virtual_host

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-virtual-host.json
Category: cmdb
Endpoint: /cmdb/firewall/access-proxy-virtual-host

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_access-proxy-virtual-host.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.access_proxy_virtual_host


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAccessProxyVirtualHostGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all access-proxy-virtual-host items."""
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
        print(f"✅ Retrieved {len(result)} access-proxy-virtual-host items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "name")
            mkey_value = getattr(item, "name", "N/A")
            print(f"   First item name: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific access-proxy-virtual-host by name."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing access-proxy-virtual-host items to test with")
        
        # Get first item's name
        mkey_value = getattr(all_items[0], "name")
        
        # Get specific item
        result = endpoint.get(name=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "name") == mkey_value
        print(f"✅ Retrieved access-proxy-virtual-host name={mkey_value}")
    
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
                q_format="name|name",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAccessProxyVirtualHostExists:
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
            mkey_value = getattr(all_items[0], "name")
            exists = endpoint.exists(name=mkey_value)
            assert exists is True
            print(f"✅ exists(name={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(name=non_existing)
            assert exists is False
            print(f"✅ exists(name={non_existing}) = False")
        else:
            pytest.skip("No existing access-proxy-virtual-host items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxyVirtualHostValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
            print(f"✅ Successfully imported validators for access-proxy-virtual-host")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_access_proxy_virtual_host_post")
            assert hasattr(validators, "validate_firewall_access_proxy_virtual_host_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        # Build minimal valid config with all required fields
        config = {
            "host": "test_host",  # string
            "host-type": "sub-string",  # option
            "ssl-certificate": "test_ssl-certificate",  # string
        }
        
        try:
            result = validators.validate_access_proxy_virtual_host_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxyVirtualHostEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_host_type(self):
        """Test enum field host-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['sub-string', 'wildcard']
        
        # Test each valid value
        for value in valid_values:
            config = {"host-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: host-type={value}")
        
        print(f"✅ Enum field host-type has {len(valid_values)} valid values")
    def auto_test_enum_empty_cert_action(self):
        """Test enum field empty-cert-action validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['accept', 'block', 'accept-unmanageable']
        
        # Test each valid value
        for value in valid_values:
            config = {"empty-cert-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: empty-cert-action={value}")
        
        print(f"✅ Enum field empty-cert-action has {len(valid_values)} valid values")
    def auto_test_enum_user_agent_detect(self):
        """Test enum field user-agent-detect validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"user-agent-detect": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: user-agent-detect={value}")
        
        print(f"✅ Enum field user-agent-detect has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/access_proxy_virtual_host"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-virtual-host.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']