"""
Service Group Convenience Wrapper

Provides simplified syntax for service group operations with full
parameter support.
Instead of: fgt.api.cmdb.firewall.service_group.post(data)
Use: fgt.firewall.service_group.create(name='Web-Group',
    member=['HTTP', 'HTTPS'], ...)
"""

import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    List,
    Literal,
    Optional,
    Union,
)

from ..api._helpers import build_cmdb_payload_normalized, validate_color

if TYPE_CHECKING:
    from ..fortios import FortiOS


def validate_service_group_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """Validate service group name."""
    if not name:
        raise ValueError(f"Service group name is required for {operation}")
    if isinstance(name, str) and len(name) > 79:
        raise ValueError(
            f"Service group name cannot exceed 79 characters, got {len(name)}"
        )


def validate_comment(comment: Optional[str]) -> None:
    """Validate comment parameter."""
    if comment is not None and isinstance(comment, str) and len(comment) > 255:
        raise ValueError(
            f"Comment cannot exceed 255 characters, got {len(comment)}"
        )


def validate_proxy(proxy: Optional[str]) -> None:
    """Validate proxy parameter."""
    if proxy is not None and proxy not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid proxy value '{proxy}'. Must be 'enable' or 'disable'"
        )


def validate_fabric_object(fabric_object: Optional[str]) -> None:
    """Validate fabric-object parameter."""
    if fabric_object is not None and fabric_object not in [
        "enable",
        "disable",
    ]:
        raise ValueError(
            f"Invalid fabric-object value '{fabric_object}'. "
            f"Must be 'enable' or 'disable'"
        )


def normalize_member_list(
    member: Union[str, List[str], List[Dict[str, str]], None],
) -> Optional[List[Dict[str, str]]]:
    """
    Normalize member parameter to FortiOS format.

    Converts string or list of strings to list of dicts:
    [{"name": "service1"}, {"name": "service2"}]
    """
    if member is None:
        return None
    if isinstance(member, str):
        return [{"name": member}]
    if isinstance(member, list):
        if not member:
            return []
        if isinstance(member[0], dict):
            return member  # type: ignore
        return [{"name": str(m)} for m in member]
    return None


