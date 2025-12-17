"""
FortiOS CMDB - Firewall Schedule Onetime

Onetime schedule configuration.

API Endpoints:
    GET    /api/v2/cmdb/firewall.schedule/onetime        - List all onetime schedules
    GET    /api/v2/cmdb/firewall.schedule/onetime/{name} - Get specific onetime schedule
    POST   /api/v2/cmdb/firewall.schedule/onetime        - Create new onetime schedule
    PUT    /api/v2/cmdb/firewall.schedule/onetime/{name} - Update onetime schedule
    DELETE /api/v2/cmdb/firewall.schedule/onetime/{name} - Delete onetime schedule
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class ScheduleOnetime:
    """Firewall onetime schedule endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ScheduleOnetime endpoint

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
        List all onetime schedules.

        Args:
            filter: Filter results
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
            >>> # List all onetime schedules
            >>> result = fgt.cmdb.firewall.schedule.onetime.list()
            >>> for schedule in result['results']:
            ...     print(f"{schedule['name']}: {schedule['start']} to {schedule['end']}")
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

        path = "firewall.schedule/onetime"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def get(
        self,
        name: str,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get a specific onetime schedule by name.

        Args:
            name: Schedule name
            datasource: Include datasource information
            with_meta: Include metadata
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # Get onetime schedule
            >>> result = fgt.cmdb.firewall.schedule.onetime.get('maintenance-2024-01-01')
            >>> print(f"Starts: {result['results']['start']}")
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

        path = f"firewall.schedule/onetime/{encode_path_component(name)}"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        color: Optional[int] = None,
        expiration_days: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new onetime schedule.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Schedule name
            start: Start time (format: hh:mm yyyy/mm/dd, e.g., '23:00 2025/01/01')
            end: End time (format: hh:mm yyyy/mm/dd, e.g., '02:00 2025/01/02')
            color: Color (0-32, default=0)
            expiration_days: Delete after this many days (0=never, 1-100 days)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create maintenance window
            >>> result = fgt.cmdb.firewall.schedule.onetime.create(
            ...     name='maintenance-jan-2025',
            ...     start='22:00 2025/01/15',
            ...     end='06:00 2025/01/16'
            ... )

            >>> # Create with auto-expiration
            >>> result = fgt.cmdb.firewall.schedule.onetime.create(
            ...     name='temporary-access',
            ...     start='08:00 2025/12/20',
            ...     end='18:00 2025/12/20',
            ...     expiration_days=7
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
            if start is not None:
                payload_dict["start"] = start
            if end is not None:
                payload_dict["end"] = end
            if color is not None:
                payload_dict["color"] = color
            if expiration_days is not None:
                payload_dict["expiration-days"] = expiration_days
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        payload_dict = {
            "name": name,
            "start": start,
            "end": end,
        }

        param_map = {
            "color": color,
            "expiration-days": expiration_days,
            "fabric-object": fabric_object,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall.schedule/onetime"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        color: Optional[int] = None,
        expiration_days: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update an existing onetime schedule.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Schedule name
            start: Start time (format: hh:mm yyyy/mm/dd)
            end: End time (format: hh:mm yyyy/mm/dd)
            color: Color (0-32, default=0)
            expiration_days: Delete after this many days (0=never, 1-100 days)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Extend maintenance window
            >>> result = fgt.cmdb.firewall.schedule.onetime.update(
            ...     name='maintenance-jan-2025',
            ...     end='08:00 2025/01/16'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if start is not None:
                payload_dict["start"] = start
            if end is not None:
                payload_dict["end"] = end
            if color is not None:
                payload_dict["color"] = color
            if expiration_days is not None:
                payload_dict["expiration-days"] = expiration_days
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        payload_dict = {}

        param_map = {
            "start": start,
            "end": end,
            "color": color,
            "expiration-days": expiration_days,
            "fabric-object": fabric_object,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = f"firewall.schedule/onetime/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a onetime schedule.

        Args:
            name: Schedule name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete schedule
            >>> result = fgt.cmdb.firewall.schedule.onetime.delete('old-maintenance')
        """
        path = f"firewall.schedule/onetime/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if a onetime schedule exists.

        Args:
            name: Schedule name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if schedule exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.schedule.onetime.exists('maintenance-jan-2025'):
            ...     print("Schedule exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return result.get("status") == "success"
        except Exception:
            return False
