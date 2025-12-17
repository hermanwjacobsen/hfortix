"""
FortiOS CMDB - Firewall SSH Host Key
SSH proxy host public keys.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ssh/host-key       - List all host keys
    GET    /api/v2/cmdb/firewall.ssh/host-key/{id}  - Get specific host key
    POST   /api/v2/cmdb/firewall.ssh/host-key       - Create host key
    PUT    /api/v2/cmdb/firewall.ssh/host-key/{id}  - Update host key
    DELETE /api/v2/cmdb/firewall.ssh/host-key/{id}  - Delete host key
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

from .....http_client import HTTPResponse


class HostKey:
    """SSH proxy host key endpoint"""

    def __init__(self, client):
        self._client = client

    def list(
        self,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs,
    ) -> HTTPResponse:
        """
        List all SSH host keys.

        Args:
            filter: Filter results
            range: Range of results (e.g., '0-50')
            sort: Sort results
            format: List of fields to include in response
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # List all host keys
            >>> result = fgt.cmdb.firewall.ssh.host_key.list()

            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.ssh.host_key.list(
            ...     format=['name', 'hostname', 'status']
            ... )
        """
        return self.get(filter=filter, range=range, sort=sort, format=format, vdom=vdom, **kwargs)

    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Get SSH host key(s).

        Args:
            name: Host key name (if retrieving specific key)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get specific host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.get('server1-key')

            >>> # Get all host keys
            >>> result = fgt.cmdb.firewall.ssh.host_key.get()
        """
        path = "firewall.ssh/host-key"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        params = {}
        param_map = {
            "filter": filter,
            "range": range,
            "sort": sort,
            "format": format,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        public_key: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Create an SSH host key.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Host key name (max 35 chars)
            status: Enable/disable host key - 'enable' or 'disable'
            type: Key type - 'RSA' or 'DSA' or 'ECDSA' or 'ED25519'
            hostname: Hostname of the SSH server
            nid: Set the NID for the SSH host
            ip: IP address of the SSH server
            port: Port of the SSH server (1-65535)
            public_key: SSH public key (Base64 encoded)
            usage: Usage - 'transparent-proxy', 'access-proxy'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create SSH host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.create(
            ...     'server1-key',
            ...     hostname='ssh.example.com',
            ...     ip='192.168.1.100',
            ...     port=22,
            ...     type='RSA',
            ...     status='enable'
            ... )

            >>> # Create with public key
            >>> result = fgt.cmdb.firewall.ssh.host_key.create(
            ...     'server2-key',
            ...     hostname='ssh2.example.com',
            ...     public_key='AAAAB3NzaC1yc2EAAAADAQABAAABAQDTest...',
            ...     type='RSA'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if name is not None:
                payload_dict["name"] = name
            if status is not None:
                payload_dict["status"] = status
            if type is not None:
                payload_dict["type"] = type
            if hostname is not None:
                payload_dict["hostname"] = hostname
            if nid is not None:
                payload_dict["nid"] = nid
            if ip is not None:
                payload_dict["ip"] = ip
            if port is not None:
                payload_dict["port"] = port
            if public_key is not None:
                payload_dict["public-key"] = public_key
            if usage is not None:
                payload_dict["usage"] = usage

        return self._client.post(
            "cmdb", "firewall.ssh/host-key", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        public_key: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Update an SSH host key.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Host key name
            status: Enable/disable host key - 'enable' or 'disable'
            type: Key type - 'RSA' or 'DSA' or 'ECDSA' or 'ED25519'
            hostname: Hostname of the SSH server
            nid: Set the NID for the SSH host
            ip: IP address of the SSH server
            port: Port of the SSH server (1-65535)
            public_key: SSH public key (Base64 encoded)
            usage: Usage - 'transparent-proxy', 'access-proxy'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update hostname and port
            >>> result = fgt.cmdb.firewall.ssh.host_key.update(
            ...     'server1-key',
            ...     hostname='newssh.example.com',
            ...     port=2222
            ... )

            >>> # Update status
            >>> result = fgt.cmdb.firewall.ssh.host_key.update(
            ...     'server2-key',
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
            if status is not None:
                payload_dict["status"] = status
            if type is not None:
                payload_dict["type"] = type
            if hostname is not None:
                payload_dict["hostname"] = hostname
            if nid is not None:
                payload_dict["nid"] = nid
            if ip is not None:
                payload_dict["ip"] = ip
            if port is not None:
                payload_dict["port"] = port
            if public_key is not None:
                payload_dict["public-key"] = public_key
            if usage is not None:
                payload_dict["usage"] = usage

        return self._client.put(
            "cmdb", f"firewall.ssh/host-key/{name}", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Delete an SSH host key.

        Args:
            name: Host key name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.delete('server1-key')
        """
        return self._client.delete(
            "cmdb", f"firewall.ssh/host-key/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if SSH host key exists.

        Args:
            name: Host key name
            vdom: Virtual domain

        Returns:
            True if host key exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.ssh.host_key.exists('server1-key'):
            ...     print("Host key exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return (
                result.get("status") == "success"
                and result.get("http_status") == 200
                and len(result.get("results", [])) > 0
            )
        except Exception:
            return False
