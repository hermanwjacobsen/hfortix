"""
FortiOS CMDB - Antivirus Quarantine
Configure quarantine options

API Endpoints:
    GET  /antivirus/quarantine - Get quarantine settings
    PUT  /antivirus/quarantine - Update quarantine settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Quarantine:
    """Antivirus Quarantine endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(
        self,
        vdom: Optional[Union[str, bool]] = None,
        # Query parameters
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        GET /antivirus/quarantine
        Get quarantine settings

        Args:
            vdom: Virtual domain (optional)

            Query parameters (all optional):
            datasource: Include datasource information for each linked object
            with_meta: Include meta information about each object
            skip: Enable CLI skip operator to hide skipped properties
            action: Special actions (default, schema, revision)
            **kwargs: Any additional parameters

        Returns:
            Quarantine configuration

        Examples:
            >>> # Get quarantine settings
            >>> settings = fgt.cmdb.antivirus.quarantine.get()

            >>> # Get with meta information
            >>> settings = fgt.cmdb.antivirus.quarantine.get(with_meta=True)
        """
        # Build params dict from provided parameters
        params = {}

        # Map parameters
        param_map = {
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'action': action,
        }

        # Add non-None parameters
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any extra kwargs
        params.update(kwargs)

        return self._client.get('cmdb', 'antivirus/quarantine', params=params if params else None, vdom=vdom)

    def update(
        self,
        agelimit: Optional[int] = None,
        maxfilesize: Optional[int] = None,
        quarantine_quota: Optional[int] = None,
        drop_infected: Optional[str] = None,
        store_infected: Optional[str] = None,
        drop_blocked: Optional[str] = None,
        store_blocked: Optional[str] = None,
        drop_heuristic: Optional[str] = None,
        store_heuristic: Optional[str] = None,
        drop_machine_learning: Optional[str] = None,
        store_machine_learning: Optional[str] = None,
        lowspace: Optional[str] = None,
        destination: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        PUT /antivirus/quarantine
        Update quarantine settings

        Args:
            agelimit: Age limit for quarantined files (0 = unlimited, 1-479 days)
            maxfilesize: Maximum file size to quarantine (0 = unlimited, 1-500 MB)
            quarantine_quota: Quarantine quota (0 = unlimited, 1-4096 MB)
            drop_infected: Do not quarantine infected files found in sessions using the selected protocols - 'imap', 'smtp', 'pop3', 'http', 'ftp', 'nntp', 'imaps', 'smtps', 'pop3s', 'ftps', 'mapi', 'cifs', 'ssh'
            store_infected: Quarantine infected files found in sessions using the selected protocols - same options as drop_infected
            drop_blocked: Do not quarantine files blocked by FortiGuard - same protocol options
            store_blocked: Quarantine files blocked by FortiGuard - same protocol options
            drop_heuristic: Do not quarantine files detected by heuristics - same protocol options
            store_heuristic: Quarantine files detected by heuristics - same protocol options
            drop_machine_learning: Do not quarantine files detected by machine learning - same protocol options
            store_machine_learning: Quarantine files detected by machine learning - same protocol options
            lowspace: Low space action - 'drop-new' or 'ovrw-old'
            destination: Quarantine destination - 'NULL', 'disk', 'FortiAnalyzer'
            vdom: Virtual domain (optional)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Set age limit and max file size
            >>> fgt.cmdb.antivirus.quarantine.update(
            ...     agelimit=30,
            ...     maxfilesize=50,
            ...     quarantine_quota=1024
            ... )

            >>> # Configure storage options
            >>> fgt.cmdb.antivirus.quarantine.update(
            ...     store_infected='imap smtp pop3 http',
            ...     drop_blocked='ftp',
            ...     lowspace='ovrw-old'
            ... )

            >>> # Set destination
            >>> fgt.cmdb.antivirus.quarantine.update(
            ...     destination='disk',
            ...     quarantine_quota=2048
            ... )
        """
        # Build data dict from provided parameters
        data = {}

        # Map Python parameter names to API field names
        param_map = {
            'agelimit': agelimit,
            'maxfilesize': maxfilesize,
            'quarantine_quota': quarantine_quota,
            'drop_infected': drop_infected,
            'store_infected': store_infected,
            'drop_blocked': drop_blocked,
            'store_blocked': store_blocked,
            'drop_heuristic': drop_heuristic,
            'store_heuristic': store_heuristic,
            'drop_machine_learning': drop_machine_learning,
            'store_machine_learning': store_machine_learning,
            'lowspace': lowspace,
            'destination': destination,
        }

        # API field name mapping
        api_field_map = {
            'agelimit': 'agelimit',
            'maxfilesize': 'maxfilesize',
            'quarantine_quota': 'quarantine-quota',
            'drop_infected': 'drop-infected',
            'store_infected': 'store-infected',
            'drop_blocked': 'drop-blocked',
            'store_blocked': 'store-blocked',
            'drop_heuristic': 'drop-heuristic',
            'store_heuristic': 'store-heuristic',
            'drop_machine_learning': 'drop-machine-learning',
            'store_machine_learning': 'store-machine-learning',
            'lowspace': 'lowspace',
            'destination': 'destination',
        }

        # Add non-None parameters
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        # Add any extra kwargs
        data.update(kwargs)

        return self._client.put('cmdb', 'antivirus/quarantine', data, vdom=vdom)
