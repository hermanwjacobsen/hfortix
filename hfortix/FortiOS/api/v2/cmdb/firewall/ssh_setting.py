"""
FortiOS CMDB - Firewall SSH Settings
SSH proxy settings.

API Endpoints:
    GET  /api/v2/cmdb/firewall.ssh/setting  - Get configuration
    PUT  /api/v2/cmdb/firewall.ssh/setting  - Update configuration
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

from .....http_client import HTTPResponse


class Setting:
    """SSH proxy settings endpoint (singleton)"""

    def __init__(self, client):
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Get SSH proxy settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable skip operator
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get SSH proxy settings
            >>> result = fgt.cmdb.firewall.ssh.setting.get()

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.ssh.setting.get(with_meta=True)
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get(
            "cmdb",
            "firewall.ssh/setting",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        caname: Optional[str] = None,
        untrusted_caname: Optional[str] = None,
        host_trusted_checking: Optional[str] = None,
        hostkey_rsa2048: Optional[str] = None,
        hostkey_dsa1024: Optional[str] = None,
        hostkey_ecdsa256: Optional[str] = None,
        hostkey_ecdsa384: Optional[str] = None,
        hostkey_ecdsa521: Optional[str] = None,
        hostkey_ed25519: Optional[str] = None,
        ssh_policy_check: Optional[str] = None,
        ssh_tun_policy_check: Optional[str] = None,
        log_violation: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> HTTPResponse:
        """
        Update SSH proxy settings.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            caname: CA certificate name
            untrusted_caname: Untrusted CA certificate name
            host_trusted_checking: Enable/disable host trusted checking - 'enable' or 'disable'
            hostkey_rsa2048: RSA 2048-bit host key name
            hostkey_dsa1024: DSA 1024-bit host key name
            hostkey_ecdsa256: ECDSA 256-bit host key name
            hostkey_ecdsa384: ECDSA 384-bit host key name
            hostkey_ecdsa521: ECDSA 521-bit host key name
            hostkey_ed25519: ED25519 host key name
            ssh_policy_check: Enable/disable SSH policy check - 'enable' or 'disable'
            ssh_tun_policy_check: Enable/disable SSH tunnel policy check - 'enable' or 'disable'
            log_violation: Enable/disable logging of violations - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # PUT - Update CA certificate
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     caname='Fortinet_CA_SSL',
            ...     host_trusted_checking='enable'
            ... )

            >>> # Enable SSH policy check
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     ssh_policy_check='enable',
            ...     log_violation='enable'
            ... )

            >>> # Configure host keys
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     hostkey_rsa2048='rsa-key-2048',
            ...     hostkey_ecdsa256='ecdsa-key-256'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if caname is not None:
                payload_dict["caname"] = caname
            if untrusted_caname is not None:
                payload_dict["untrusted-caname"] = untrusted_caname
            if host_trusted_checking is not None:
                payload_dict["host-trusted-checking"] = host_trusted_checking
            if hostkey_rsa2048 is not None:
                payload_dict["hostkey-rsa2048"] = hostkey_rsa2048
            if hostkey_dsa1024 is not None:
                payload_dict["hostkey-dsa1024"] = hostkey_dsa1024
            if hostkey_ecdsa256 is not None:
                payload_dict["hostkey-ecdsa256"] = hostkey_ecdsa256
            if hostkey_ecdsa384 is not None:
                payload_dict["hostkey-ecdsa384"] = hostkey_ecdsa384
            if hostkey_ecdsa521 is not None:
                payload_dict["hostkey-ecdsa521"] = hostkey_ecdsa521
            if hostkey_ed25519 is not None:
                payload_dict["hostkey-ed25519"] = hostkey_ed25519
            if ssh_policy_check is not None:
                payload_dict["ssh-policy-check"] = ssh_policy_check
            if ssh_tun_policy_check is not None:
                payload_dict["ssh-tun-policy-check"] = ssh_tun_policy_check
            if log_violation is not None:
                payload_dict["log-violation"] = log_violation

        return self._client.put(
            "cmdb", "firewall.ssh/setting", payload_dict, vdom=vdom, raw_json=raw_json
        )
