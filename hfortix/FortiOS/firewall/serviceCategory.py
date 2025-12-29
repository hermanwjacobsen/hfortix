"""
Service Category Convenience Wrapper

Provides simplified syntax for service category operations with full
parameter support.
Instead of: fgt.api.cmdb.firewall.service_category.post(data)
Use: fgt.firewall.service_category.create(name='MyCategory', ...)
"""

import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    Literal,
    Optional,
    Union,
)

from ..api._helpers import build_cmdb_payload_normalized

if TYPE_CHECKING:
    from ..fortios import FortiOS


def validate_fabric_object(value: Optional[str]) -> None:
    """
    Validate fabric-object parameter.

    Args:
        value: The fabric-object value to validate

    Raises:
        ValueError: If value is invalid
    """
    if value is not None and value not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid fabric-object value '{value}'. "
            f"Must be 'enable' or 'disable'"
        )


def validate_service_category_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """
    Validate service category name.

    Args:
        name: The name to validate
        operation: Operation name for error messages

    Raises:
        ValueError: If name is invalid
    """
    if not name:
        raise ValueError(f"Service category name is required for {operation}")

    if isinstance(name, str):
        if len(name) > 63:
            raise ValueError(
                f"Service category name cannot exceed 63 characters, "
                f"got {len(name)}"
            )


def validate_comment(comment: Optional[str]) -> None:
    """
    Validate comment parameter.

    Args:
        comment: The comment to validate

    Raises:
        ValueError: If comment is too long
    """
    if comment is not None and isinstance(comment, str) and len(comment) > 255:
        raise ValueError(
            f"Comment cannot exceed 255 characters, got {len(comment)}"
        )


