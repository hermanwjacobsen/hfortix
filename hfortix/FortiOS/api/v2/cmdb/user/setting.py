"""
FortiOS CMDB - User Setting

API Endpoints:
    GET    /user/setting
    PUT    /user/setting
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Setting:
    """Setting operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Setting endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select all entries in a CLI table.
        
        Args:
            exclude_default_values: Exclude properties/objects with default value (optional)
            stat_items: Items to count occurrence in entire response (multiple items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/user/setting"
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if stat_items is not None:
            params['stat-items'] = stat_items
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        auth_type: str | None = None,
        auth_cert: str | None = None,
        auth_ca_cert: str | None = None,
        auth_secure_http: str | None = None,
        auth_http_basic: str | None = None,
        auth_ssl_allow_renegotiation: str | None = None,
        auth_src_mac: str | None = None,
        auth_on_demand: str | None = None,
        auth_timeout: int | None = None,
        auth_timeout_type: str | None = None,
        auth_portal_timeout: int | None = None,
        radius_ses_timeout_act: str | None = None,
        auth_blackout_time: int | None = None,
        auth_invalid_max: int | None = None,
        auth_lockout_threshold: int | None = None,
        auth_lockout_duration: int | None = None,
        per_policy_disclaimer: str | None = None,
        auth_ports: list | None = None,
        auth_ssl_min_proto_version: str | None = None,
        auth_ssl_max_proto_version: str | None = None,
        auth_ssl_sigalgs: str | None = None,
        default_user_password_policy: str | None = None,
        cors: str | None = None,
        cors_allowed_origins: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            auth_type: Supported firewall policy authentication protocols/methods. (optional)
            auth_cert: HTTPS server certificate for policy authentication. (optional)
            auth_ca_cert: HTTPS CA certificate for policy authentication. (optional)
            auth_secure_http: Enable/disable redirecting HTTP user authentication to more secure HTTPS. (optional)
            auth_http_basic: Enable/disable use of HTTP basic authentication for identity-based firewall policies. (optional)
            auth_ssl_allow_renegotiation: Allow/forbid SSL re-negotiation for HTTPS authentication. (optional)
            auth_src_mac: Enable/disable source MAC for user identity. (optional)
            auth_on_demand: Always/implicitly trigger firewall authentication on demand. (optional)
            auth_timeout: Time in minutes before the firewall user authentication timeout requires the user to re-authenticate. (optional)
            auth_timeout_type: Control if authenticated users have to login again after a hard timeout, after an idle timeout, or after a session timeout. (optional)
            auth_portal_timeout: Time in minutes before captive portal user have to re-authenticate (1 - 30 min, default 3 min). (optional)
            radius_ses_timeout_act: Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server session timeouts. (optional)
            auth_blackout_time: Time in seconds an IP address is denied access after failing to authenticate five times within one minute. (optional)
            auth_invalid_max: Maximum number of failed authentication attempts before the user is blocked. (optional)
            auth_lockout_threshold: Maximum number of failed login attempts before login lockout is triggered. (optional)
            auth_lockout_duration: Lockout period in seconds after too many login failures. (optional)
            per_policy_disclaimer: Enable/disable per policy disclaimer. (optional)
            auth_ports: Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET. (optional)
            auth_ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). (optional)
            auth_ssl_max_proto_version: Maximum supported protocol version for SSL/TLS connections (default is no limit). (optional)
            auth_ssl_sigalgs: Set signature algorithms related to HTTPS authentication (affects TLS version <= 1.2 only, default is to enable all). (optional)
            default_user_password_policy: Default password policy to apply to all local users unless otherwise specified, as defined in config user password-policy. (optional)
            cors: Enable/disable allowed origins white list for CORS. (optional)
            cors_allowed_origins: Allowed origins white list for CORS. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/user/setting"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if auth_type is not None:
            data_payload['auth-type'] = auth_type
        if auth_cert is not None:
            data_payload['auth-cert'] = auth_cert
        if auth_ca_cert is not None:
            data_payload['auth-ca-cert'] = auth_ca_cert
        if auth_secure_http is not None:
            data_payload['auth-secure-http'] = auth_secure_http
        if auth_http_basic is not None:
            data_payload['auth-http-basic'] = auth_http_basic
        if auth_ssl_allow_renegotiation is not None:
            data_payload['auth-ssl-allow-renegotiation'] = auth_ssl_allow_renegotiation
        if auth_src_mac is not None:
            data_payload['auth-src-mac'] = auth_src_mac
        if auth_on_demand is not None:
            data_payload['auth-on-demand'] = auth_on_demand
        if auth_timeout is not None:
            data_payload['auth-timeout'] = auth_timeout
        if auth_timeout_type is not None:
            data_payload['auth-timeout-type'] = auth_timeout_type
        if auth_portal_timeout is not None:
            data_payload['auth-portal-timeout'] = auth_portal_timeout
        if radius_ses_timeout_act is not None:
            data_payload['radius-ses-timeout-act'] = radius_ses_timeout_act
        if auth_blackout_time is not None:
            data_payload['auth-blackout-time'] = auth_blackout_time
        if auth_invalid_max is not None:
            data_payload['auth-invalid-max'] = auth_invalid_max
        if auth_lockout_threshold is not None:
            data_payload['auth-lockout-threshold'] = auth_lockout_threshold
        if auth_lockout_duration is not None:
            data_payload['auth-lockout-duration'] = auth_lockout_duration
        if per_policy_disclaimer is not None:
            data_payload['per-policy-disclaimer'] = per_policy_disclaimer
        if auth_ports is not None:
            data_payload['auth-ports'] = auth_ports
        if auth_ssl_min_proto_version is not None:
            data_payload['auth-ssl-min-proto-version'] = auth_ssl_min_proto_version
        if auth_ssl_max_proto_version is not None:
            data_payload['auth-ssl-max-proto-version'] = auth_ssl_max_proto_version
        if auth_ssl_sigalgs is not None:
            data_payload['auth-ssl-sigalgs'] = auth_ssl_sigalgs
        if default_user_password_policy is not None:
            data_payload['default-user-password-policy'] = default_user_password_policy
        if cors is not None:
            data_payload['cors'] = cors
        if cors_allowed_origins is not None:
            data_payload['cors-allowed-origins'] = cors_allowed_origins
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
