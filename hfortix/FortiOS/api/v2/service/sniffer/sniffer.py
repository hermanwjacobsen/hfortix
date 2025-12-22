"""
FortiOS SERVICE - Service Sniffer Sniffer

Service endpoint.

API Endpoints:
    GET    /service/sniffer/sniffer

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.service.sniffer.sniffer.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.service.sniffer.sniffer.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from .....http_client_interface import IHTTPClient


class Delete:
    """
    Delete Operations.

    Provides CRUD operations for FortiOS delete configuration.

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

    def post(
        self,
        mkey: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Deletes a packet capture.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: post(param='value')
               2. Payload dict: post(payload_dict={'param': 'value'})

               Args:
                   mkey: Packet capture name.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.delete.post()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.delete.post(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if mkey is not None:
            params["mkey"] = mkey

        params.update(kwargs)

        return self._client.post(
            "service",
            "sniffer/delete/",
            data=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Download:
    """Download resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def post(
        self,
        mkey: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Returns a PCAP file of the packet capture.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: post(param='value')
               2. Payload dict: post(payload_dict={'param': 'value'})

               Args:
                   mkey: Packet Capture name.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.download.post()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.download.post(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if mkey is not None:
            params["mkey"] = mkey

        params.update(kwargs)

        return self._client.post(
            "service",
            "sniffer/download/",
            data=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class List:
    """List resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        mkey: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Returns list of all packet captures and their status information.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   mkey: Filters by packet capture name.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.list.get()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.list.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if mkey is not None:
            params["mkey"] = mkey

        params.update(kwargs)

        return self._client.get(
            "service",
            "sniffer/list/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Meta:
    """Meta resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Returns system limitations & meta information of packet capture feature.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   No parameters
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.meta.get()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.meta.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}

        params.update(kwargs)

        return self._client.get(
            "service",
            "sniffer/meta/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Start:
    """Start resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def post(
        self,
        mkey: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Creates a new packet capture and starts it.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: post(param='value')
               2. Payload dict: post(payload_dict={'param': 'value'})

               Args:
                   mkey: Packet capture name
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.start.post()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.start.post(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if mkey is not None:
            params["mkey"] = mkey

        params.update(kwargs)

        return self._client.post(
            "service",
            "sniffer/start/",
            data=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Stop:
    """Stop resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def post(
        self,
        mkey: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
               Stop a running packet capture.
        Access Group: netgrp.packet-capture

               Supports dual approach:
               1. Individual parameters: post(param='value')
               2. Payload dict: post(payload_dict={'param': 'value'})

               Args:
                   mkey: Packet capture name.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.sniffer.stop.post()

                   # Using payload_dict
                   result = fgt.api.service.sniffer.stop.post(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if mkey is not None:
            params["mkey"] = mkey

        params.update(kwargs)

        return self._client.post(
            "service",
            "sniffer/stop/",
            data=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class Sniffer:
    """Main Sniffer service class"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client
        self._delete = None
        self._download = None
        self._list = None
        self._meta = None
        self._start = None
        self._stop = None

    @property
    def delete(self) -> Delete:
        """Access Delete resource"""
        if self._delete is None:
            self._delete = Delete(self._client)
        return self._delete

    @property
    def download(self) -> Download:
        """Access Download resource"""
        if self._download is None:
            self._download = Download(self._client)
        return self._download

    @property
    def list(self) -> List:
        """Access List resource"""
        if self._list is None:
            self._list = List(self._client)
        return self._list

    @property
    def meta(self) -> Meta:
        """Access Meta resource"""
        if self._meta is None:
            self._meta = Meta(self._client)
        return self._meta

    @property
    def start(self) -> Start:
        """Access Start resource"""
        if self._start is None:
            self._start = Start(self._client)
        return self._start

    @property
    def stop(self) -> Stop:
        """Access Stop resource"""
        if self._stop is None:
            self._stop = Stop(self._client)
        return self._stop
