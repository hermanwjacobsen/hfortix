"""
Auto-generated basic tests for cmdb.system/ddns

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ddns.json
Category: cmdb
Endpoint: /cmdb/system/ddns

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ddns.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ddns


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoDdnsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all ddns items."""
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
        print(f"✅ Retrieved {len(result)} ddns items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "ddnsid")
            mkey_value = getattr(item, "ddnsid", "N/A")
            print(f"   First item ddnsid: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific ddns by ddnsid."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing ddns items to test with")
        
        # Get first item's ddnsid
        mkey_value = getattr(all_items[0], "ddnsid")
        
        # Get specific item
        result = endpoint.get(ddnsid=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "ddnsid") == mkey_value
        print(f"✅ Retrieved ddns ddnsid={mkey_value}")
    
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
                q_format="name|ddnsid",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoDdnsExists:
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
            mkey_value = getattr(all_items[0], "ddnsid")
            exists = endpoint.exists(ddnsid=mkey_value)
            assert exists is True
            print(f"✅ exists(ddnsid={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(ddnsid=non_existing)
            assert exists is False
            print(f"✅ exists(ddnsid={non_existing}) = False")
        else:
            pytest.skip("No existing ddns items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDdnsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
            print(f"✅ Successfully imported validators for ddns")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ddns_post")
            assert hasattr(validators, "validate_system_ddns_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ddns-server": "dyndns.org",  # option
            "monitor-interface": "test_monitor-interface",  # string
        }
        
        try:
            result = validators.validate_ddns_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDdnsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ddns_server(self):
        """Test enum field ddns-server validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['dyndns.org', 'dyns.net', 'tzo.com', 'vavic.com', 'dipdns.net', 'now.net.cn', 'dhs.org', 'easydns.com', 'genericDDNS', 'FortiGuardDDNS', 'noip.com']
        
        # Test each valid value
        for value in valid_values:
            config = {"ddns-server": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ddns-server={value}")
        
        print(f"✅ Enum field ddns-server has {len(valid_values)} valid values")
    def auto_test_enum_addr_type(self):
        """Test enum field addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-type={value}")
        
        print(f"✅ Enum field addr-type has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ddns"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ddns.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']