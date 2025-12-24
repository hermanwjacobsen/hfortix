"""
FortiOS-Specific Exceptions
FortiOS error codes and product-specific exception handling
"""

from typing import Optional

# ============================================================================
# Helper Functions for Error Context
# ============================================================================


def _is_sensitive_param(param_name: str) -> bool:
    """
    Check if a parameter name contains sensitive data

    Args:
        param_name: Parameter name to check

    Returns:
        bool: True if parameter contains sensitive data
    """
    sensitive_keywords = {
        "password",
        "passwd",
        "pwd",
        "secret",
        "token",
        "api_key",
        "apikey",
        "key",
        "private",
        "credential",
        "auth",
    }
    param_lower = param_name.lower()
    return any(keyword in param_lower for keyword in sensitive_keywords)


def _sanitize_params(params: Optional[dict]) -> Optional[dict]:
    """
    Sanitize sensitive parameters for safe logging

    Args:
        params: Parameters dictionary to sanitize

    Returns:
        dict: Sanitized copy of parameters with sensitive values masked
    """
    if not params:
        return params

    sanitized = {}
    for key, value in params.items():
        if _is_sensitive_param(key):
            sanitized[key] = "***REDACTED***"
        else:
            # Truncate long values
            if isinstance(value, str) and len(value) > 100:
                sanitized[key] = value[:97] + "..."
            else:
                sanitized[key] = value
    return sanitized


# ============================================================================
# Base Exception Classes
# ============================================================================


class FortinetError(Exception):
    """Base exception for all Fortinet API errors"""


class APIError(FortinetError):
    """
    Generic API error with optional metadata

    Attributes:
        message: Error message
        http_status: HTTP status code (e.g., 400, 404, 500)
        error_code: FortiOS internal error code (e.g., -5, -3)
        response: Full API response dict
        endpoint: API endpoint path (e.g., '/api/v2/cmdb/firewall/policy')
        method: HTTP method (GET, POST, PUT, DELETE)
        params: Request parameters (sanitized)
        hint: Helpful suggestion for resolving the error
        request_id: Unique identifier for this request
        timestamp: ISO 8601 timestamp when error occurred
    """

    def __init__(
        self,
        message,
        http_status=None,
        error_code=None,
        response=None,
        endpoint=None,
        method=None,
        params=None,
        hint=None,
        request_id=None,
    ):
        import uuid
        from datetime import datetime, timezone

        super().__init__(message)
        self.http_status = http_status
        self.error_code = error_code
        self.response = response
        self.endpoint = endpoint
        self.method = method
        self.params = params
        self.hint = hint
        self._original_message = message

        # Add metadata for debugging
        self.request_id = request_id or str(uuid.uuid4())
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def __str__(self) -> str:
        """Format error with full context for better debugging"""
        parts = [self._original_message]

        # Add endpoint and method context
        if self.endpoint and self.method:
            parts.append(f"  → {self.method} {self.endpoint}")
        elif self.endpoint:
            parts.append(f"  → Endpoint: {self.endpoint}")

        # Add HTTP status if available
        if self.http_status:
            status_desc = get_http_status_description(self.http_status)
            parts.append(
                f"  → HTTP Status: {self.http_status} ({status_desc})"
            )

        # Add FortiOS error code if available
        if self.error_code:
            error_desc = get_error_description(self.error_code)
            parts.append(
                f"  → FortiOS Error: {self.error_code} ({error_desc})"
            )

        # Add parameters (sanitized) if available
        if self.params:
            sanitized = _sanitize_params(self.params)
            if sanitized:
                params_items = list(sanitized.items())[:5]
                params_str = ", ".join(f"{k}={v}" for k, v in params_items)
                if len(sanitized) > 5:
                    params_str += f", ... (+{len(sanitized) - 5} more)"
                parts.append(f"  → Parameters: {params_str}")

        # Add hint if available
        if self.hint:
            parts.append(f"  💡 {self.hint}")

        return "\n".join(parts)

    def __repr__(self) -> str:
        """Developer-friendly representation for debugging"""
        return (
            f"{self.__class__.__name__}("
            f"message={self._original_message!r}, "
            f"http_status={self.http_status}, "
            f"error_code={self.error_code}, "
            f"endpoint={self.endpoint!r}, "
            f"method={self.method!r}, "
            f"request_id={self.request_id!r})"
        )


class AuthenticationError(FortinetError):
    """HTTP 401 - Authentication failed (invalid credentials)"""


class AuthorizationError(FortinetError):
    """HTTP 403 - Authorization failed (insufficient permissions)"""


# ============================================================================
# Retry Logic Exception Hierarchy
# ============================================================================


class RetryableError(APIError):
    """
    Base exception for errors that should trigger automatic retry

    These errors are typically transient and may succeed on retry:
    - Rate limiting (429)
    - Service unavailable (503)
    - Timeouts
    - Circuit breaker open
    """


class NonRetryableError(APIError):
    """
    Base exception for errors that should NOT be retried

    These errors indicate client-side mistakes or permanent failures:
    - Bad request (400)
    - Resource not found (404)
    - Duplicate entry
    - Entry in use
    - Permission denied
    """


# ============================================================================
# Client-Side Configuration Exceptions
# ============================================================================


class ConfigurationError(FortinetError):
    """
    Raised when FortiOS instance is misconfigured

    Examples:
    - Both token and username/password provided
    - Missing required authentication
    - Invalid parameter combinations
    """


class VDOMError(FortinetError):
    """
    Raised when VDOM operation fails or VDOM doesn't exist

    Attributes:
        vdom: The VDOM name that caused the error
    """

    def __init__(self, message: str, vdom: str):
        super().__init__(message)
        self.vdom = vdom


