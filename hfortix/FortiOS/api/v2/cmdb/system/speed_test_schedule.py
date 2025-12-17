"""
FortiOS CMDB - System SpeedTestSchedule

Speed test schedule for each interface.

API Endpoints:
    GET    /system/speed-test-schedule           - List all / Get specific
    POST   /system/speed-test-schedule           - Create
    PUT    /system/speed-test-schedule/{name}   - Update
    DELETE /system/speed-test-schedule/{name}   - Delete
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class SpeedTestSchedule:
    """speed-test-schedule endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize SpeedTestSchedule endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        format: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get speed-test-schedule

        Args:
            name (str, optional): Object name (get specific object)
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions
            format (str, optional): Field list to return
            filter (str, optional): Filter expression
            count (int, optional): Maximum number of entries
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response

        Examples:
            >>> # Get all
            >>> result = fgt.api.cmdb.system.speed_test_schedule.get()
            
            >>> # Get specific by name
            >>> result = fgt.api.cmdb.system.speed_test_schedule.get(name='obj1')
        """
        params = {}
        
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
            "format": format,
            "filter": filter,
            "count": count,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        path = "system/speed-test-schedule"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create speed-test-schedule

        Args:
            payload_dict (dict, optional): Complete configuration as dictionary
            name (str, optional): Object name
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # POST - Create with dictionary
            >>> result = fgt.api.cmdb.system.speed_test_schedule.create(
            ...     payload_dict={'name': 'obj1', 'comment': 'Test'}
            ... )
            
            >>> # POST - Create with parameters
            >>> result = fgt.api.cmdb.system.speed_test_schedule.create(
            ...     name='obj1',
            ...     comment='Test'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        if name is not None:
            data["name"] = name
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.post("cmdb", "system/speed-test-schedule", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update speed-test-schedule

        Args:
            name (str): Object name (required)
            payload_dict (dict, optional): Complete configuration as dictionary
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update with dictionary
            >>> result = fgt.api.cmdb.system.speed_test_schedule.update(
            ...     name='obj1',
            ...     payload_dict={'comment': 'Updated'}
            ... )
            
            >>> # PUT - Update with parameters
            >>> result = fgt.api.cmdb.system.speed_test_schedule.update(
            ...     name='obj1',
            ...     comment='Updated'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.put("cmdb", f"system/speed-test-schedule/{encode_path_component(name)}", data=data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
    ) -> dict[str, Any]:
        """
        Delete speed-test-schedule

        Args:
            name (str): Object name to delete
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.api.cmdb.system.speed_test_schedule.delete('obj1')
        """
        return self._client.delete("cmdb", f"system/speed-test-schedule/{encode_path_component(name)}", vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if speed-test-schedule exists

        Args:
            name (str): Object name to check
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.system.speed_test_schedule.exists('obj1'):
            ...     print("Exists")
        """
        try:
            result = self.get(name=name, vdom=vdom)
            return result.get("status") == "success"
        except Exception:
            return False
