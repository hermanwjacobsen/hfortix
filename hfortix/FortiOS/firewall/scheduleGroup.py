"""Firewall Schedule Group Convenience Wrapper."""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from ..api._helpers import normalize_to_name_list
from ._helpers import validate_color, validate_schedule_name

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from ..fortios import FortiOS


class ScheduleGroup:
    """Convenience wrapper for firewall schedule groups."""

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the ScheduleGroup wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.schedule_group

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Get schedule group(s)."""
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
        members: Union[str, List[str], List[Dict[str, str]]],
        color: Optional[int] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Create a new schedule group."""
        validate_schedule_name(name, "create")

        if color is not None:
            validate_color(color)

        member_list = normalize_to_name_list(members)

        if not member_list or len(member_list) == 0:
            raise ValueError("At least one member schedule is required")

        data: dict[str, Any] = {
            "name": name,
            "member": member_list,
        }

        if color is not None:
            data["color"] = color

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.post(data, **api_params)

    def update(
        self,
        name: str,
        members: Optional[Union[str, List[str], List[Dict[str, str]]]] = None,
        color: Optional[int] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Update an existing schedule group."""
        validate_schedule_name(name, "update")

        if color is not None:
            validate_color(color)

        data: dict[str, Any] = {}

        if members is not None:
            member_list = normalize_to_name_list(members)
            if not member_list or len(member_list) == 0:
                raise ValueError("At least one member schedule is required")
            data["member"] = member_list

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
        """Delete a schedule group."""
        validate_schedule_name(name, "delete")

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.delete(name, **api_params)

    def exists(self, name: str, vdom: Optional[str] = None) -> bool:
        """Check if a schedule group exists."""
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
        """Get a schedule group by name, returning the group data directly."""
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
        """Rename a schedule group."""
        validate_schedule_name(name, "rename (current name)")
        validate_schedule_name(new_name, "rename (new name)")

        current = self.get_by_name(name=name, vdom=vdom)
        if not current:
            raise ValueError(f"Schedule group '{name}' not found")

        api_params: dict[str, Any] = {"name": new_name}
        if vdom:
            api_params["vdom"] = vdom

        return self._api.put(name, data={"name": new_name}, vdom=vdom)

    def clone(
        self,
        name: str,
        new_name: str,
        members: Optional[Union[str, List[str], List[Dict[str, str]]]] = None,
        color: Optional[int] = None,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Clone an existing schedule group."""
        validate_schedule_name(name, "clone (source)")
        validate_schedule_name(new_name, "clone (new name)")

        original = self.get_by_name(name=name, vdom=vdom)
        if not original:
            raise ValueError(f"Schedule group '{name}' not found")

        clone_members = (
            members if members is not None else original.get("member", [])
        )
        member_list = normalize_to_name_list(clone_members)

        if not member_list or len(member_list) == 0:
            raise ValueError("At least one member schedule is required")

        clone_data: dict[str, Any] = {
            "name": new_name,
            "member": member_list,
        }

        clone_color = color if color is not None else original.get("color")
        if clone_color is not None:
            validate_color(clone_color)
            clone_data["color"] = clone_color

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom

        return self._api.post(clone_data, **api_params)

    def add_member(
        self, name: str, member: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Add a member to an existing schedule group."""
        validate_schedule_name(name, "add_member")

        current = self.get_by_name(name=name, vdom=vdom)
        if not current:
            raise ValueError(f"Schedule group '{name}' not found")

        current_members = current.get("member", [])
        member_names = [
            m.get("name") if isinstance(m, dict) else m
            for m in current_members
        ]

        if member in member_names:
            raise ValueError(
                f"Member '{member}' already exists in group '{name}'"
            )

        updated_members = current_members + [{"name": member}]

        return self.update(name=name, members=updated_members, vdom=vdom)

    def remove_member(
        self, name: str, member: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Remove a member from an existing schedule group."""
        validate_schedule_name(name, "remove_member")

        current = self.get_by_name(name=name, vdom=vdom)
        if not current:
            raise ValueError(f"Schedule group '{name}' not found")

        current_members = current.get("member", [])
        updated_members = [
            m
            for m in current_members
            if (m.get("name") if isinstance(m, dict) else m) != member
        ]

        if len(updated_members) == len(current_members):
            raise ValueError(f"Member '{member}' not found in group '{name}'")

        if len(updated_members) == 0:
            raise ValueError(f"Cannot remove last member from group '{name}'")

        return self.update(name=name, members=updated_members, vdom=vdom)
