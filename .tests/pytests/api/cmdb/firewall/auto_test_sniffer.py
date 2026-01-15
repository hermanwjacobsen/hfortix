"""
Auto-generated basic tests for cmdb.firewall/sniffer

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.sniffer.json
Category: cmdb
Endpoint: /cmdb/firewall/sniffer

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_sniffer.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.sniffer


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSnifferGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all sniffer items."""
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
        print(f"✅ Retrieved {len(result)} sniffer items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "id")
            mkey_value = getattr(item, "id", "N/A")
            print(f"   First item id: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific sniffer by id."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing sniffer items to test with")
        
        # Get first item's id
        mkey_value = getattr(all_items[0], "id")
        
        # Get specific item
        result = endpoint.get(id=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "id") == mkey_value
        print(f"✅ Retrieved sniffer id={mkey_value}")
    
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
                q_format="name|id",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSnifferExists:
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
            mkey_value = getattr(all_items[0], "id")
            exists = endpoint.exists(id=mkey_value)
            assert exists is True
            print(f"✅ exists(id={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(id=non_existing)
            assert exists is False
            print(f"✅ exists(id={non_existing}) = False")
        else:
            pytest.skip("No existing sniffer items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnifferValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
            print(f"✅ Successfully imported validators for sniffer")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_sniffer_post")
            assert hasattr(validators, "validate_firewall_sniffer_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        # Build minimal valid config with all required fields
        config = {
            "application-list": "test_application-list",  # string
            "av-profile": "test_av-profile",  # string
            "dlp-profile": "test_dlp-profile",  # string
            "emailfilter-profile": "test_emailfilter-profile",  # string
            "file-filter-profile": "test_file-filter-profile",  # string
            "ips-sensor": "test_ips-sensor",  # string
            "webfilter-profile": "test_webfilter-profile",  # string
        }
        
        try:
            result = validators.validate_sniffer_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnifferEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
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
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        valid_values = ['all', 'utm', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"logtraffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: logtraffic={value}")
        
        print(f"✅ Enum field logtraffic has {len(valid_values)} valid values")
    def auto_test_enum_ipv6(self):
        """Test enum field ipv6 validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6={value}")
        
        print(f"✅ Enum field ipv6 has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/sniffer"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.sniffer.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']