class ServiceCategory:
    """
    Convenience wrapper for service category operations with full
    parameter support.
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """
        Initialize the ServiceCategory wrapper.

        Args:
            fortios_instance: The parent FortiOS instance
        """
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.service_category
        self._logger = logging.getLogger("hfortix.firewall.service_category")

    def create(
        self,
        # Required parameters
        name: str,
        # Optional parameters
        uuid: Optional[str] = None,
        comment: Optional[str] = None,
        fabric_object: Optional[Literal["enable", "disable"]] = None,
        # API parameters
        vdom: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        raw_json: Optional[bool] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Create a new service category with all available parameters.

        Args:
            name: Service category name (max 63 chars, required)
            uuid: Universally Unique Identifier (UUID; automatically
                assigned but can be manually reset)
            comment: Comment (max 255 chars)
            fabric_object: Security Fabric global object setting
                ('enable'/'disable')
            vdom: Virtual domain name
            datasource: Include datasource information
            with_meta: Include meta information
            raw_json: Return raw JSON response
            data: Additional fields as dictionary

        Returns:
            API response dictionary

        Raises:
            ValueError: If validation fails

        Example:
            >>> result = fgt.firewall.service_category.create(
            ...     name="Web-Services",
            ...     comment="HTTP and HTTPS services",
            ...     fabric_object="disable"
            ... )
        """
        # Validate required parameters
        validate_service_category_name(name, "create")

        # Validate optional parameters
        validate_comment(comment)
        validate_fabric_object(fabric_object)

        # Build payload using normalized helper
        payload = build_cmdb_payload_normalized(
            name=name,
            uuid=uuid,
            comment=comment,
            fabric_object=fabric_object,
            data=data,
        )

        self._logger.debug(f"Creating service category: {name}")
        return self._api.post(
            payload_dict=payload,
            vdom=vdom,
            datasource=datasource,
            with_meta=with_meta,
            raw_json=(
                raw_json if raw_json is not None else False
            ),  # API expects bool, default to False
        )

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Retrieve service category configuration.

        Args:
            name: Specific category name (optional, returns all if not
                specified)
            vdom: Virtual domain name
            **kwargs: Additional query parameters (filter, format, etc.)

        Returns:
            API response dictionary

        Example:
            >>> # Get all categories
            >>> categories = fgt.firewall.service_category.get()
            >>>
            >>> # Get specific category
            >>> category = fgt.firewall.service_category.get(
            ...     name="Web-Services"
            ... )
        """
        self._logger.debug(
            f"Getting service category: {name if name else 'all'}"
        )
        return self._api.get(name=name, vdom=vdom, **kwargs)

    def update(
        self,
        # Required parameter
        name: str,
        # Optional parameters
        uuid: Optional[str] = None,
        comment: Optional[str] = None,
        fabric_object: Optional[Literal["enable", "disable"]] = None,
        # API parameters
        vdom: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        raw_json: Optional[bool] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Update an existing service category.

        Args:
            name: Service category name (required)
            uuid: Universally Unique Identifier
            comment: Comment (max 255 chars)
            fabric_object: Security Fabric global object setting
                ('enable'/'disable')
            vdom: Virtual domain name
            datasource: Include datasource information
            with_meta: Include meta information
            raw_json: Return raw JSON response
            data: Additional fields as dictionary

        Returns:
            API response dictionary

        Raises:
            ValueError: If validation fails

        Example:
            >>> result = fgt.firewall.service_category.update(
            ...     name="Web-Services",
            ...     comment="Updated comment"
            ... )
        """
        # Validate required parameters
        validate_service_category_name(name, "update")

        # Validate optional parameters
        validate_comment(comment)
        validate_fabric_object(fabric_object)

        # Build payload
        payload = build_cmdb_payload_normalized(
            uuid=uuid,
            comment=comment,
            fabric_object=fabric_object,
            data=data,
        )

        self._logger.debug(f"Updating service category: {name}")
        return self._api.put(
            name=name,
            payload_dict=payload,
            vdom=vdom,
            datasource=datasource,
            with_meta=with_meta,
            raw_json=(
                raw_json if raw_json is not None else False
            ),  # API expects bool, default to False
        )

    def rename(
        self,
        name: str,
        new_name: str,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Rename a service category.

        Args:
            name: Current category name
            new_name: New category name
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Raises:
            ValueError: If validation fails

        Example:
            >>> result = fgt.firewall.service_category.rename(
            ...     name="Web-Services",
            ...     new_name="WebServices"
            ... )
        """
        validate_service_category_name(name, "rename (name)")
        validate_service_category_name(new_name, "rename (new_name)")

        self._logger.debug(f"Renaming service category: {name} -> {new_name}")
        return self.update(name=name, data={"name": new_name}, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Delete a service category.

        Args:
            name: Category name to delete (required)
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is not provided

        Example:
            >>> result = fgt.firewall.service_category.delete(
            ...     name="Web-Services"
            ... )
        """
        validate_service_category_name(name, "delete")

        self._logger.debug(f"Deleting service category: {name}")
        return self._api.delete(name=name, vdom=vdom)

    def exists(
        self,
        name: str,
        vdom: Optional[str] = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if a service category exists.

        Args:
            name: Category name to check
            vdom: Virtual domain name

        Returns:
            True if category exists, False otherwise

        Example:
            >>> if fgt.firewall.service_category.exists("Web-Services"):
            ...     print("Category exists")
        """
        validate_service_category_name(name, "exists")

        self._logger.debug(f"Checking if service category exists: {name}")
        return self._api.exists(name=name, vdom=vdom)

    def get_by_name(
        self,
        name: str,
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]], None]:
        """
        Get a service category by name, returning None if not found.

        Args:
            name: Category name
            vdom: Virtual domain name

        Returns:
            Category configuration or None if not found

        Example:
            >>> category = fgt.firewall.service_category.get_by_name(
            ...     "Web-Services"
            ... )
            >>> if category:
            ...     print(f"Found: {category['comment']}")
        """
        validate_service_category_name(name, "get_by_name")

        try:
            return self.get(name=name, vdom=vdom)
        except Exception as e:
            self._logger.debug(f"Service category not found: {name} - {e}")
            return None
