"""
FortiOS SERVICE - Service Security Rating Security Rating

Service endpoint.

API Endpoints:
    GET    /service/security_rating/security_rating

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.service.security_rating.security_rating.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.service.security_rating.security_rating.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Recommendations:
    """
    Recommendations Operations.

    Provides CRUD operations for FortiOS recommendations configuration.

    Methods:
        get(): Retrieve configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        checks: str,
        scope: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
               Retrieve recommendations for Security Rating tests.
        Access Group: secfabgrp.csfsys

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   checks: Retrieve the recommendations for the given Security
                   Rating checks.
                   scope: Scope of the request [global | vdom*].
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass
                   all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result =
                   fgt.api.service.security-rating.recommendations.get()

                   # Using payload_dict
                   result =
                   fgt.api.service.security-rating.recommendations.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if checks is not None:
            params["checks"] = checks
        if scope is not None:
            params["scope"] = scope

        params.update(kwargs)

        return self._client.get(
            "service",
            "security-rating/recommendations/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Report:
    """Report resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        type: str,
        scope: Optional[str] = None,
        standalone: Optional[str] = None,
        checks: Optional[str] = None,
        show_hidden: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
               Retrieve full report of all Security Rating tests.
        Access Group: secfabgrp.csfsys

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   type: The report sub-type to fetch ['psirt', 'insight'].
                   scope: Scope of the request [global | vdom*].
                   standalone: If enabled this will only return a report with
                   checks for the current FortiGate.
                   checks: Retrieve a report with only the given Security
                   Rating checks.
                   show_hidden: Show hidden Security Rating controls in the
                   report.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass
                   all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.security-rating.report.get()

                   # Using payload_dict
                   result = fgt.api.service.security-rating.report.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if type is not None:
            params["type"] = type
        if scope is not None:
            params["scope"] = scope
        if standalone is not None:
            params["standalone"] = standalone
        if checks is not None:
            params["checks"] = checks
        if show_hidden is not None:
            params["show-hidden"] = show_hidden

        params.update(kwargs)

        return self._client.get(
            "service",
            "security-rating/report/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class SecurityRating:
    """Main Security Rating service class"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client
        self._recommendations: Recommendations | None = None
        self._report: Report | None = None

    @property
    def recommendations(self) -> Recommendations:
        """Access Recommendations resource"""
        if self._recommendations is None:
            self._recommendations = Recommendations(self._client)
        return self._recommendations

    @property
    def report(self) -> Report:
        """Access Report resource"""
        if self._report is None:
            self._report = Report(self._client)
        return self._report
