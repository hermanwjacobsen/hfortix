"""Firewall Schedule Recurring Convenience Wrapper."""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from ._helpers import (
    validate_color,
    validate_day_names,
    validate_schedule_name,
    validate_time_format,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from ..fortios import FortiOS


class ScheduleRecurring:
    """Convenience wrapper for firewall recurring schedules."""

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the ScheduleRecurring wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.schedule_recurring

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Get recurring schedule(s)."""
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        if name is not None:
            return self._api.get(name, **api_params)
        return self._api.get(**api_params)

    def create(
        self,
        name: str,
        start: str,
        end: str,
        day: str,
        color: Optional[int] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Create a new recurring schedule."""
        validate_schedule_name(name, "create")
        validate_time_format(start, "start")
        validate_time_format(end, "end")
        validate_day_names(day)

        data: dict[str, Any] = {
            "name": name,
            "start": start,
            "end": end,
            "day": day,
        }

        if color is not None:
            validate_color(color)
            data["color"] = color

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.post(data, **api_params)

    def update(
        self,
        name: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        day: Optional[str] = None,
        color: Optional[int] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Update an existing recurring schedule."""
        validate_schedule_name(name, "update")

        if start is not None:
            validate_time_format(start, "start")
        if end is not None:
            validate_time_format(end, "end")
        if day is not None:
            validate_day_names(day)
        if color is not None:
            validate_color(color)

        data: dict[str, Any] = {}
        if start is not None:
            data["start"] = start
        if end is not None:
            data["end"] = end
        if day is not None:
            data["day"] = day
        if color is not None:
            data["color"] = color

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(name, data, **api_params)

    def delete(
        self, name: str, vdom: Optional[str] = None, **kwargs: Any
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Delete a recurring schedule."""
        validate_schedule_name(name, "delete")

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.delete(name, **api_params)

    def exists(self, name: str, vdom: Optional[str] = None) -> bool:
        """Check if a recurring schedule exists."""
        validate_schedule_name(name, "exists")

        try:
            result = self.get(name=name, vdom=vdom)
            # Handle both list and dict responses
            if isinstance(result, list):
                return len(result) > 0
            elif isinstance(result, dict):
                results = result.get("results", [])
                return len(results) > 0
            return False
        except Exception:
            return False

    def get_by_name(
        self, name: str, vdom: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Get a recurring schedule by name, returning the schedule data
        directly.
        """
        validate_schedule_name(name, "get_by_name")

        try:
            result = self.get(name=name, vdom=vdom)

            if isinstance(result, dict):
                if "results" in result:
                    results = result["results"]
                else:
                    return result
            elif isinstance(result, list):
                results = result
            else:
                return None

            return results[0] if results else None
        except Exception:
            return None

    def rename(
        self,
        name: str,
        new_name: str,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Rename a recurring schedule."""
        validate_schedule_name(name, "rename (current name)")
        validate_schedule_name(new_name, "rename (new name)")

        current = self.get_by_name(name=name, vdom=vdom)
        if not current:
            raise ValueError(f"Schedule '{name}' not found")

        api_params: dict[str, Any] = {"name": new_name}
        if vdom:
            api_params["vdom"] = vdom

        return self._api.put(name, data={"name": new_name}, vdom=vdom)

    def clone(
        self,
        name: str,
        new_name: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        day: Optional[str] = None,
        color: Optional[int] = None,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Clone an existing recurring schedule."""
        validate_schedule_name(name, "clone (source)")
        validate_schedule_name(new_name, "clone (new name)")

        original = self.get_by_name(name=name, vdom=vdom)
        if not original:
            raise ValueError(f"Schedule '{name}' not found")

        clone_data: dict[str, Any] = {
            "name": new_name,
            "start": start if start is not None else original.get("start"),
            "end": end if end is not None else original.get("end"),
            "day": day if day is not None else original.get("day"),
        }

        if start is not None:
            validate_time_format(start, "start")
        if end is not None:
            validate_time_format(end, "end")
        if day is not None:
            validate_day_names(day)

        clone_color = color if color is not None else original.get("color")
        if clone_color is not None:
            validate_color(clone_color)
            clone_data["color"] = clone_color

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom

        return self._api.post(clone_data, **api_params)
