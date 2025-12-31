# Authentication

Learn how to set up API authentication for FortiOS devices.

## API Token Authentication (Recommended)

FortiOS 6.0+ supports token-based authentication, which is the recommended method for API access.

### Creating an API Token

1. Log in to your FortiGate web interface
2. Navigate to **System > Administrators**
3. Click **Create New > REST API Admin**
4. Configure the API user:
   - **Username**: Choose a descriptive name (e.g., `api-admin`)
   - **Profile**: Select an administrator profile (e.g., `super_admin` for full access)
   - **CORS Allow Origin**: Leave blank or specify allowed origins
   - **Trusted Hosts**: Restrict to specific IP addresses for security (recommended)
   - Click **OK**
5. **Copy the API token immediately** - it will only be shown once!

```{important}
The API token is displayed only once when created. If you lose it, you must create a new one.
Store it securely (e.g., in a password manager or environment variable).
```

### Token Requirements

API tokens must meet these requirements:

- Minimum 25 characters long
- Contains only letters, numbers, hyphens, and underscores
- No spaces or special characters

HFortix validates tokens on initialization and provides helpful error messages for common issues:

```python
from hfortix import FortiOS

# ❌ Token too short
fgt = FortiOS(host='192.168.1.99', token='abc123')
# Raises: ValueError: API token must be at least 25 characters

# ❌ Token with spaces (common copy-paste error)
fgt = FortiOS(host='192.168.1.99', token='my token with spaces')
# Raises: ValueError: API token contains invalid characters

# ❌ Placeholder token
fgt = FortiOS(host='192.168.1.99', token='your_token_here')
# Raises: ValueError: API token appears to be a placeholder

# ✅ Valid token
fgt = FortiOS(host='192.168.1.99', token='abcdef1234567890abcdef1234567890')
```

### Using API Tokens

```python
from hfortix import FortiOS

# Basic usage
fgt = FortiOS(
    host='fortigate.example.com',
    token='your-25-plus-character-api-token'
)

# With SSL verification (production)
fgt = FortiOS(
    host='fortigate.example.com',
    token='your-api-token',
    verify=True  # Verify SSL certificate
)

# Without SSL verification (development/self-signed certs)
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False  # Disable SSL verification
)
```

## Environment Variables (Best Practice)

Never hardcode tokens in your code. Use environment variables instead:

### Using python-dotenv

1. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file:
   ```bash
   FORTIGATE_HOST=192.168.1.99
   FORTIGATE_TOKEN=your-actual-api-token-here
   FORTIGATE_VERIFY_SSL=False
   ```

3. Add `.env` to your `.gitignore`:
   ```bash
   echo ".env" >> .gitignore
   ```

4. Use in your code:
   ```python
   import os
   from dotenv import load_dotenv
   from hfortix import FortiOS

   # Load environment variables
   load_dotenv()

   # Initialize client from environment
   fgt = FortiOS(
       host=os.getenv('FORTIGATE_HOST'),
       token=os.getenv('FORTIGATE_TOKEN'),
       verify=os.getenv('FORTIGATE_VERIFY_SSL', 'True').lower() == 'true'
   )
   ```

### Using OS Environment Variables

```bash
# Set environment variables
export FORTIGATE_HOST=192.168.1.99
export FORTIGATE_TOKEN=your-api-token
export FORTIGATE_VERIFY_SSL=false

# Run your script
python your_script.py
```

```python
import os
from hfortix import FortiOS

fgt = FortiOS(
    host=os.getenv('FORTIGATE_HOST'),
    token=os.getenv('FORTIGATE_TOKEN'),
    verify=os.getenv('FORTIGATE_VERIFY_SSL', 'true').lower() == 'true'
)
```

## Username/Password Authentication (Legacy)

```{warning}
Username/password authentication is deprecated in FortiOS 7.6.x and later.
Use API tokens instead for better security and compatibility.
```

For FortiOS ≤7.4.x only:

```python
from hfortix import FortiOS

fgt = FortiOS(
    host='192.168.1.99',
    username='admin',
    password='your-password',
    verify=False
)
```

## SSL Certificate Verification

### Production Environments

Always use `verify=True` in production with valid SSL certificates:

```python
fgt = FortiOS(
    host='fortigate.company.com',
    token='your-api-token',
    verify=True  # Verify SSL certificates
)
```

### Custom Certificate Authority

If using a custom CA:

```python
fgt = FortiOS(
    host='fortigate.company.com',
    token='your-api-token',
    verify='/path/to/ca-bundle.crt'  # Path to CA certificate
)
```

### Development/Testing with Self-Signed Certificates

Only use `verify=False` in development/testing environments:

```python
import urllib3

# Suppress SSL warnings (optional)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False  # Disable SSL verification
)
```

```{danger}
Never use `verify=False` in production! This disables SSL certificate validation
and makes your connection vulnerable to man-in-the-middle attacks.
```

## Administrator Profiles

When creating API users, select an appropriate administrator profile:

- **super_admin**: Full access to all features (use with caution)
- **prof_admin**: Read/write access to most features
- **Read-Only**: View-only access (safe for monitoring scripts)
- **Custom Profile**: Create a custom profile with specific permissions

### Example: Creating a Read-Only API User

For monitoring scripts that only need read access:

1. Create a custom administrator profile:
   - Navigate to **System > Admin Profiles**
   - Create a new profile with read-only permissions
2. Create an API user with this profile
3. Use the token for monitoring operations

```python
from hfortix import FortiOS

# Read-only monitoring client
fgt_monitor = FortiOS(
    host='192.168.1.99',
    token='read-only-api-token',
    verify=True
)

# Safe operations - will succeed
status = fgt_monitor.api.monitor.system.status.get()
policies = fgt_monitor.api.cmdb.firewall.policy.list()

# Write operations - will fail with permission error
# fgt_monitor.api.cmdb.firewall.address.create(...)  # PermissionError
```

## Trusted Hosts (Security Best Practice)

Restrict API access to specific IP addresses:

1. When creating the API user, set **Trusted Hosts**
2. Add your application server's IP address
3. Click the **+** to add multiple trusted hosts if needed

Example trusted hosts:
- `192.168.1.100/32` - Single IP address
- `10.0.0.0/24` - Entire subnet
- `0.0.0.0/0` - Any IP (not recommended for production)

## Testing Your Authentication

Verify your credentials work:

```python
from hfortix import FortiOS, APIError

try:
    fgt = FortiOS(
        host='192.168.1.99',
        token='your-api-token',
        verify=False
    )
    
    # Test with a simple API call
    status = fgt.api.monitor.system.status.get()
    print(f"✅ Connected to {status['hostname']}")
    print(f"   FortiOS Version: {status['version']}")
    print(f"   Serial Number: {status['serial']}")
    
except APIError as e:
    print(f"❌ Authentication failed: {e.message}")
except Exception as e:
    print(f"❌ Connection error: {e}")
```

## Next Steps

- [Quick Start Guide](quickstart.md) - Start using HFortix
- [User Guide](../user-guide/fortios-overview.md) - Comprehensive documentation
- [Security](../security.md) - Security best practices
