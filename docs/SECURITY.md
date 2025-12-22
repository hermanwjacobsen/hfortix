# Security Policy and Best Practices

## Security Audit Status

**Last Audit:** December 22, 2025  
**Tool:** Bandit 1.9.2  
**Result:** ✅ **PASSED** - No security issues found

- **Total Lines Scanned:** 337,673
- **Issues Found:** 8 Low severity (all false positives in test code)
- **High/Medium Issues:** 0

---

## Reporting Security Vulnerabilities

If you discover a security vulnerability in hfortix, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Email: hermanwjacobsen@gmail.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

We will respond within 48 hours and work with you to address the issue.

---

## Security Best Practices

### 1. Credential Management

#### ✅ DO: Use Environment Variables
```python
import os
from hfortix import FortiOS

# Best practice: Load from environment
fgt = FortiOS(
    host=os.getenv('FORTIOS_HOST'),
    token=os.getenv('FORTIOS_TOKEN'),
    verify=True  # Always verify SSL in production
)
```

#### ✅ DO: Use Configuration Files (with proper permissions)
```python
import json
from hfortix import FortiOS

# Load from config file (chmod 600)
with open('/etc/hfortix/config.json') as f:
    config = json.load(f)

fgt = FortiOS(
    host=config['host'],
    token=config['token'],
    verify=True
)
```

#### ❌ DON'T: Hardcode Credentials
```python
# NEVER do this!
fgt = FortiOS(
    host="192.168.1.1",
    token="abc123xyz",  # Hardcoded token - security risk!
    verify=False
)
```

#### ❌ DON'T: Commit Credentials to Git
- Add `.env`, `config.json`, and credential files to `.gitignore`
- Never commit API tokens, passwords, or keys
- Use placeholder values in examples: `token="your_token_here"`

### 2. SSL/TLS Verification

#### ✅ DO: Always Verify SSL in Production
```python
# Production: Always verify SSL certificates
fgt = FortiOS(
    host="fortigate.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    verify=True  # ✅ Default and recommended
)
```

#### ⚠️ CAUTION: Disable SSL Verification Only for Development
```python
# Development/Testing ONLY with self-signed certificates
fgt = FortiOS(
    host="192.168.1.1",
    token=os.getenv('FORTIOS_TOKEN'),
    verify=False,  # ⚠️ Only for development!
)
```

**Why SSL Verification Matters:**
- Prevents man-in-the-middle (MITM) attacks
- Ensures you're connecting to the intended FortiGate device
- Protects credentials and configuration data in transit

**When to Disable (Development Only):**
- Local testing with self-signed certificates
- Lab environments without proper CA infrastructure
- Temporary troubleshooting

**Production Alternative:**
Instead of disabling verification, use a proper certificate:
1. Install a valid CA-signed certificate on FortiGate
2. Add self-signed CA certificate to Python's trust store
3. Use `verify='/path/to/ca-bundle.crt'` for custom CA

### 3. API Token Security

#### ✅ DO: Use API Tokens (Recommended)
```python
# API token authentication (stateless, secure)
fgt = FortiOS(
    host="fortigate.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    verify=True
)
```

**Benefits of API Tokens:**
- Stateless authentication (no session management)
- Granular permissions (API user can have limited scope)
- Easy rotation without password changes
- Audit trail in FortiGate logs

#### ⚠️ CAUTION: Username/Password Authentication
```python
# Username/password (session-based, deprecated in FortiOS 7.6+)
with FortiOS(
    host="192.168.1.1",
    username=os.getenv('FORTIOS_USER'),
    password=os.getenv('FORTIOS_PASS'),
    verify=True
) as fgt:
    # Auto-logout on exit
    status = fgt.api.monitor.system.status.get()
```

**Important Notes:**
- Username/password authentication is **deprecated** in FortiOS 7.6+
- Always use context manager (`with` statement) for auto-logout
- Tokens are preferred for production deployments

### 4. Network Security

#### ✅ DO: Use Secure Networks
- Connect over VPN or secure private networks
- Avoid public Wi-Fi for FortiGate management
- Use firewall rules to restrict API access

#### ✅ DO: Implement Rate Limiting
```python
# Use built-in retry logic with limits
fgt = FortiOS(
    host="fortigate.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    max_retries=3,  # Limit retry attempts
    verify=True
)
```

### 5. Data Sanitization

hfortix automatically sanitizes sensitive data in logs:

```python
# Sensitive fields are automatically redacted in logs
# password, token, secret, key, vdom, etc.
fgt = FortiOS(
    host="fortigate.example.com",
    token="sensitive_token",  # Logged as "***REDACTED***"
    debug='info'
)
```

**Automatically Redacted Fields:**
- `password`, `passwd`
- `token`, `api_key`, `apikey`
- `secret`, `passphrase`
- `private-key`, `psk`
- `authorization`
- `vdom` (to protect tenant info)

### 6. Read-Only Mode

Use read-only mode for safe exploration and testing:

```python
# Read-only mode: All write operations are blocked
fgt = FortiOS(
    host="production.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    read_only=True,  # ✅ Safe for production testing
    verify=True
)

# This will be logged but NOT executed
fgt.firewall.policy.create(name="test")  # Blocked by read-only mode
```

**Use Cases:**
- Testing against production environments
- Training and demonstrations
- CI/CD dry-run mode
- Audit and compliance checks

### 7. Operation Tracking

Enable operation tracking for audit trails:

```python
# Track all API operations for auditing
fgt = FortiOS(
    host="fortigate.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    track_operations=True,  # ✅ Enable audit logging
    verify=True
)

# Later, retrieve audit log
operations = fgt.get_operations()
for op in operations:
    print(f"{op['timestamp']} - {op['method']} {op['url']}")
```

