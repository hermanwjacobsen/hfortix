"""
FortiOS MONITOR - Monitor Firewall Gtp

Monitoring endpoint for monitor firewall gtp data.

API Endpoints:
    GET    /monitor/firewall/gtp

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.gtp.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.gtp.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Flush:
    """
    Flush Operations.

    Provides read-only access for FortiOS flush data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Flush endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        scope: str | None = None,
        gtp_profile: str | None = None,
        version: int | None = None,
        imsi: str | None = None,
        msisdn: str | None = None,
        ms_addr: str | None = None,
        ms_addr6: str | None = None,
        cteid: int | None = None,
        cteid_addr: str | None = None,
        cteid_addr6: str | None = None,
        fteid: int | None = None,
        fteid_addr: str | None = None,
        fteid_addr6: str | None = None,
        apn: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Flush GTP tunnels.

        Args:
            scope: Scope from which to flush tunnels from [global|*vdom].
            (optional)
            gtp_profile: Filter: GTP profile. (optional)
            version: Filter: GTP version. (optional)
            imsi: Filter: International mobile subscriber identity. (optional)
            msisdn: Filter: Mobile station international subscriber directory
            number (optional)
            ms_addr: Filter: Mobile user IP address. (optional)
            ms_addr6: Filter: Mobile user IPv6 address. (optional)
            cteid: Filter: Control plane fully qualified tunnel endpoint
            identifier. (optional)
            cteid_addr: Filter: Control plane TEID IP address. (optional)
            cteid_addr6: Filter: Control plane TEID IPv6 address. (optional)
            fteid: Filter: Data plane fully qualified tunnel endpoint
            identifier. (optional)
            fteid_addr: Filter: Data plane TEID IP address. (optional)
            fteid_addr6: Filter: Data plane TEID IPv6 address. (optional)
            apn: Filter: Access point name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.gtp.flush.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            data["scope"] = scope
        if gtp_profile is not None:
            data["gtp_profile"] = gtp_profile
        if version is not None:
            data["version"] = version
        if imsi is not None:
            data["imsi"] = imsi
        if msisdn is not None:
            data["msisdn"] = msisdn
        if ms_addr is not None:
            data["ms_addr"] = ms_addr
        if ms_addr6 is not None:
            data["ms_addr6"] = ms_addr6
        if cteid is not None:
            data["cteid"] = cteid
        if cteid_addr is not None:
            data["cteid_addr"] = cteid_addr
        if cteid_addr6 is not None:
            data["cteid_addr6"] = cteid_addr6
        if fteid is not None:
            data["fteid"] = fteid
        if fteid_addr is not None:
            data["fteid_addr"] = fteid_addr
        if fteid_addr6 is not None:
            data["fteid_addr6"] = fteid_addr6
        if apn is not None:
            data["apn"] = apn
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/gtp/flush", data=data)


class Gtp:
    """Gtp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Gtp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.flush = Flush(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
                Retrieve a list of GTP tunnels
        Access Group: utmgrp.

                Args:
                    payload_dict: Optional dictionary of parameters
                    raw_json: Return raw JSON response if True
                    **kwargs: Additional parameters as keyword arguments

                Returns:
                    Dictionary containing API response

                Example:
                    >>> fgt.api.monitor.firewall.gtp.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/gtp", params=params)