class OperationNotSupportedError(FortinetError):
    """
    Raised when attempting unsupported operation on endpoint

    Attributes:
        operation: The operation that was attempted (e.g., 'DELETE')
        endpoint: The endpoint that doesn't support it
    """

    def __init__(self, message: str, operation: str, endpoint: str):
        super().__init__(message)
        self.operation = operation
        self.endpoint = endpoint


class ReadOnlyModeError(FortinetError):
    """
    Operation blocked by read-only mode

    Raised when attempting POST/PUT/DELETE operations with read_only=True.
    This is a client-side block to prevent accidental writes in safe mode.
    """


# ============================================================================
# HTTP Status Code Exceptions
# ============================================================================


class BadRequestError(NonRetryableError):
    """HTTP 400 - Bad Request"""

    def __init__(self, message="Bad request", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 400
        super().__init__(message, **kwargs)


class ResourceNotFoundError(NonRetryableError):
    """HTTP 404 - Resource not found"""

    def __init__(self, message="Resource not found", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 404
        super().__init__(message, **kwargs)

    def suggest_recovery(self) -> str:
        """Suggest how to recover from this error"""
        return (
            "Recovery options:\n"
            "  1. Use .post() to create the resource\n"
            "  2. Use .get() to list available resources\n"
            "  3. Check the name/ID for typos"
        )


class MethodNotAllowedError(NonRetryableError):
    """HTTP 405 - Method not allowed"""

    def __init__(self, message="Method not allowed", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 405
        super().__init__(message, **kwargs)


class RateLimitError(RetryableError):
    """HTTP 429 - Rate limit exceeded"""

    def __init__(self, message="Rate limit exceeded", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 429
        super().__init__(message, **kwargs)


class ServerError(RetryableError):
    """HTTP 500 - Internal server error"""

    def __init__(self, message="Internal server error", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 500
        super().__init__(message, **kwargs)


class ServiceUnavailableError(RetryableError):
    """HTTP 503 - Service temporarily unavailable"""

    def __init__(self, message="Service temporarily unavailable", **kwargs):
        if "http_status" not in kwargs:
            kwargs["http_status"] = 503
        super().__init__(message, **kwargs)


class CircuitBreakerOpenError(RetryableError):
    """Circuit breaker is open - service appears to be down"""

    def __init__(self, message="Circuit breaker is open", **kwargs):
        super().__init__(message, **kwargs)


class TimeoutError(RetryableError):
    """Request timed out"""

    def __init__(self, message="Request timed out", **kwargs):
        super().__init__(message, **kwargs)


# ============================================================================
# HTTP Status Code Reference
# ============================================================================

HTTP_STATUS_CODES = {
    200: "OK - Request successful",
    201: "Created - Resource created successfully",
    204: "No Content - Request successful, no content to return",
    400: "Bad Request - Invalid request syntax or parameters",
    401: "Unauthorized - Authentication required or failed",
    403: "Forbidden - Insufficient permissions",
    404: "Not Found - Resource does not exist",
    405: "Method Not Allowed - HTTP method not supported for this endpoint",
    409: "Conflict - Request conflicts with current state",
    422: "Unprocessable Entity - Request syntax is correct but semantically invalid",  # noqa: E501
    429: "Too Many Requests - Rate limit exceeded",
    500: "Internal Server Error - Server encountered an error",
    502: "Bad Gateway - Invalid response from upstream server",
    503: "Service Unavailable - Server temporarily unavailable",
    504: "Gateway Timeout - Upstream server timeout",
}


def get_http_status_description(status_code: int) -> str:
    """
    Get human-readable description for HTTP status code

    Args:
        status_code (int): HTTP status code

    Returns:
        str: Status description or "Unknown status code"
    """
    return HTTP_STATUS_CODES.get(
        status_code, f"Unknown status code: {status_code}"
    )


# ============================================================================
# FortiOS-Specific Exceptions
# ============================================================================


class DuplicateEntryError(NonRetryableError):
    """Duplicate entry exists (error code -5, -15, -100, etc.)"""

    def __init__(self, message="A duplicate entry already exists", **kwargs):
        if "error_code" not in kwargs:
            kwargs["error_code"] = -5
        super().__init__(message, **kwargs)

    def suggest_recovery(self) -> str:
        """Suggest how to recover from this error"""
        return (
            "Recovery options:\n"
            "  1. Use .put() to update the existing entry\n"
            "  2. Use .delete() then .post() to replace it\n"
            "  3. Use .get() to check if it matches your desired state"
        )


class EntryInUseError(NonRetryableError):
    """
    Entry cannot be deleted because it's in use (error code -23, -94,
    -95, etc.)
    """

    def __init__(
        self, message="Entry is in use and cannot be deleted", **kwargs
    ):
        if "error_code" not in kwargs:
            kwargs["error_code"] = -23
        super().__init__(message, **kwargs)

    def suggest_recovery(self) -> str:
        """Suggest how to recover from this error"""
        return (
            "Recovery options:\n"
            "  1. Remove references to this entry first\n"
            "  2. Use .get() to find what's using this entry\n"
            "  3. Check policies, groups, or other objects using this"
        )


class InvalidValueError(NonRetryableError):
    """Invalid value provided (error code -651, -1, -50, etc.)"""

    def __init__(self, message="Input value is invalid", **kwargs):
        if "error_code" not in kwargs:
            kwargs["error_code"] = -651
        super().__init__(message, **kwargs)


class PermissionDeniedError(NonRetryableError):
    """Permission denied, insufficient privileges (error code -14, -37)"""

    def __init__(
        self, message="Permission denied. Insufficient privileges.", **kwargs
    ):
        if "error_code" not in kwargs:
            kwargs["error_code"] = -14
        super().__init__(message, **kwargs)


# ============================================================================
# FortiOS Error Codes
# Comprehensive mapping of internal error codes to descriptions
# ============================================================================

FORTIOS_ERROR_CODES = {
    # Common Errors (-1 to -100)
    -1: "Invalid length of value",
    -2: "Index out of range",
    -3: "Entry not found",
    -4: "Maximum number of entries has been reached",
    -5: "A duplicate entry already exists",
    -6: "Failed memory allocation",
    -7: "Value conflicts with system settings",
    -8: "Invalid IP Address",
    -9: "Invalid IP Netmask",
    -10: "Invalid gateway address",
    -11: "Incorrect hexadecimal entry. Must use 2 hex digits in the range 0-9, A-F",  # noqa: E501
    -12: "Invalid IPSEC auto algorithm chosen",
    -13: "Invalid Timeout value. Should be in the range 1-480",
    -14: "Permission denied. Insufficient privileges",
    -15: "Duplicate entry found",
    -16: "Blank or incorrect address entry",
    -17: "Incorrect address name",
    -18: "Incorrect service value",
    -19: "Incorrect schedule value",
    -20: "Blank entry",
    -21: "Invalid IPsec tunnel",
    -22: "Invalid IPsec tunnel",
    -23: "Entry is used",
    -24: "Error opening file",
    -25: "Error reading from shared memory",
    -26: "File error",
    -27: "Error opening IP-MAC info file",
    -28: "File is not an update file",
    -29: "Failed to update routing information",
    -30: "Invalid username or password",
    -31: "Invalid old password",
    -32: "Invalid PIN number",
    -33: "Invalid MAC address",
    -34: "Duplicate remote gateway",
    -35: "Duplicate destination in VPN policy",
    -36: "Duplicate or invalid VIP mapping",
    -37: "Permission denied",
    -38: "Download file does not exist",
    -39: "Configuration file error",
    -40: "Invalid DHCP range. Start address is greater than end address",
    -41: "Invalid service group",
    -42: "DMZ->Internal virtual IP mapping is not allowed",
    -43: "Cannot use the external interface's IP as a virtual IP",
    -44: "Set RADIUS info before enabling RADIUS",
    -45: "Invalid IP range",
    -46: "Invalid zone",
    -47: "Replacement message is too large",
    -48: "The end time should be later than the start time",
    -49: "The password must conform to the system password policy",
    -50: "Input is in invalid format",
    -51: "Out of length. Max length is 80 western characters",
    -52: "Upload file is too big or invalid",
    -53: "Banned word used has an invalid character",
    -54: "IP address is in same subnet as the others",
    -55: "Duplicate default gateway",
    -56: "Empty values are not allowed",
    -57: "Server error",
    -58: "PPPOE permission deny",
    -59: "PPPOE is trying",
    -60: "PPPOE password error",
    -61: "Input not as expected",
    -62: "One time schedule stop time should be later than the current time",
    -63: "FortiGuard AV update failed",
    -64: "IPS update failed",
    -65: "Unable to uncompress the tar file you provided",
    -66: "Unable to uncompress the gz file you provided",
    -67: "Cannot create tmp directory",
    -68: "Upload file should contain the migadmin and bin directories",
    -69: "Unable to activate the key you provided",
    -70: "Cannot enable the smartfilter categories",
    -71: "Failed to update the smartfilter",
    -72: "Field value exceeds the maximum number of characters",
    -73: "End IP cannot be smaller than the start IP",
    -74: "The last download operation has not ended yet, please wait until it finishes",  # noqa: E501
    -75: "DHCP range has conflict with IP/MAC binding",
    -76: "DHCP relay cannot be created because DHCP server of same type already exists on that interface",  # noqa: E501
    -77: "DHCP server cannot be created because DHCP relay of same type already exists on that interface",  # noqa: E501
    -78: "DHCP over IPSEC service created conflicts with another DHCP over IPSEC service on VPN's internal interface",  # noqa: E501
    -79: "Internal error in ipsec",
    -80: "No route to the remote gateway",
    -81: "No tunnel",
    -82: "Tunnel already exists",
    -83: "SPI already exists",
    -84: "No route or SPI already exists",
    -85: "Firewall has all the updates found in the given file",
    -86: "File does not contain any updates for this feature",
    -87: "IMAGE crc error",
    -88: "VLAN name error",
    -89: "Invalid number",
    -90: "Invalid IP pool name",
    -91: "IP pool address should match the interface",
    -92: "Invalid external service port. It has been occupied by system",
    -93: "Connection config error",
    -94: "The user group cannot be deleted because it is in use by one of the policies",  # noqa: E501
    -95: "The user group cannot be deleted because it is in use by PPTP",
    -96: "The user group cannot be deleted because it is in use by L2TP",
    -97: "The radius cannot be deleted because it is in use by one of the users",  # noqa: E501
    -98: "There is no such user group name",
    -99: "The radius cannot be deleted because it is in use by one of the groups",  # noqa: E501
    -100: "A duplicate user name already exists",
    # User/Group/Auth Errors (-101 to -200)
    -101: "A duplicate remote server name already exists",
    -102: "The route gateway is used by policy route",
    -103: "The gateway is not a valid gateway",
    -104: "The gateway is not a valid gateway",
    -105: "The gateway is not a valid gateway",
    -106: "The gateway is not a valid gateway",
    -107: "The user group cannot be deleted because it is in use by IPSEC",
    -108: "Update center cannot be both empty",
    -109: "Invalid email address",
    -110: "The keylife value cannot be smaller than 120 seconds",
    -111: "FortiGuard AV update unauthorized",
    -112: "IPS update unauthorized",
    -113: "The keylife value cannot be bigger than 172800 seconds",
    -114: "The keep-alive frequency cannot be longer than 900 seconds",
    -115: "The gateway is not a valid gateway",
    -116: "Please enter an external interface name",
    -117: "Remote IP must be set if IP is defined",
    -118: "IP must be set if remote IP is defined",
    -119: "Blank or incorrect schedule entry",
    -122: "The VLAN is not in the same zone as the address",
    -123: "Invalid day input",
    -124: "Invalid hour input",
    -125: "Minute should be 00, 15, 30 and 45 only",
    -126: "Update center cannot both be empty",
    -127: "Invalid admin timeout",
    -128: "Invalid auth timeout",
    -129: "PIN number length should be 6 digits",
    -130: "Invalid date input",
    -131: "Invalid year input",
    -132: "Invalid month input",
    -133: "Invalid day input",
    -134: "Invalid time input",
    -135: "Invalid hour input",
    -136: "Invalid minute input",
    -137: "Invalid second input",
    -138: "The gateway peerid cannot be same as the localid or peerid in any other gateway settings",  # noqa: E501
    -139: "The IP pool range cannot be larger than a class A subnet",
    -140: "Missing the ipsec phase1 dpd value",
    -141: "Missing the ipsec phase1 dpd idleworry value",
    -142: "Missing the ipsec phase1 dpd retrycount value",
    -143: "Missing the ipsec phase1 dpd retryinterval value",
    -144: "Missing the ipsec phase1 dpd idlecleanup value",
    -145: "The imported local certificate is invalid",
    -146: "The imported CA certificate is invalid",
    -147: "The certificate is being used",
    -148: "Rules file format error",
    -149: "User group does not exist",
    -150: "Log level out of range",
    -151: "The certificate does not exist",
    -152: "Invalid encryption key",
    -153: "Invalid authentication key",
    -154: "Bridge management IP and HA port IP cannot be in the same subnet",
    -155: "Keylife KBytes value must be greater than 5120",
    -156: "The IP pool range overlapped an existing IP pool range",
    -157: "This interface cannot be assigned to a zone because it is currently being used by a policy",  # noqa: E501
    -158: "Invalid VLAN ID",
    -160: "CFG_ER_GENERIC",
    -161: "The primary and secondary IP cannot be the same",
    -162: "Service names and service group names cannot be the same",
    -163: "Address names and address group names cannot be the same",
    -164: "Address names and virtual IP names cannot be the same",
    -165: "Address group names and virtual IP names cannot be the same",
    -166: "The name is too long",
    -167: "Failed to import pkcs12 file",
    -168: "Could not export pkcs12 file",
    -169: "Your traffic shaping maximum bandwidth must be greater than your guaranteed bandwidth",  # noqa: E501
    -170: "Invalid SMTP mail server format",
    -171: "Invalid SMTP mail user format",
    -172: "No password for authentication",
    -173: "The string contains XSS vulnerability characters",
    -175: "Max size of log file must be in the range 1 and 1024",
    -176: "This ippool is being used by a policy",
    -177: "Moving a policy from one interface/zone pair to a different interface/zone pair is not permitted",  # noqa: E501
    -178: "Moving a policy from one interface/zone to a different interface/zone is not permitted",  # noqa: E501
    -180: "We are unable to send your update request",
    -181: "Upload file is too big, only part of it is saved",
    -183: "Incorrect upload file or the file is empty",
    -184: "Some duplicate entries in the upload file have been removed",
    -185: "Too many regular expression entries were present in the upload file, only part of them were saved",  # noqa: E501
    -186: "Maximum number of regular expression entries has been reached",
    -187: "End Point pattern exceeds the maximum length",
    -188: "Cannot have both HA and session-sync turned on",
    -190: "Too many interfaces to detect",
    # Authentication Errors (-203 to -257)
    -203: "Invalid Username or Password",
    -204: "Invalid Username or Password",
    -210: "Interface is not in manual addressing mode",
    -211: "Interface is not in dhcp or pppoe addressing mode",
    -212: "Interface is not in dhcp addressing mode",
    -213: "Interface is not in pppoe addressing mode",
    -214: "DHCP Server is not enabled on the interface",
    -215: "Invalid interface name",
    -216: "DHCP Client has not connected to DHCP server",
    -217: "Cannot set mode to DHCP or PPPoE when HA is on",
    -218: "Interface speed cannot be set for aggregated interfaces",
    -220: "Missing interface keyword or parameter",
    -221: "Missing scope keyword or parameter",
    -222: "Missing IP range keyword or parameter",
    -223: "Missing netmask keyword or parameter",
    -224: "Scope name already exists",
    -230: "Start IP, end IP, and default gateway are not in the same subnet",
    -231: "Start IP and end IP cannot be in the same subnet with other scopes",
    -232: "Start IP and end IP cannot be changed to different subnet",
    -233: "Start IP and end IP conflict with excluded IP range configuration",
    -234: "Start IP and end IP conflict with reserved IP-MAC configuration",
    -235: "Scope IP pool conflicts with system IP-MAC binding configuration",
    -236: "A regular(Ethernet) DHCP server cannot be configured on an interface without a static IP",  # noqa: E501
    -240: "Invalid DHCP lease time",
    -241: "Invalid default gateway IP address",
    -242: "Invalid DNS IP address",
    -243: "Invalid WINS IP address",
    -244: "Invalid exclude IP address",
    -245: "Invalid exclude IP range",
    -250: "Duplicated IP in reserved IP/MAC pair",
    -251: "Duplicated MAC address in reserved IP/MAC pair",
    -252: "Invalid port",
    -253: "Conflicted IP timeout must be between 60 and 8640000 seconds",
    -254: "Invalid IPv6 prefix",
    -255: "Invalid IPv6 address",
    -257: "Invalid hostname",
    # VIP/Certificate/Protocol Errors (-292 to -393)
    -292: "Reached maximum number of real servers for this VIP",
    -300: "Email banned word operation failed",
    -301: "Invalid email banned word",
    -302: "Error importing remote certificate",
    -303: "SCEP certificate enrollment failed",
    -310: "Virtual IP group names and virtual IP names cannot be the same",
    -311: "Virtual IP group names and address names cannot be the same",
    -312: "Virtual IP group names and address group names cannot be the same",
    -313: "The bookmark group could not be deleted because it is used by one of the SSLVPN user groups",  # noqa: E501
    -314: "At least one SSL VPN web application needs to be enabled",
    -315: "Archived file does not exist on Disk",
    -350: "Invalid ICMP type",
    -351: "Invalid ICMP code",
    -352: "This ICMP code does not exist for the ICMP type",
    -353: "This ICMP type does not have code",
    -354: "The IP protocol number is not allowed here",
    -360: "CMDB commands timeout",
    -361: "The CMDB add entry failed",
    -363: "Invalid port range",
    -375: "A radius server in this vdom is used by wireless setting",
    -376: "VDOM contains vdom-link",
    -377: "Invalid IPsec transform. Encryption and authentication cannot both be NULL",  # noqa: E501
    -390: "Invalid GTP RAI value",
    -392: "Invalid GTP IMEI value",
    -393: "Carrier feature license invalid or not present",
    -400: "Invalid ping server IP",
    # Interface/VDOM Errors (-506 to -565)
    -506: "Interface IP overlap",
    -508: "Please input a valid interface IP",
    -509: "The interface is not allowed to change the zone because one of the policies depends on it",  # noqa: E501
    -513: "Duplicate virtual domain name",
    -514: "Virtual domains still in use cannot be deleted",
    -515: "The name is a reserved keyword by the system",
    -516: "AV profile is empty",
    -519: "Interface name cannot be the same as VDOM",
    -520: "VLAN MTU cannot be larger than its physical interface's MTU",
    -521: "Physical interface MTU cannot be smaller than its VLAN interface's MTU",  # noqa: E501
    -522: "VLAN ID or physical interface cannot be changed once a VLAN has been created",  # noqa: E501
    -523: "Virtual domain license exceeded",
    -525: "Timeout should be between 0 and 65535 seconds",
    -526: "Another DHCP server with a lease range of the same subnet ID already exists",  # noqa: E501
    -527: "The interface name for a DHCP server can't be more than 14 characters",  # noqa: E501
    -528: "The client interface name for a DHCP relay can't be more than 14 characters",  # noqa: E501
    -529: "An ActiveDirectory group on this server is being used by a user group",  # noqa: E501
    -530: "Interfaces must have the same forward domain ID in TP mode",
    -531: "PPTP timeout must be between 0 and 65535 minutes",
    -540: "Invalid IP range. The specified IPs must be contained on the same 24-bit subnet (x.x.x.1-x.x.x.254)",  # noqa: E501
    -541: "Invalid IP range. The L2TP and PPTP address ranges must not overlap",  # noqa: E501
    -542: "The imported CRL certificate is invalid",
    -550: "Cannot enable HTTPS redirect because FortiClient checking is enabled in some policy",  # noqa: E501
    -551: "Cannot enable FortiClient checking because authentication is redirected to HTTPS",  # noqa: E501
    -552: "Cannot create interface with name that could conflict with interfaces created by changing internal-switch-mode",  # noqa: E501
    -553: "Name conflicts with an interface, vdom, switch-interface, zone, or interface name used for hardware switch interfaces",  # noqa: E501
    -554: "Switch-interface members cannot be changed once the switch has been created",  # noqa: E501
    -555: "Software switch interfaces are not permitted in transparent mode",
    -560: "Supplied name is a reserved keyword and cannot be used",
    -561: "Registering device to FortiManager failed",
    -562: "Please select an endpoint NAC profile",
    -563: "Please select an application detection list",
    -564: "Invalid FortiClient license key",
    -565: "A specific application must be selected for 'Not Installed' or 'Not Running' rules with a 'Deny' action",  # noqa: E501
    -580: "The vdom property limit has been reached",
    -581: "Must delete one replacemsg group otherwise it will exceed group limit after vdom enable",  # noqa: E501
    # Web Filtering/Content Errors (-600 to -713)
    -600: "Invalid category or group",
    -602: "Invalid reporting time range",
    -603: "Invalid number of arguments specified",
    -604: "FortiGuard Web Filtering reports are unavailable on units without hard drives",  # noqa: E501
    -605: "That protection profile does not exist",
    -606: "An unknown error occurred while processing the configuration request",  # noqa: E501
    -607: "Invalid duration",
    -608: "Invalid date/time format. The date and time must be 'yyyy/mm/dd hh:mm:ss'",  # noqa: E501
    -609: "The specified expiry date is invalid. It must be from 5 minutes to 365 days in the future",  # noqa: E501
    -610: "Invalid local category ID (must be in the range 96-127)",
    -611: "Invalid override authentication port (must be in the range 1-65535 excluding 80 and 443)",  # noqa: E501
    -612: "Invalid cache time-to-live (must be in the range 300-86400 seconds)",  # noqa: E501
    -613: "Invalid cache memory usage limit (must be in the range 2-15%)",
    -614: "Only a domain name can be specified for this rule type. Either specify only the domain name or change the type to directory",  # noqa: E501
    -615: "The HTTP and HTTPS override authentication ports cannot overlap",
    -650: "The integer value is not within valid range",
    -651: "Input value is invalid",
    -652: "Some of the filter elements specified are mutually exclusive",
    -653: "Invalid regular expression",
    -658: "Question marks are not allowed in simple URL Filter entries",
    -659: "Cannot change to TP mode because this vdom has at least one vdom-link or loopback interface",  # noqa: E501
    -690: "You must have at least one authentication method enabled",
    -701: "Wrong Group type in group definition",
    -702: "Group id out of range in group definition",
    -703: "Unknown keyword",
    -704: "Keyword in wrong sequence or the mandatory keywords are missing",
    -705: "Wrong value for given keyword",
    -706: "Missing start '(' in rule definition",
    -707: "Missing start ')' in rule definition",
    -708: "Missing default value for given parameter",
    -709: "IPS rule definition is incomplete",
    -710: "Missing required keyword",
    -711: "Unknown signature format",
    -712: "The user-defined rule name is invalid",
    -713: "Input value is invalid",
    # VPN/Backup/System Errors (-800 to -1102)
    -800: "The SSL VPN session zone cannot be deleted because it is in use by one of the policies",  # noqa: E501
    -901: "Backup failed, please try again",
    -902: "Restore failed, please try again",
    -950: "Invalid timeout",
    -951: "Protocol mismatch",
    -952: "Invalid DLP action",
    -953: "Invalid DLP archive setting",
    -1000: "The operation mode has been changed",
    -1001: "Invalid number of arguments",
    -1002: "Invalid key size",
    -1003: "Invalid key",
    -1004: "Cannot update license file",
    -1010: "Login Disclaimer Declined",
    -1100: "Invalid FortiClient Installer",
    -1101: "FortiGuard service is unavailable",
    -1102: "Downloading FortiClient installer from FortiGuard timed out",
    # Password/SSL VPN Errors (-2001 to -2011)
    -2001: "Your password must be at least 1 character long",
    -2002: "Your password cannot contain the following characters: ~ ! # % ^ & *+`':()[]{}<>|/",  # noqa: E501
    -2003: "The password entries do not match",
    -2004: "Your name is invalid",
    -2006: "Your password must be at least 8 characters long",
    -2007: "SSLVPN port and HTTPS admin port clash on same IP address",
    -2008: "Destination address of split tunneling policy is invalid",
    -2009: "Please select at least one client check option when client check is enabled",  # noqa: E501
    -2011: "At least one IP pool must be specified for SSL VPN tunnel mode",
    # File/FortiAnalyzer Errors (-3000 to -3248)
    -3000: "Internal error processing requested file",
    -3001: "Line in the uploaded file is too long",
    -3002: "Uploaded file contains binary symbols",
    -3003: "Out of temporary space",
    -3004: "Line in the uploaded file has an invalid format",
    -3005: "Line in the uploaded file contains an invalid language ID",
    -3199: "Unable to retrieve FortiAnalyzer status",
    -3200: "FortiAnalyzer IP is not valid",
    -3201: "FortiAnalyzer IP is used by other settings",
    -3202: "Cannot connect to FortiAnalyzer",
    -3203: "FortiAnalyzer version does not recognize remote log viewing request",  # noqa: E501
    -3204: "FortiAnalyzer is used by other settings",
    -3205: "Error reading FortiAnalyzer report files",
    -3206: "Please configure a FortiAnalyzer device",
    -3207: "Archived file does not exist on FortiAnalyzer device",
    -3208: "Invalid option on FortiAnalyzer",
    -3209: "Communication error with FortiAnalyzer device",
    -3210: "Hello holdtime must not be less than hello interval",
    -3211: "You must set a BSR interface if you are a BSR candidate",
    -3212: "You must set a RP candidate interface if you are a RP candidate",
    -3213: "You must set the source override interface",
    -3214: "Query interval must be greater than Query max response time",
    -3215: "Inputted IP is not a multicast IP address",
    -3216: "Multicast route threshold must not exceed multicast route limit",
    -3220: "Report name is already in use",
    -3221: "Access permissions are disabled on the FortiAnalyzer",
    -3222: "No available reports on the FortiAnalyzer",
    -3230: "Cannot connect to FortiGuard",
    -3231: "FortiGuard version does not recognize remote log viewing request",
    -3232: "There was an error when purging FortiGuard logs",
    -3233: "Archived file does not exist on FortiGuard Service device",
    -3234: "Invalid option on FortiGuard Service",
    -3235: "Communication error with FortiGuard Service device",
    -3240: "Unable to update FortiGuard Analysis & Management Service license information",  # noqa: E501
    -3241: "Error requesting image from the management station",
    -3242: "Error downloading image from the management station",
    -3243: "Error saving configuration to the management station",
    -3244: "Error retrieving configuration from the management station",
    -3245: "Error retrieving configuration from the management station",
    -3246: "Error retrieving diff from the management station",
    -3247: "Error requesting firmware image list",
    -3248: "Failed to delete script execution history record",
    # Wireless/System Errors (-4001 to -10002)
    -4001: "Please remove virtual AP interfaces before switching out of AP mode",  # noqa: E501
    -10000: "Invalid action",
    -10001: "Request missing",
    -10002: "Invalid request",
}


# ============================================================================
# Helper Functions
# ============================================================================


def get_error_description(error_code: int) -> str:
    """
    Get human-readable description for FortiOS error code

    Args:
        error_code (int): FortiOS error code

    Returns:
        str: Error description or "Unknown error"

    Examples:
        >>> get_error_description(-5)
        'A duplicate entry already exists'
        >>> get_error_description(-651)
        'Input value is invalid'
    """
    return FORTIOS_ERROR_CODES.get(error_code, "Unknown error")


def _extract_resource_from_endpoint(endpoint: Optional[str]) -> Optional[str]:
    """
    Extract resource name from API endpoint path

    Args:
        endpoint: API endpoint path (e.g., '/api/v2/cmdb/firewall/address')

    Returns:
        Resource name (e.g., 'address') or None

    Examples:
        >>> _extract_resource_from_endpoint('/api/v2/cmdb/firewall/address')
        'address'
        >>> _extract_resource_from_endpoint('/api/v2/cmdb/system/interface')
        'interface'
    """
    if not endpoint:
        return None

    # Remove leading/trailing slashes and split
    parts = endpoint.strip("/").split("/")

    # API endpoint format: api/v2/{api_type}/{category}/{resource}
    # Example: api/v2/cmdb/firewall/address
    if len(parts) >= 5:
        return parts[4]  # Return resource name
    elif len(parts) >= 4:
        return parts[3]  # Some endpoints are shorter

    return None


def _check_validation_available(
    endpoint: Optional[str], method: Optional[str]
) -> bool:
    """
    Check if validation helper exists for this endpoint and method

    Args:
        endpoint: API endpoint path
        method: HTTP method (GET, POST, PUT, DELETE)

    Returns:
        bool: True if validation helper exists
    """
    if not endpoint or not method:
        return False

    resource = _extract_resource_from_endpoint(endpoint)
    if not resource:
        return False

    # Derive module path from endpoint
    # Example: /api/v2/cmdb/firewall/address -> firewall._helpers.address
    parts = endpoint.strip("/").split("/")
    if len(parts) < 4:
        return False

    api_type = parts[2]  # cmdb, monitor, log, service
    category = parts[3]  # firewall, system, user, etc.

    if api_type != "cmdb":
        # Currently, most validation helpers are for CMDB endpoints
        return False

    # Try to import the validation module
    try:
        module_path = (
            f"hfortix.FortiOS.api.v2.{api_type}.{category}._helpers.{resource}"
        )
        __import__(module_path)
        return True
    except ImportError:
        return False


def _get_validation_hint(
    endpoint: Optional[str],
    method: Optional[str],
    error_code: Optional[int],
    http_status: Optional[int],
) -> str:
    """
    Get validation-specific hint if validation helper exists

    NOTE: Validation functions are for internal wrapper development.
    This function is disabled for end-user error messages.
    Validation is handled internally by wrapper classes.

    Args:
        endpoint: API endpoint path
        method: HTTP method
        error_code: FortiOS error code
        http_status: HTTP status code

    Returns:
        Validation hint string (currently always empty)
    """
    # Validation hints removed - validation is internal to wrappers
    # Users should use high-level wrapper methods that handle validation
    return ""


def _get_suggestion_for_error(
    error_code: Optional[int],
    http_status: Optional[int],
    endpoint: Optional[str] = None,
    method: Optional[str] = None,
) -> str:
    """
    Get helpful suggestion based on error type

    Args:
        error_code: FortiOS error code
        http_status: HTTP status code
        endpoint: API endpoint path (optional)
        method: HTTP method (optional)

    Returns:
        str: Helpful suggestion for the user, or empty string
    """
    # Enhanced suggestions with common fixes
    suggestions = {
        -3: "💡 Tip: Use .exists() to check if the object exists before accessing it.",  # noqa: E501
        -5: "💡 Tip: Use .exists() to check for duplicates before creating, or .update() to modify existing objects.",  # noqa: E501
        -15: "💡 Tip: Use unique names for all objects. Use .exists() to verify uniqueness.",  # noqa: E501
        -23: "💡 Tip: Remove references from firewall policies and other configs before deleting.",  # noqa: E501
        -94: "💡 Tip: Remove user group from all firewall policies before deleting.",  # noqa: E501
        -95: "💡 Tip: Remove user group from PPTP configuration before deleting.",  # noqa: E501
        -14: "💡 Tip: Check VDOM access permissions and API token admin privileges.",  # noqa: E501
        -37: "💡 Tip: Ensure your API token or user has sufficient read/write permissions.",  # noqa: E501
        -651: "💡 Tip: Invalid value provided. Check parameter format and allowed values.",  # noqa: E501
        -1: "💡 Tip: Check string length limits and field format requirements.",
        -50: "💡 Tip: Input format is invalid. Validate format matches expected pattern (IP, MAC, etc.).",  # noqa: E501
        -8: (
            "💡 Tip: Invalid IP address format. "
            "Use format: x.x.x.x or x.x.x.x/mask"
        ),
        -9: (
            "💡 Tip: Invalid IP netmask. Use CIDR notation "
            "(e.g., /24) or dotted decimal (255.255.255.0)"
        ),
        -33: (
            "💡 Tip: Invalid MAC address format. "
            "Use format: xx:xx:xx:xx:xx:xx"
        ),
        -72: (
            "💡 Tip: Field value exceeds maximum length. "
            "Check character limits for this field."
        ),
    }

    http_suggestions = {
        404: (
            "💡 Tip: Verify the object name and endpoint path. "
            "Use .exists() to check availability."
        ),
        400: (
            "💡 Tip: Bad request - check required parameters "
            "and their format."
        ),
        401: (
            "💡 Tip: Verify API token is valid and not expired. "
            "Re-authenticate if needed."
        ),
        403: (
            "💡 Tip: Check VDOM access and ensure API user "
            "has required permissions."
        ),
        429: (
            "💡 Tip: Implement rate limiting in your code or "
            "increase delay between requests."
        ),
        500: (
            "💡 Tip: This is a FortiGate server error. "
            "Check device logs and system status."
        ),
        503: (
            "💡 Tip: FortiGate may be busy or restarting. "
            "Wait and retry with exponential backoff."
        ),
    }

    hint_parts = []

    # Check error code first (more specific)
    if error_code in suggestions:
        hint_parts.append(f"\n{suggestions[error_code]}")
    # Fall back to HTTP status
    elif http_status in http_suggestions:
        hint_parts.append(f"\n{http_suggestions[http_status]}")

    # Add validation hint if available
    validation_hint = _get_validation_hint(
        endpoint, method, error_code, http_status
    )
    if validation_hint:
        hint_parts.append(validation_hint)

    return "".join(hint_parts)


def raise_for_status(
    response: dict,
    endpoint: Optional[str] = None,
    method: Optional[str] = None,
    params: Optional[dict] = None,
) -> None:
    """
    Raise appropriate exception based on FortiOS API response

    Args:
        response (dict): API response dictionary
        endpoint (str): Optional API endpoint for better error context
        method (str): Optional HTTP method (GET, POST, PUT, DELETE)
        params (dict): Optional request parameters (will be sanitized)

    Raises:
        APIError: If response indicates an error

    Examples:
        >>> response = {'status': 'error', 'http_status': 404, 'error': -3}
        >>> raise_for_status(
        ...     response,
        ...     endpoint='/api/v2/cmdb/firewall/address',
        ...     method='GET'
        ... )
        # Raises ResourceNotFoundError with helpful context and tip
    """
    if not isinstance(response, dict):
        return

    status = response.get("status")
    if status == "success":
        return  # Success case - no exception to raise

    http_status = response.get("http_status")
    error_code = response.get("error")
    message = response.get("error_description", "API request failed")

    # Get helpful suggestion based on error type (now validation-aware)
    hint = _get_suggestion_for_error(error_code, http_status, endpoint, method)

    # Prepare common exception kwargs
    exc_kwargs = {
        "http_status": http_status,
        "error_code": error_code,
        "response": response,
        "endpoint": endpoint,
        "method": method,
        "params": params,
        "hint": hint,
    }

    # Priority 1: Check error codes first (more specific than HTTP status)
    if error_code == -5 or error_code == -15 or error_code == -100:
        raise DuplicateEntryError(message, **exc_kwargs)
    elif (
        error_code == -23
        or error_code == -94
        or error_code == -95
        or error_code == -96
    ):
        raise EntryInUseError(message, **exc_kwargs)
    elif error_code == -14 or error_code == -37:
        raise PermissionDeniedError(message, **exc_kwargs)
    elif error_code == -651 or error_code == -1 or error_code == -50:
        raise InvalidValueError(message, **exc_kwargs)
    elif error_code == -3:
        raise ResourceNotFoundError(message, **exc_kwargs)

    # Priority 2: Check HTTP status codes
    elif http_status == 404:
        raise ResourceNotFoundError(message, **exc_kwargs)
    elif http_status == 400:
        raise BadRequestError(message, **exc_kwargs)
    elif http_status == 401:
        raise AuthenticationError(message)
    elif http_status == 403:
        raise AuthorizationError(message)
    elif http_status == 405:
        raise MethodNotAllowedError(message, **exc_kwargs)
    elif http_status == 429:
        raise RateLimitError(message, **exc_kwargs)
    elif http_status == 500:
        raise ServerError(message, **exc_kwargs)
    elif http_status == 503:
        raise ServiceUnavailableError(message, **exc_kwargs)

    # Default: Generic APIError
    else:
        raise APIError(message, **exc_kwargs)


# ============================================================================
# Helper Utility Functions
# ============================================================================


def is_retryable_error(error: Exception) -> bool:
    """
    Check if error should trigger automatic retry

    Args:
        error: Exception to check

    Returns:
        True if error is retryable, False otherwise

    Example:
        >>> try:
        ...     fgt.api.cmdb.firewall.policy.get()
        ... except Exception as e:
        ...     if is_retryable_error(e):
        ...         time.sleep(5)
        ...         # retry logic here
    """
    return isinstance(error, RetryableError)


def get_retry_delay(
    error: Exception,
    attempt: int,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
) -> float:
    """
    Calculate appropriate retry delay based on error type and attempt number

    Args:
        error: Exception that occurred
        attempt: Retry attempt number (1, 2, 3, ...)
        base_delay: Base delay in seconds (default: 1.0)
        max_delay: Maximum delay in seconds (default: 60.0)

    Returns:
        Recommended delay in seconds

    Example:
        >>> for attempt in range(1, 4):
        ...     try:
        ...         result = fgt.api.cmdb.firewall.policy.get()
        ...         break
        ...     except Exception as e:
        ...         if is_retryable_error(e):
        ...             delay = get_retry_delay(e, attempt)
        ...             time.sleep(delay)
        ...         else:
        ...             raise
    """
    if isinstance(error, RateLimitError):
        # Exponential backoff for rate limits
        delay = min(base_delay * (2**attempt), max_delay)
    elif isinstance(error, ServiceUnavailableError):
        # Linear backoff for service issues
        delay = min(base_delay * attempt, max_delay)
    elif isinstance(error, TimeoutError):
        # Moderate exponential backoff for timeouts
        delay = min(base_delay * (1.5**attempt), max_delay)
    else:
        # Default to base delay
        delay = base_delay

    return delay


# ============================================================================
# Exports
# ============================================================================

__all__ = [
    # Base exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    # Retry hierarchy
    "RetryableError",
    "NonRetryableError",
    # Client-side exceptions
    "ConfigurationError",
    "VDOMError",
    "OperationNotSupportedError",
    "ReadOnlyModeError",
    # HTTP status exceptions
    "BadRequestError",
    "ResourceNotFoundError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    "CircuitBreakerOpenError",
    "TimeoutError",
    # FortiOS-specific exceptions
    "DuplicateEntryError",
    "EntryInUseError",
    "InvalidValueError",
    "PermissionDeniedError",
    # Helper functions
    "get_error_description",
    "get_http_status_description",
    "raise_for_status",
    "is_retryable_error",
    "get_retry_delay",
    # Data
    "FORTIOS_ERROR_CODES",
    "HTTP_STATUS_CODES",
]
