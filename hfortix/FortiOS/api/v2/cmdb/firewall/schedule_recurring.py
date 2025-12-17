"""
FortiOS CMDB - Firewall Schedule Recurring

Recurring schedule configuration.

API Endpoints:
    GET    /api/v2/cmdb/firewall.schedule/recurring           - List all / Get specific
    POST   /api/v2/cmdb/firewall.schedule/recurring           - Create
    PUT    /api/v2/cmdb/firewall.schedule/recurring/{name}   - Update
    DELETE /api/v2/cmdb/firewall.schedule/recurring/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class ScheduleRecurring:
    """Firewall recurring schedule endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ScheduleRecurring endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get a specific recurring schedule by name, or list all if name is not provided.

        Args:
            name: Schedule name (optional - if None, lists all schedules)
            datasource: Include datasource information
            with_meta: Include metadata
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all schedules
            >>> result = fgt.cmdb.firewall.schedule.recurring.get()
            >>> # Get recurring schedule
            >>> result = fgt.cmdb.firewall.schedule.recurring.get('weekday-business-hours')
            >>> print(f"Days: {result['results']['day']}")
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

        if name is not None:
            path = f"firewall.schedule/recurring/{encode_path_component(name)}"
        else:
            path = "firewall.schedule/recurring"
            
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        day: Optional[list[str]] = None,
        color: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create recurring schedule.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Schedule name
            start: Start time (format: hh:mm, e.g., '08:00')
            end: End time (format: hh:mm, e.g., '18:00')
            day: Days of week (list of: 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
            color: Color (0-32, default=0)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # POST - Create weekday business hours
            >>> result = fgt.cmdb.firewall.schedule.recurring.create(
            ...     name='weekday-business-hours',
            ...     start='08:00',
            ...     end='18:00',
            ...     day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
            ... )

            >>> # POST - Create weekend schedule
            >>> result = fgt.cmdb.firewall.schedule.recurring.create(
            ...     name='weekend-morning',
            ...     start='08:00',
            ...     end='12:00',
            ...     day=['saturday', 'sunday']
            ... )

            >>> # POST - Create 24/7 schedule
            >>> result = fgt.cmdb.firewall.schedule.recurring.create(
            ...     name='always',
            ...     start='00:00',
            ...     end='23:59',
            ...     day=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
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
            if day is not None:
                payload_dict["day"] = day
            if color is not None:
                payload_dict["color"] = color
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        payload_dict = {
            "name": name,
            "start": start,
            "end": end,
        }

        param_map = {
            "day": day,
            "color": color,
            "fabric-object": fabric_object,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall.schedule/recurring"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        day: Optional[list[str]] = None,
        color: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update recurring schedule.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Schedule name
            start: Start time (format: hh:mm)
            end: End time (format: hh:mm)
            day: Days of week (list of: 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
            color: Color (0-32, default=0)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Extend business hours
            >>> result = fgt.cmdb.firewall.schedule.recurring.update(
            ...     name='weekday-business-hours',
            ...     end='20:00'
            ... )

            >>> # Add Saturday to workdays
            >>> result = fgt.cmdb.firewall.schedule.recurring.update(
            ...     name='weekday-business-hours',
            ...     day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
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
            if day is not None:
                payload_dict["day"] = day
            if color is not None:
                payload_dict["color"] = color
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        payload_dict = {}

        param_map = {
            "start": start,
            "end": end,
            "day": day,
            "color": color,
            "fabric-object": fabric_object,
        }

        for key, value in param_map.items():
            if value is not None:
                payload_dict[key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = f"firewall.schedule/recurring/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a recurring schedule.

        Args:
            name: Schedule name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete schedule
            >>> result = fgt.cmdb.firewall.schedule.recurring.delete('old-schedule')
        """
        path = f"firewall.schedule/recurring/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if a recurring schedule exists.

        Args:
            name: Schedule name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if schedule exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.schedule.recurring.exists('weekday-business-hours'):
            ...     print("Schedule exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return result.get("status") == "success"
        except Exception:
            return False
