"""
FortiOS CMDB - Cmdb Log Setting

Configuration endpoint for managing cmdb log setting objects.

API Endpoints:
    GET    /cmdb/log/setting
    PUT    /cmdb/log/setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.log.setting.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


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
        endpoint = "/log/setting"
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
        resolve_ip: str | None = None,
        resolve_port: str | None = None,
        log_user_in_upper: str | None = None,
        fwpolicy_implicit_log: str | None = None,
        fwpolicy6_implicit_log: str | None = None,
        extended_log: str | None = None,
        local_in_allow: str | None = None,
        local_in_deny_unicast: str | None = None,
        local_in_deny_broadcast: str | None = None,
        local_in_policy_log: str | None = None,
        local_out: str | None = None,
        local_out_ioc_detection: str | None = None,
        daemon_log: str | None = None,
        neighbor_event: str | None = None,
        brief_traffic_format: str | None = None,
        user_anonymize: str | None = None,
        expolicy_implicit_log: str | None = None,
        log_policy_comment: str | None = None,
        faz_override: str | None = None,
        syslog_override: str | None = None,
        rest_api_set: str | None = None,
        rest_api_get: str | None = None,
        rest_api_performance: str | None = None,
        long_live_session_stat: str | None = None,
        extended_utm_log: str | None = None,
        zone_name: str | None = None,
        web_svc_perf: str | None = None,
        custom_log_fields: list | None = None,
        anonymization_hash: str | None = None,
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
            resolve_ip: Enable/disable adding resolved domain names to traffic
            logs if possible. (optional)
            resolve_port: Enable/disable adding resolved service names to
            traffic logs. (optional)
            log_user_in_upper: Enable/disable logs with user-in-upper.
            (optional)
            fwpolicy_implicit_log: Enable/disable implicit firewall policy
            logging. (optional)
            fwpolicy6_implicit_log: Enable/disable implicit firewall policy6
            logging. (optional)
            extended_log: Enable/disable extended traffic logging. (optional)
            local_in_allow: Enable/disable local-in-allow logging. (optional)
            local_in_deny_unicast: Enable/disable local-in-deny-unicast
            logging. (optional)
            local_in_deny_broadcast: Enable/disable local-in-deny-broadcast
            logging. (optional)
            local_in_policy_log: Enable/disable local-in-policy logging.
            (optional)
            local_out: Enable/disable local-out logging. (optional)
            local_out_ioc_detection: Enable/disable local-out traffic IoC
            detection. Requires local-out to be enabled. (optional)
            daemon_log: Enable/disable daemon logging. (optional)
            neighbor_event: Enable/disable neighbor event logging. (optional)
            brief_traffic_format: Enable/disable brief format traffic logging.
            (optional)
            user_anonymize: Enable/disable anonymizing user names in log
            messages. (optional)
            expolicy_implicit_log: Enable/disable proxy firewall implicit
            policy logging. (optional)
            log_policy_comment: Enable/disable inserting policy comments into
            traffic logs. (optional)
            faz_override: Enable/disable override FortiAnalyzer settings.
            (optional)
            syslog_override: Enable/disable override Syslog settings.
            (optional)
            rest_api_set: Enable/disable REST API POST/PUT/DELETE request
            logging. (optional)
            rest_api_get: Enable/disable REST API GET request logging.
            (optional)
            rest_api_performance: Enable/disable REST API memory and
            performance stats in rest-api-get/set logs. (optional)
            long_live_session_stat: Enable/disable long-live-session statistics
            logging. (optional)
            extended_utm_log: Enable/disable extended UTM logging. (optional)
            zone_name: Enable/disable zone name logging. (optional)
            web_svc_perf: Enable/disable web-svc performance logging.
            (optional)
            custom_log_fields: Custom fields to append to all log messages.
            (optional)
            anonymization_hash: User name anonymization hash salt. (optional)
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
        endpoint = "/log/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if resolve_ip is not None:
            data_payload["resolve-ip"] = resolve_ip
        if resolve_port is not None:
            data_payload["resolve-port"] = resolve_port
        if log_user_in_upper is not None:
            data_payload["log-user-in-upper"] = log_user_in_upper
        if fwpolicy_implicit_log is not None:
            data_payload["fwpolicy-implicit-log"] = fwpolicy_implicit_log
        if fwpolicy6_implicit_log is not None:
            data_payload["fwpolicy6-implicit-log"] = fwpolicy6_implicit_log
        if extended_log is not None:
            data_payload["extended-log"] = extended_log
        if local_in_allow is not None:
            data_payload["local-in-allow"] = local_in_allow
        if local_in_deny_unicast is not None:
            data_payload["local-in-deny-unicast"] = local_in_deny_unicast
        if local_in_deny_broadcast is not None:
            data_payload["local-in-deny-broadcast"] = local_in_deny_broadcast
        if local_in_policy_log is not None:
            data_payload["local-in-policy-log"] = local_in_policy_log
        if local_out is not None:
            data_payload["local-out"] = local_out
        if local_out_ioc_detection is not None:
            data_payload["local-out-ioc-detection"] = local_out_ioc_detection
        if daemon_log is not None:
            data_payload["daemon-log"] = daemon_log
        if neighbor_event is not None:
            data_payload["neighbor-event"] = neighbor_event
        if brief_traffic_format is not None:
            data_payload["brief-traffic-format"] = brief_traffic_format
        if user_anonymize is not None:
            data_payload["user-anonymize"] = user_anonymize
        if expolicy_implicit_log is not None:
            data_payload["expolicy-implicit-log"] = expolicy_implicit_log
        if log_policy_comment is not None:
            data_payload["log-policy-comment"] = log_policy_comment
        if faz_override is not None:
            data_payload["faz-override"] = faz_override
        if syslog_override is not None:
            data_payload["syslog-override"] = syslog_override
        if rest_api_set is not None:
            data_payload["rest-api-set"] = rest_api_set
        if rest_api_get is not None:
            data_payload["rest-api-get"] = rest_api_get
        if rest_api_performance is not None:
            data_payload["rest-api-performance"] = rest_api_performance
        if long_live_session_stat is not None:
            data_payload["long-live-session-stat"] = long_live_session_stat
        if extended_utm_log is not None:
            data_payload["extended-utm-log"] = extended_utm_log
        if zone_name is not None:
            data_payload["zone-name"] = zone_name
        if web_svc_perf is not None:
            data_payload["web-svc-per"] = web_svc_perf
        if custom_log_fields is not None:
            data_payload["custom-log-fields"] = custom_log_fields
        if anonymization_hash is not None:
            data_payload["anonymization-hash"] = anonymization_hash
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
