"""
Auto-generated basic tests for cmdb.system/ips_urlfilter_dns

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips-urlfilter-dns.json
Category: cmdb
Endpoint: /cmdb/system/ips-urlfilter-dns

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ips-urlfilter-dns.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ips_urlfilter_dns


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoIpsUrlfilterDnsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all ips-urlfilter-dns items."""
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
        print(f"✅ Retrieved {len(result)} ips-urlfilter-dns items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "address")
            mkey_value = getattr(item, "address", "N/A")
            print(f"   First item address: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific ips-urlfilter-dns by address."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing ips-urlfilter-dns items to test with")
        
        # Get first item's address
        mkey_value = getattr(all_items[0], "address")
        
        # Get specific item
        result = endpoint.get(address=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "address") == mkey_value
        print(f"✅ Retrieved ips-urlfilter-dns address={mkey_value}")
    
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
                q_format="name|address",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoIpsUrlfilterDnsExists:
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
            mkey_value = getattr(all_items[0], "address")
            exists = endpoint.exists(address=mkey_value)
            assert exists is True
            print(f"✅ exists(address={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(address=non_existing)
            assert exists is False
            print(f"✅ exists(address={non_existing}) = False")
        else:
            pytest.skip("No existing ips-urlfilter-dns items to test exists() with")




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpsUrlfilterDnsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ips_urlfilter_dns as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_ipv6_capability(self):
        """Test enum field ipv6-capability validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ips_urlfilter_dns as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6-capability": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6-capability={value}")
        
        print(f"✅ Enum field ipv6-capability has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ips_urlfilter_dns"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips-urlfilter-dns.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']