"""
FortiOS CMDB - Cmdb Wireless Controller Hotspot20 H2qp Conn Capability

Configuration endpoint for managing cmdb wireless controller hotspot20 h2qp
conn capability objects.

API Endpoints:
    GET    /cmdb/wireless-controller/hotspot20_h2qp_conn_capability
    POST   /cmdb/wireless-controller/hotspot20_h2qp_conn_capability
    GET    /cmdb/wireless-controller/hotspot20_h2qp_conn_capability
    PUT /cmdb/wireless-controller/hotspot20_h2qp_conn_capability/{identifier}
    DELETE
    /cmdb/wireless-controller/hotspot20_h2qp_conn_capability/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_conn_capability.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_conn_capability.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_conn_capability.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_conn_capability.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_conn_capability.delete(name="item_name")

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


class Hotspot20H2qpConnCapability:
    """
    Hotspot20H2Qpconncapability Operations.

    Provides CRUD operations for FortiOS hotspot20h2qpconncapability
    configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Hotspot20H2qpConnCapability endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = (
                f"/wireless-controller.hotspot20/h2qp-conn-capability/{name}"
            )
        else:
            endpoint = "/wireless-controller.hotspot20/h2qp-conn-capability"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        icmp_port: str | None = None,
        ftp_port: str | None = None,
        ssh_port: str | None = None,
        http_port: str | None = None,
        tls_port: str | None = None,
        pptp_vpn_port: str | None = None,
        voip_tcp_port: str | None = None,
        voip_udp_port: str | None = None,
        ikev2_port: str | None = None,
        ikev2_xx_port: str | None = None,
        esp_port: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: Connection capability name. (optional)
            icmp_port: Set ICMP port service status. (optional)
            ftp_port: Set FTP port service status. (optional)
            ssh_port: Set SSH port service status. (optional)
            http_port: Set HTTP port service status. (optional)
            tls_port: Set TLS VPN (HTTPS) port service status. (optional)
            pptp_vpn_port: Set Point to Point Tunneling Protocol (PPTP) VPN
            port service status. (optional)
            voip_tcp_port: Set VoIP TCP port service status. (optional)
            voip_udp_port: Set VoIP UDP port service status. (optional)
            ikev2_port: Set IKEv2 port service for IPsec VPN status. (optional)
            ikev2_xx_port: Set UDP port 4500 (which may be used by IKEv2 for
            IPsec VPN) service status. (optional)
            esp_port: Set ESP port service (used by IPsec VPNs) status.
            (optional)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = (
            f"/wireless-controller.hotspot20/h2qp-conn-capability/{name}"
        )
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if icmp_port is not None:
            data_payload["icmp-port"] = icmp_port
        if ftp_port is not None:
            data_payload["ftp-port"] = ftp_port
        if ssh_port is not None:
            data_payload["ssh-port"] = ssh_port
        if http_port is not None:
            data_payload["http-port"] = http_port
        if tls_port is not None:
            data_payload["tls-port"] = tls_port
        if pptp_vpn_port is not None:
            data_payload["pptp-vpn-port"] = pptp_vpn_port
        if voip_tcp_port is not None:
            data_payload["voip-tcp-port"] = voip_tcp_port
        if voip_udp_port is not None:
            data_payload["voip-udp-port"] = voip_udp_port
        if ikev2_port is not None:
            data_payload["ikev2-port"] = ikev2_port
        if ikev2_xx_port is not None:
            data_payload["ikev2-xx-port"] = ikev2_xx_port
        if esp_port is not None:
            data_payload["esp-port"] = esp_port
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = (
            f"/wireless-controller.hotspot20/h2qp-conn-capability/{name}"
        )
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        icmp_port: str | None = None,
        ftp_port: str | None = None,
        ssh_port: str | None = None,
        http_port: str | None = None,
        tls_port: str | None = None,
        pptp_vpn_port: str | None = None,
        voip_tcp_port: str | None = None,
        voip_udp_port: str | None = None,
        ikev2_port: str | None = None,
        ikev2_xx_port: str | None = None,
        esp_port: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: Connection capability name. (optional)
            icmp_port: Set ICMP port service status. (optional)
            ftp_port: Set FTP port service status. (optional)
            ssh_port: Set SSH port service status. (optional)
            http_port: Set HTTP port service status. (optional)
            tls_port: Set TLS VPN (HTTPS) port service status. (optional)
            pptp_vpn_port: Set Point to Point Tunneling Protocol (PPTP) VPN
            port service status. (optional)
            voip_tcp_port: Set VoIP TCP port service status. (optional)
            voip_udp_port: Set VoIP UDP port service status. (optional)
            ikev2_port: Set IKEv2 port service for IPsec VPN status. (optional)
            ikev2_xx_port: Set UDP port 4500 (which may be used by IKEv2 for
            IPsec VPN) service status. (optional)
            esp_port: Set ESP port service (used by IPsec VPNs) status.
            (optional)
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
        endpoint = "/wireless-controller.hotspot20/h2qp-conn-capability"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if icmp_port is not None:
            data_payload["icmp-port"] = icmp_port
        if ftp_port is not None:
            data_payload["ftp-port"] = ftp_port
        if ssh_port is not None:
            data_payload["ssh-port"] = ssh_port
        if http_port is not None:
            data_payload["http-port"] = http_port
        if tls_port is not None:
            data_payload["tls-port"] = tls_port
        if pptp_vpn_port is not None:
            data_payload["pptp-vpn-port"] = pptp_vpn_port
        if voip_tcp_port is not None:
            data_payload["voip-tcp-port"] = voip_tcp_port
        if voip_udp_port is not None:
            data_payload["voip-udp-port"] = voip_udp_port
        if ikev2_port is not None:
            data_payload["ikev2-port"] = ikev2_port
        if ikev2_xx_port is not None:
            data_payload["ikev2-xx-port"] = ikev2_xx_port
        if esp_port is not None:
            data_payload["esp-port"] = esp_port
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
