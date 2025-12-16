"""
FortiOS CMDB - Antivirus Settings
Configure AntiVirus settings

API Endpoints:
    GET  /antivirus/settings - Get antivirus settings
    PUT  /antivirus/settings - Update antivirus settings
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Settings:
    """Antivirus Settings endpoint"""

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
        GET /antivirus/settings
        Get antivirus settings

        Args:
            vdom: Virtual domain (optional)

            Query parameters (all optional):
            datasource: Include datasource information for each linked object
            with_meta: Include meta information about each object
            skip: Enable CLI skip operator to hide skipped properties
            action: Special actions (default, schema, revision)
            **kwargs: Any additional parameters

        Returns:
            Antivirus settings configuration

        Examples:
            >>> # Get antivirus settings
            >>> settings = fgt.cmdb.antivirus.settings.get()

            >>> # Get with meta information
            >>> settings = fgt.cmdb.antivirus.settings.get(with_meta=True)
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

        return self._client.get('cmdb', 'antivirus/settings', params=params if params else None, vdom=vdom)

    def update(
        self,
        data: Optional[Dict[str, Any]] = None,
        default_db: Optional[str] = None,
        grayware: Optional[str] = None,
        override_timeout: Optional[int] = None,
        cache_infected_result: Optional[str] = None,
        cache_clean_result: Optional[str] = None,
        machine_learning_detection: Optional[str] = None,
        use_extreme_db: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        PUT /antivirus/settings
        Update antivirus settings

        Args:
            default_db: Default antivirus database - 'normal', 'extended', 'extreme'
            grayware: Enable/disable grayware detection - 'enable' or 'disable'
            override_timeout: Override timeout in seconds (10-3600, 0=use recommended)
            cache_infected_result: Enable/disable caching of infected file results - 'enable' or 'disable'
            cache_clean_result: Enable/disable caching of clean file results - 'enable' or 'disable'
            machine_learning_detection: Enable/disable machine learning detection - 'enable' or 'disable'
            use_extreme_db: Enable/disable extreme database - 'enable' or 'disable'
            vdom: Virtual domain (optional)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Enable grayware detection
            >>> fgt.cmdb.antivirus.settings.update(
            ...     grayware='enable',
            ...     default_db='extended'
            ... )

            >>> # Configure caching
            >>> fgt.cmdb.antivirus.settings.update(
            ...     cache_infected_result='enable',
            ...     cache_clean_result='enable',
            ...     override_timeout=300
            ... )

            >>> # Enable machine learning
            >>> fgt.cmdb.antivirus.settings.update(
            ...     machine_learning_detection='enable',
            ...     use_extreme_db='enable'
            ... )
        """
        # Build data dict from provided parameters
        data = {}

        # Map Python parameter names to API field names
        param_map = {
            'default_db': default_db,
            'grayware': grayware,
            'override_timeout': override_timeout,
            'cache_infected_result': cache_infected_result,
            'cache_clean_result': cache_clean_result,
            'machine_learning_detection': machine_learning_detection,
            'use_extreme_db': use_extreme_db,
        }

        # API field name mapping
        api_field_map = {
            'default_db': 'default-db',
            'grayware': 'grayware',
            'override_timeout': 'override-timeout',
            'cache_infected_result': 'cache-infected-result',
            'cache_clean_result': 'cache-clean-result',
            'machine_learning_detection': 'machine-learning-detection',
            'use_extreme_db': 'use-extreme-db',
        }

        # Add non-None parameters
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        # Add any extra kwargs
        data.update(kwargs)

        return self._client.put('cmdb', 'antivirus/settings', data, vdom=vdom)
