"""
FortiOS Service API - Security Rating

Retrieve Security Rating reports and recommendations for security posture analysis.

API Endpoints:
    GET /security-rating/report/           - Get full Security Rating report
    GET /security-rating/recommendations/  - Get recommendations for specific checks
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SecurityRating:
    """Security Rating service endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def report(
        self,
        type: str,
        scope: Optional[str] = None,
        standalone: Optional[str] = None,
        checks: Optional[str] = None,
        show_hidden: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve full report of all Security Rating tests

        Get comprehensive security rating report with all checks and their results
        across the Security Fabric. Supports filtering by type, checks, and scope.

        Args:
            type (str, required): Report sub-type to fetch
                Valid values: 'psirt', 'insight'
            scope (str, optional): Scope of the request
                Valid values: 'global', 'vdom*'
            standalone (str, optional): Only return report for current FortiGate
                Valid values: 'true', 'false'
            checks (str, optional): Comma-separated list of specific Security Rating checks
                Example: 'check1,check2,check3'
            show_hidden (str, optional): Show hidden Security Rating controls
                Valid values: 'true', 'false'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response with Security Rating report

        Response fields:
            - check (str): ID of the Security Rating check
            - title (str): Translation string for check title
            - description (str): Translation string for check description
            - severity (str): Severity level - 'none', 'low', 'medium', 'high', 'critical'
            - customMetadata (object): Custom metadata for the check
            - summary (array): Summary details per device/VDOM
                - device (str): Device serial number or name
                - deviceType (str): Type of device
                - vdom (str): Virtual domain name
                - scope (str): Scope of the check
                - issueCount (int): Number of issues found
                - result (str): Check result
                - timestamp (int): Unix timestamp

        Examples:
            >>> # Get PSIRT security rating report
            >>> report = fgt.service.security_rating.report(type='psirt')
            >>> print(f"Total checks: {len(report['results'])}")

            >>> # Get insight report for current FortiGate only
            >>> report = fgt.service.security_rating.report(
            ...     type='insight',
            ...     standalone='true'
            ... )

            >>> # Get specific checks with hidden controls
            >>> report = fgt.service.security_rating.report(
            ...     type='psirt',
            ...     checks='check1,check2',
            ...     show_hidden='true'
            ... )

            >>> # Get report for specific VDOM
            >>> report = fgt.service.security_rating.report(
            ...     type='insight',
            ...     scope='vdom',
            ...     vdom='root'
            ... )
        """
        params = {"type": type}

        param_map = {
            "scope": scope,
            "standalone": standalone,
            "checks": checks,
            "show-hidden": show_hidden,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "service", "security-rating/report/", params=params, vdom=vdom, raw_json=raw_json
        )

    def recommendations(
        self,
        checks: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve recommendations for Security Rating tests

        Get detailed recommendations for specific Security Rating checks. This provides
        actionable guidance on how to resolve security issues identified in the report.

        Args:
            checks (str, required): Comma-separated list of Security Rating check IDs
                Example: 'check1,check2,check3'
            scope (str, optional): Scope of the request
                Valid values: 'global', 'vdom*'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response with recommendations

        Response fields:
            - check (str): ID of the Security Rating check
            - summary (array): Summary for each device in Security Fabric
                - device (str): Device serial number or name
                - deviceType (str): Type of device
                - vdom (str): Virtual domain name
                - scope (str): Scope of the check
                - recommendations (array): List of recommendations
                    - title (str): Recommendation title
                    - description (str): Detailed recommendation
                    - action (str): Suggested action to take

        Examples:
            >>> # Get recommendations for specific checks
            >>> recs = fgt.service.security_rating.recommendations(
            ...     checks='admin-password-policy,tls-version'
            ... )
            >>>
            >>> for check in recs['results']:
            ...     print(f"Check: {check['check']}")
            ...     for summary in check.get('summary', []):
            ...         print(f"  Device: {summary['device']}")
            ...         for rec in summary.get('recommendations', []):
            ...             print(f"    - {rec.get('title')}")

            >>> # Get recommendations for specific VDOM
            >>> recs = fgt.service.security_rating.recommendations(
            ...     checks='check1',
            ...     scope='vdom',
            ...     vdom='root'
            ... )

            >>> # Get global recommendations
            >>> recs = fgt.service.security_rating.recommendations(
            ...     checks='psirt-check1,psirt-check2',
            ...     scope='global'
            ... )
        """
        params = {"checks": checks}

        param_map = {"scope": scope}

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "service",
            "security-rating/recommendations/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )
