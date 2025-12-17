"""
Log custom field endpoint module.

This module provides access to the log/custom-field endpoint
for managing custom log fields.

API Path: log/custom-field
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class CustomField:
    """
    Interface for managing custom log fields.

    This class provides CRUD operations for custom log field configuration.

    Example usage:
        # List all custom fields
        fields = fgt.api.cmdb.log.custom_field.get()

        # Get specific custom field
        field = fgt.api.cmdb.log.custom_field.get(pkey='field1')

        # Create new custom field
        fgt.api.cmdb.log.custom_field.create(
            id='field1',
            name='CustomField1',
            value='custom_value'
        )

        # Update custom field
        fgt.api.cmdb.log.custom_field.update(
            pkey='field1',
            name='UpdatedField'
        )

        # Delete custom field
        fgt.api.cmdb.log.custom_field.delete(pkey='field1')
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the CustomField instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log/custom-field"

    def get(
        self, pkey: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Retrieve custom log field configuration.

        Args:
            pkey: Custom field ID (retrieves specific field if provided)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing custom field configuration

        Example:
            >>> # Get all custom fields
            >>> result = fgt.api.cmdb.log.custom_field.get()
            >>>
            >>> # Get specific custom field
            >>> result = fgt.api.cmdb.log.custom_field.get(pkey='field1')
        """
        path = f"{self._endpoint}/{pkey}" if pkey else self._endpoint
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def create(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Create a new custom log field.

        Args:
            data_dict: Dictionary with API format parameters
            id: Custom field ID
            name: Name of custom log field
            value: Value of custom log field
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.custom_field.create(
            ...     id='field1',
            ...     name='CustomField1',
            ...     value='custom_value'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "id": "id",
            "name": "name",
            "value": "value",
        }

        for py_name, api_name in param_map.items():
            value_param = locals().get(py_name)
            if value_param is not None:
                payload[api_name] = value_param

        payload.update(kwargs)

        return self._client.post("cmdb", self._endpoint, data=payload, vdom=vdom)

    def update(
        self,
        pkey: str,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update an existing custom log field.

        Args:
            pkey: Custom field ID to update
            data_dict: Dictionary with API format parameters
            id: Custom field ID
            name: Name of custom log field
            value: Value of custom log field
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.custom_field.update(
            ...     pkey='field1',
            ...     name='UpdatedField',
            ...     value='new_value'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "id": "id",
            "name": "name",
            "value": "value",
        }

        for py_name, api_name in param_map.items():
            value_param = locals().get(py_name)
            if value_param is not None:
                payload[api_name] = value_param

        payload.update(kwargs)

        path = f"{self._endpoint}/{pkey}"
        return self._client.put("cmdb", path, data=payload, vdom=vdom)

    def delete(self, pkey: str, vdom: Optional[Union[str, bool]] = None) -> Dict[str, Any]:
        """
        Delete a custom log field.

        Args:
            pkey: Custom field ID to delete
            vdom: Virtual domain

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.custom_field.delete(pkey='field1')
        """
        path = f"{self._endpoint}/{pkey}"
        return self._client.delete("cmdb", path, vdom=vdom)
