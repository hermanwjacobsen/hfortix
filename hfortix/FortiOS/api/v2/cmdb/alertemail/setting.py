"""
FortiOS CMDB - Cmdb Alertemail Setting

Configuration endpoint for managing cmdb alertemail setting objects.

API Endpoints:
    GET    /cmdb/alertemail/setting
    PUT    /cmdb/alertemail/setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.alertemail.setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.alertemail.setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.alertemail.setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.alertemail.setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.alertemail.setting.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

from collections.abc import Coroutine


class Setting:
    """
    Setting Operations.

    Provides CRUD operations for FortiOS setting configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/alertemail/setting"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        username: str | None = None,
        mailto1: str | None = None,
        mailto2: str | None = None,
        mailto3: str | None = None,
        filter_mode: str | None = None,
        email_interval: int | None = None,
        IPS_logs: str | None = None,
        firewall_authentication_failure_logs: str | None = None,
        HA_logs: str | None = None,
        IPsec_errors_logs: str | None = None,
        FDS_update_logs: str | None = None,
        PPP_errors_logs: str | None = None,
        antivirus_logs: str | None = None,
        webfilter_logs: str | None = None,
        configuration_changes_logs: str | None = None,
        violation_traffic_logs: str | None = None,
        admin_login_logs: str | None = None,
        FDS_license_expiring_warning: str | None = None,
        log_disk_usage_warning: str | None = None,
        fortiguard_log_quota_warning: str | None = None,
        amc_interface_bypass_mode: str | None = None,
        FIPS_CC_errors: str | None = None,
        FSSO_disconnect_logs: str | None = None,
        ssh_logs: str | None = None,
        local_disk_usage: int | None = None,
        emergency_interval: int | None = None,
        alert_interval: int | None = None,
        critical_interval: int | None = None,
        error_interval: int | None = None,
        warning_interval: int | None = None,
        notification_interval: int | None = None,
        information_interval: int | None = None,
        debug_interval: int | None = None,
        severity: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            username: Name that appears in the From: field of alert emails
            (max. 63 characters). (optional)
            mailto1: Email address to send alert email to (usually a system
            administrator) (max. 63 characters). (optional)
            mailto2: Optional second email address to send alert email to (max.
            63 characters). (optional)
            mailto3: Optional third email address to send alert email to (max.
            63 characters). (optional)
            filter_mode: How to filter log messages that are sent to alert
            emails. (optional)
            email_interval: Interval between sending alert emails (1 - 99999
            min, default = 5). (optional)
            IPS_logs: Enable/disable IPS logs in alert email. (optional)
            firewall_authentication_failure_logs: Enable/disable firewall
            authentication failure logs in alert email. (optional)
            HA_logs: Enable/disable HA logs in alert email. (optional)
            IPsec_errors_logs: Enable/disable IPsec error logs in alert email.
            (optional)
            FDS_update_logs: Enable/disable FortiGuard update logs in alert
            email. (optional)
            PPP_errors_logs: Enable/disable PPP error logs in alert email.
            (optional)
            antivirus_logs: Enable/disable antivirus logs in alert email.
            (optional)
            webfilter_logs: Enable/disable web filter logs in alert email.
            (optional)
            configuration_changes_logs: Enable/disable configuration change
            logs in alert email. (optional)
            violation_traffic_logs: Enable/disable violation traffic logs in
            alert email. (optional)
            admin_login_logs: Enable/disable administrator login/logout logs in
            alert email. (optional)
            FDS_license_expiring_warning: Enable/disable FortiGuard license
            expiration warnings in alert email. (optional)
            log_disk_usage_warning: Enable/disable disk usage warnings in alert
            email. (optional)
            fortiguard_log_quota_warning: Enable/disable FortiCloud log quota
            warnings in alert email. (optional)
            amc_interface_bypass_mode: Enable/disable Fortinet Advanced
            Mezzanine Card (AMC) interface bypass mode logs in alert email.
            (optional)
            FIPS_CC_errors: Enable/disable FIPS and Common Criteria error logs
            in alert email. (optional)
            FSSO_disconnect_logs: Enable/disable logging of FSSO collector
            agent disconnect. (optional)
            ssh_logs: Enable/disable SSH logs in alert email. (optional)
            local_disk_usage: Disk usage percentage at which to send alert
            email (1 - 99 percent, default = 75). (optional)
            emergency_interval: Emergency alert interval in minutes. (optional)
            alert_interval: Alert alert interval in minutes. (optional)
            critical_interval: Critical alert interval in minutes. (optional)
            error_interval: Error alert interval in minutes. (optional)
            warning_interval: Warning alert interval in minutes. (optional)
            notification_interval: Notification alert interval in minutes.
            (optional)
            information_interval: Information alert interval in minutes.
            (optional)
            debug_interval: Debug alert interval in minutes. (optional)
            severity: Lowest severity level to log. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/alertemail/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if username is not None:
            data_payload["username"] = username
        if mailto1 is not None:
            data_payload["mailto1"] = mailto1
        if mailto2 is not None:
            data_payload["mailto2"] = mailto2
        if mailto3 is not None:
            data_payload["mailto3"] = mailto3
        if filter_mode is not None:
            data_payload["filter-mode"] = filter_mode
        if email_interval is not None:
            data_payload["email-interval"] = email_interval
        if IPS_logs is not None:
            data_payload["IPS-logs"] = IPS_logs
        if firewall_authentication_failure_logs is not None:
            data_payload["firewall-authentication-failure-logs"] = (
                firewall_authentication_failure_logs
            )
        if HA_logs is not None:
            data_payload["HA-logs"] = HA_logs
        if IPsec_errors_logs is not None:
            data_payload["IPsec-errors-logs"] = IPsec_errors_logs
        if FDS_update_logs is not None:
            data_payload["FDS-update-logs"] = FDS_update_logs
        if PPP_errors_logs is not None:
            data_payload["PPP-errors-logs"] = PPP_errors_logs
        if antivirus_logs is not None:
            data_payload["antivirus-logs"] = antivirus_logs
        if webfilter_logs is not None:
            data_payload["webfilter-logs"] = webfilter_logs
        if configuration_changes_logs is not None:
            data_payload["configuration-changes-logs"] = (
                configuration_changes_logs
            )
        if violation_traffic_logs is not None:
            data_payload["violation-traffic-logs"] = violation_traffic_logs
        if admin_login_logs is not None:
            data_payload["admin-login-logs"] = admin_login_logs
        if FDS_license_expiring_warning is not None:
            data_payload["FDS-license-expiring-warning"] = (
                FDS_license_expiring_warning
            )
        if log_disk_usage_warning is not None:
            data_payload["log-disk-usage-warning"] = log_disk_usage_warning
        if fortiguard_log_quota_warning is not None:
            data_payload["fortiguard-log-quota-warning"] = (
                fortiguard_log_quota_warning
            )
        if amc_interface_bypass_mode is not None:
            data_payload["amc-interface-bypass-mode"] = (
                amc_interface_bypass_mode
            )
        if FIPS_CC_errors is not None:
            data_payload["FIPS-CC-errors"] = FIPS_CC_errors
        if FSSO_disconnect_logs is not None:
            data_payload["FSSO-disconnect-logs"] = FSSO_disconnect_logs
        if ssh_logs is not None:
            data_payload["ssh-logs"] = ssh_logs
        if local_disk_usage is not None:
            data_payload["local-disk-usage"] = local_disk_usage
        if emergency_interval is not None:
            data_payload["emergency-interval"] = emergency_interval
        if alert_interval is not None:
            data_payload["alert-interval"] = alert_interval
        if critical_interval is not None:
            data_payload["critical-interval"] = critical_interval
        if error_interval is not None:
            data_payload["error-interval"] = error_interval
        if warning_interval is not None:
            data_payload["warning-interval"] = warning_interval
        if notification_interval is not None:
            data_payload["notification-interval"] = notification_interval
        if information_interval is not None:
            data_payload["information-interval"] = information_interval
        if debug_interval is not None:
            data_payload["debug-interval"] = debug_interval
        if severity is not None:
            data_payload["severity"] = severity
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
