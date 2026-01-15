from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

# Disable circuit breaker for testing by setting a very high threshold
# This allows tests to run without being blocked by protective circuit breaker
fgt: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="test",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)


try:
    addresses = fgt.api.cmdb.firewall.address.get()
    for addr in addresses:
        if addr.name == "test_address1":
            try:
                delete_response = fgt.api.cmdb.firewall.address.delete(name="test_address1")
                print(f"Deleted existing test_address1: HTTP {delete_response.http_status}")    
            except Exception:
                pass
except Exception:
    pass

create_address = fgt.api.cmdb.firewall.address.set(
    name="test_address1",
    subnet="10.0.0.0/24"
)

print(f" https status: {create_address.http_status}")


create_address = fgt.api.cmdb.firewall.address.set(
    name="test_address1",
    subnet="10.0.0.0/24",
    comment="Updated via test script"
)
print(f" https status: {create_address.http_status}")
print(f" https method: {create_address.http_method}")
print(f" https stats: {create_address.status}")