### 8. Dependency Security

#### Keep Dependencies Updated
```bash
# Regularly update dependencies
pip install --upgrade hfortix

# Check for known vulnerabilities
pip install safety
safety check
```

#### Pin Versions in Production
```text
# requirements.txt
hfortix==0.3.21
httpx>=0.27.0,<1.0.0
```

### 9. Secure Coding Practices

#### ✅ DO: Validate User Input
```python
# Validate before making API calls
def create_address(name: str, subnet: str):
    # Basic validation
    if not name or not subnet:
        raise ValueError("Name and subnet required")
    
    if '..' in name or '/' not in subnet:
        raise ValueError("Invalid input")
    
    fgt.api.cmdb.firewall.address.create(
        name=name,
        subnet=subnet
    )
```

#### ✅ DO: Handle Exceptions Properly
```python
from hfortix import FortiOS
from hfortix.FortiOS.exceptions import AuthenticationError, APIError

try:
    fgt = FortiOS(
        host="fortigate.example.com",
        token=os.getenv('FORTIOS_TOKEN'),
        verify=True
    )
    result = fgt.api.cmdb.firewall.address.get("test")
except AuthenticationError:
    # Handle authentication failure
    logger.error("Invalid credentials")
except APIError as e:
    # Handle API errors
    logger.error(f"API error: {e}")
```

#### ✅ DO: Use Context Managers
```python
# Ensures proper cleanup
with FortiOS(
    host="fortigate.example.com",
    username=os.getenv('FORTIOS_USER'),
    password=os.getenv('FORTIOS_PASS'),
    verify=True
) as fgt:
    # Auto-logout on exit (for username/password auth)
    status = fgt.api.monitor.system.status.get()
```

### 10. Logging and Monitoring

#### ✅ DO: Configure Secure Logging
```python
import logging

# Configure logging with appropriate level
logging.basicConfig(
    level=logging.INFO,  # Don't use DEBUG in production
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/hfortix.log', mode='a'),
        logging.StreamHandler()
    ]
)

# Or use instance-specific debug level
fgt = FortiOS(
    host="fortigate.example.com",
    token=os.getenv('FORTIOS_TOKEN'),
    debug='warning',  # ✅ Limit verbosity in production
    verify=True
)
```

#### ❌ DON'T: Log Sensitive Data
```python
# Avoid logging raw credentials
# hfortix sanitizes automatically, but be careful with custom logging
logger.debug(f"Token: {token}")  # ❌ Never do this!
```

---

## Security Features in hfortix

### Built-in Security

1. **Default SSL Verification:** `verify=True` by default
2. **Credential Sanitization:** Automatic redaction in logs
3. **Private Variables:** Credentials stored in `_token`, `_password` (not public)
4. **No Hardcoded Secrets:** Zero hardcoded credentials in codebase
5. **Secure Defaults:** All security features enabled by default

### Security Audit Results

**Bandit Scan (December 22, 2025):**
- ✅ No high or medium severity issues
- ✅ No hardcoded passwords (8 false positives in test code)
- ✅ Proper exception handling throughout
- ✅ No SQL injection risks (no database interaction)
- ✅ No shell injection risks (no subprocess calls with user input)

**Code Quality:**
- ✅ 100% type hint coverage
- ✅ 100% PEP 8 compliance
- ✅ Comprehensive docstrings
- ✅ Automated testing (226 test files)

---

## Compliance and Standards

### Supported Authentication Standards
- **API Token (OAuth 2.0 Bearer Token)** - Recommended
- **Username/Password (Basic Auth)** - Deprecated in FortiOS 7.6+

### Encryption Standards
- **TLS 1.2+** - via httpx library
- **HTTP/2** - Enabled by default for better performance

### Logging Standards
- **Structured Logging** - Machine-readable format
- **Sensitive Data Redaction** - Automatic sanitization
- **Audit Trail** - Operation tracking available

---

## Production Deployment Checklist

Before deploying hfortix in production:

- [ ] ✅ Use API token authentication (not username/password)
- [ ] ✅ Store credentials in environment variables or secure vault
- [ ] ✅ Enable SSL verification (`verify=True`)
- [ ] ✅ Use proper CA-signed certificates on FortiGate
- [ ] ✅ Restrict API access with firewall rules
- [ ] ✅ Enable operation tracking for audit trail
- [ ] ✅ Set appropriate logging level (`warning` or `error`)
- [ ] ✅ Implement proper exception handling
- [ ] ✅ Pin dependency versions in requirements.txt
- [ ] ✅ Regularly update dependencies
- [ ] ✅ Review FortiGate API user permissions (principle of least privilege)
- [ ] ✅ Monitor API usage and set rate limits
- [ ] ✅ Implement automated security scanning in CI/CD
- [ ] ✅ Document security procedures for your team

---

## Additional Resources

- **FortiOS API Documentation:** https://docs.fortinet.com/
- **API User Configuration:** System > Admin > API Users
- **Certificate Management:** System > Certificates
- **Security Audit Tools:** bandit, safety, pip-audit
- **hfortix Documentation:** [README.md](README.md), [QUICKSTART.md](QUICKSTART.md)

---

## Questions or Concerns?

If you have security questions or need clarification on best practices:

- **Email:** hermanwjacobsen@gmail.com
- **GitHub Issues:** https://github.com/hermanwjacobsen/hfortix/issues (for non-security bugs)
- **Security Issues:** Email directly (do not create public issues)

**Remember:** Security is a shared responsibility. Always follow your organization's security policies and compliance requirements.