class ServiceGroup:
    """
    Convenience wrapper for service group operations with full
    parameter support.
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """Initialize the ServiceGroup wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.service_group
        self._logger = logging.getLogger("hfortix.firewall.service_group")

    def create(
        self,
        # Required parameters
        name: str,
        member: Union[str, List[str], List[Dict[str, str]]],
        # Optional parameters
        uuid: Optional[str] = None,
        proxy: Optional[Literal["enable", "disable"]] = None,
        comment: Optional[str] = None,
        color: Optional[int] = None,
        fabric_object: Optional[Literal["enable", "disable"]] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Create a new service group.

        Args:
            name: Service group name (max 79 chars, required)
            member: Service objects contained within the group (required)
                    Can be: string, list of strings, or list of dicts
            uuid: Universally Unique Identifier
            proxy: Enable/disable web proxy service group
            comment: Comment (max 255 chars)
            color: Color of icon on GUI (0-32)
            fabric_object: Security Fabric global object setting
            vdom: Virtual domain name
            data: Additional fields as dictionary

        Returns:
            API response dictionary

        Example:
            >>> # Create with list of member names
            >>> result = fgt.firewall.service_group.create(
            ...     name="Web-Group",
            ...     member=["HTTP", "HTTPS", "HTTP-8080"],
            ...     comment="Web services group"
            ... )
            >>>
            >>> # Create with single member
            >>> result = fgt.firewall.service_group.create(
            ...     name="DNS-Group",
            ...     member="DNS"
            ... )
        """
        validate_service_group_name(name, "create")
        validate_comment(comment)
        validate_proxy(proxy)
        validate_fabric_object(fabric_object)
        if color is not None:
            validate_color(color)

        # Normalize member list
        normalized_member = normalize_member_list(member)
        if not normalized_member:
            raise ValueError(
                "At least one member is required for service group"
            )

        payload = build_cmdb_payload_normalized(
            name=name,
            uuid=uuid,
            proxy=proxy,
            member=normalized_member,
            comment=comment,
            color=color,
            fabric_object=fabric_object,
            data=data,
        )

        self._logger.debug(f"Creating service group: {name}")
        return self._api.post(payload_dict=payload, vdom=vdom)

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Retrieve service group configuration."""
        return self._api.get(name=name, vdom=vdom, **kwargs)

    def update(
        self,
        # Required parameter
        name: str,
        # Optional parameters
        uuid: Optional[str] = None,
        proxy: Optional[Literal["enable", "disable"]] = None,
        member: Optional[Union[str, List[str], List[Dict[str, str]]]] = None,
        comment: Optional[str] = None,
        color: Optional[int] = None,
        fabric_object: Optional[Literal["enable", "disable"]] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Update an existing service group."""
        validate_service_group_name(name, "update")
        validate_comment(comment)
        validate_proxy(proxy)
        validate_fabric_object(fabric_object)
        if color is not None:
            validate_color(color)

        # Normalize member list if provided
        normalized_member = (
            normalize_member_list(member) if member is not None else None
        )

        payload = build_cmdb_payload_normalized(
            uuid=uuid,
            proxy=proxy,
            member=normalized_member,
            comment=comment,
            color=color,
            fabric_object=fabric_object,
            data=data,
        )

        self._logger.debug(f"Updating service group: {name}")
        return self._api.put(name=name, payload_dict=payload, vdom=vdom)

    def rename(
        self, name: str, new_name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Rename a service group."""
        validate_service_group_name(name, "rename (name)")
        validate_service_group_name(new_name, "rename (new_name)")
        return self.update(name=name, data={"name": new_name}, vdom=vdom)

    def delete(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Delete a service group."""
        validate_service_group_name(name, "delete")
        return self._api.delete(name=name, vdom=vdom)

    def exists(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """Check if a service group exists."""
        validate_service_group_name(name, "exists")
        return self._api.exists(name=name, vdom=vdom)

    def get_by_name(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]], None]:
        """Get a service group by name, returning None if not found."""
        validate_service_group_name(name, "get_by_name")
        try:
            return self.get(name=name, vdom=vdom)
        except Exception as e:
            self._logger.debug(f"Service group not found: {name} - {e}")
            return None

    def add_member(
        self,
        group_name: str,
        member: Union[str, List[str]],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Add member(s) to an existing service group.

        Args:
            group_name: Service group name
            member: Member name(s) to add (string or list)
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Example:
            >>> # Add single member
            >>> result = fgt.firewall.service_group.add_member(
            ...     "Web-Group", "DNS"
            ... )
            >>>
            >>> # Add multiple members
            >>> result = fgt.firewall.service_group.add_member(
            ...     "Web-Group", ["FTP", "SMTP"]
            ... )
        """
        validate_service_group_name(group_name, "add_member")

        # Get current group with raw_json=True to get full response
        current = self.get(name=group_name, vdom=vdom, raw_json=True)
        # Type narrowing for async/sync compatibility
        if isinstance(current, dict):
            current_dict = current
        else:
            # If it's a coroutine, this is in async context
            # Not typical for this use case
            raise TypeError(
                "add_member does not support async context directly"
            )

        if not current_dict or "results" not in current_dict:
            raise ValueError(f"Service group '{group_name}' not found")

        # When getting a specific object, results is a dict, not a list
        group_data = current_dict["results"]
        if isinstance(group_data, list):
            # Handle case where results is a list
            # (shouldn't happen with name specified)
            if not group_data:
                raise ValueError(f"Service group '{group_name}' not found")
            group_data = group_data[0]

        current_members = group_data.get("member", [])

        # Normalize new members
        if isinstance(member, str):
            new_members = [member]
        else:
            new_members = member

        # Build updated member list
        existing_names = {m["name"] for m in current_members if "name" in m}
        for new_member in new_members:
            if new_member not in existing_names:
                current_members.append({"name": new_member})

        self._logger.debug(
            f"Adding member(s) to service group {group_name}: {new_members}"
        )
        return self.update(name=group_name, member=current_members, vdom=vdom)

    def remove_member(
        self,
        group_name: str,
        member: Union[str, List[str]],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Remove member(s) from an existing service group.

        Args:
            group_name: Service group name
            member: Member name(s) to remove (string or list)
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Example:
            >>> # Remove single member
            >>> result = fgt.firewall.service_group.remove_member(
            ...     "Web-Group", "DNS"
            ... )
            >>>
            >>> # Remove multiple members
            >>> result = fgt.firewall.service_group.remove_member(
            ...     "Web-Group", ["FTP", "SMTP"]
            ... )
        """
        validate_service_group_name(group_name, "remove_member")

        # Get current group with raw_json=True to get full response
        current = self.get(name=group_name, vdom=vdom, raw_json=True)
        # Type narrowing for async/sync compatibility
        if isinstance(current, dict):
            current_dict = current
        else:
            # If it's a coroutine, this is in async context
            # Not typical for this use case
            raise TypeError(
                "remove_member does not support async context directly"
            )

        if not current_dict or "results" not in current_dict:
            raise ValueError(f"Service group '{group_name}' not found")

        # When getting a specific object, results is a dict, not a list
        group_data = current_dict["results"]
        if isinstance(group_data, list):
            # Handle case where results is a list
            # (shouldn't happen with name specified)
            if not group_data:
                raise ValueError(f"Service group '{group_name}' not found")
            group_data = group_data[0]

        current_members = group_data.get("member", [])

        # Normalize members to remove
        if isinstance(member, str):
            members_to_remove = {member}
        else:
            members_to_remove = set(member)

        # Filter out members to remove
        updated_members = [
            m
            for m in current_members
            if m.get("name") not in members_to_remove
        ]

        if not updated_members:
            raise ValueError(
                "Cannot remove all members from service group. "
                "At least one member is required."
            )

        self._logger.debug(
            f"Removing member(s) from service group {group_name}: "
            f"{members_to_remove}"
        )
        return self.update(name=group_name, member=updated_members, vdom=vdom)
