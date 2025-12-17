"""
FortiOS CMDB - Firewall IP-MAC Binding Table

Configure IP to MAC address pairs in the IP/MAC binding table.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ipmacbinding/table        - List all IP-MAC bindings
    GET    /api/v2/cmdb/firewall.ipmacbinding/table/{seq-num} - Get specific binding
    POST   /api/v2/cmdb/firewall.ipmacbinding/table        - Create new IP-MAC binding
    PUT    /api/v2/cmdb/firewall.ipmacbinding/table/{seq-num} - Update IP-MAC binding
    DELETE /api/v2/cmdb/firewall.ipmacbinding/table/{seq-num} - Delete IP-MAC binding
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class IpmacbindingTable:
    """Firewall IP-MAC binding table endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize IpmacbindingTable endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(
        self,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all IP-MAC binding table entries.

        Args:
            filter: Filter results (e.g., 'status==enable')
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of property names to include
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all IP-MAC bindings
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.list()
            >>> for entry in result['results']:
            ...     print(f"{entry['seq-num']}: {entry['ip']} -> {entry['mac']}")

            >>> # List only enabled bindings
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.list(filter='status==enable')

            >>> # Get first 10 entries
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.list(start=0, count=10)
        """
        params = {}
        param_map = {
            "filter": filter,
            "start": start,
            "count": count,
            "with_meta": with_meta,
            "datasource": datasource,
            "format": format,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "firewall.ipmacbinding/table"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def get(
        self,
        seq_num: int,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get a specific IP-MAC binding entry by sequence number.

        Args:
            seq_num: Entry sequence number
            datasource: Include datasource information
            with_meta: Include metadata
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # Get binding entry 1
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.get(1)
            >>> print(f"IP: {result['results']['ip']}, MAC: {result['results']['mac']}")

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.get(1, with_meta=True)
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = f"firewall.ipmacbinding/table/{encode_path_component(str(seq_num))}"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        seq_num: Optional[int] = None,
        ip: Optional[str] = None,
        mac: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new IP-MAC binding entry.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            seq_num: Entry number (0-4294967295)
            ip: IPv4 address (format: xxx.xxx.xxx.xxx)
            mac: MAC address (format: xx:xx:xx:xx:xx:xx)
            name: Name of the pair (optional, max 35 chars)
            status: Enable/disable this binding ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create a simple IP-MAC binding
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.create(
            ...     seq_num=1,
            ...     ip='192.168.1.100',
            ...     mac='00:11:22:33:44:55'
            ... )

            >>> # Create with name and status
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.create(
            ...     seq_num=2,
            ...     ip='192.168.1.200',
            ...     mac='aa:bb:cc:dd:ee:ff',
            ...     name='server01',
            ...     status='enable'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if seq_num is not None:
                payload_dict["seq-num"] = seq_num
            if ip is not None:
                payload_dict["ip"] = ip
            if mac is not None:
                payload_dict["mac"] = mac
            if name is not None:
                payload_dict["name"] = name
            if status is not None:
                payload_dict["status"] = status

        payload_dict = {
            "seq-num": seq_num,
            "ip": ip,
            "mac": mac,
        }

        param_map = {
            "name": name,
            "status": status,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall.ipmacbinding/table"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        seq_num: Optional[int] = None,
        payload_dict: Optional[Dict[str, Any]] = None,
        ip: Optional[str] = None,
        mac: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update an existing IP-MAC binding entry.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            seq_num: Entry number to update
            ip: IPv4 address (format: xxx.xxx.xxx.xxx)
            mac: MAC address (format: xx:xx:xx:xx:xx:xx)
            name: Name of the pair (optional, max 35 chars)
            status: Enable/disable this binding ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Update IP address
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.update(
            ...     seq_num=1,
            ...     ip='192.168.1.150'
            ... )

            >>> # Update MAC and name
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.update(
            ...     seq_num=2,
            ...     mac='11:22:33:44:55:66',
            ...     name='updated-server'
            ... )

            >>> # Disable a binding
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.update(
            ...     seq_num=3,
            ...     status='disable'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if seq_num is not None:
                payload_dict["seq-num"] = seq_num
            if ip is not None:
                payload_dict["ip"] = ip
            if mac is not None:
                payload_dict["mac"] = mac
            if status is not None:
                payload_dict["status"] = status

        payload_dict = {}

        param_map = {
            "ip": ip,
            "mac": mac,
            "name": name,
            "status": status,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = f"firewall.ipmacbinding/table/{encode_path_component(str(seq_num))}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        seq_num: int,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete an IP-MAC binding entry.

        Args:
            seq_num: Entry number to delete
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete binding entry
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.delete(1)

            >>> # Delete from specific VDOM
            >>> result = fgt.cmdb.firewall.ipmacbinding.table.delete(2, vdom='customer1')
        """
        path = f"firewall.ipmacbinding/table/{encode_path_component(str(seq_num))}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if an IP-MAC binding entry exists.

        Args:
            seq_num: Entry number to check
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if entry exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.ipmacbinding.table.exists(1):
            ...     print("Entry 1 exists")
            ... else:
            ...     print("Entry 1 does not exist")
        """
        try:
            result = self.get(seq_num, vdom=vdom, raw_json=True)
            return result.get("status") == "success"
        except Exception:
            return False
