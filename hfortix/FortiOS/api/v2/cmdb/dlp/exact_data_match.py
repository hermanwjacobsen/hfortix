"""
FortiOS CMDB - DLP Exact Data Match

Configure exact-data-match template used by DLP scan.

API Endpoints:
    GET    /dlp/exact-data-match       - List all exact-data-match templates
    GET    /dlp/exact-data-match/{name} - Get specific template
    POST   /dlp/exact-data-match       - Create new template
    PUT    /dlp/exact-data-match/{name} - Update template
    DELETE /dlp/exact-data-match/{name} - Delete template
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ExactDataMatch:
    """DLP exact-data-match endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: str | None = None,
        # Query parameters
        attr: str | None = None,
        count: int | None = None,
        skip_to_datasource: dict[str, Any] | None = None,
        acs: int | None = None,
        search: str | None = None,
        scope: str | None = None,
        datasource: bool | None = None,
        with_meta: bool | None = None,
        skip: bool | None = None,
        format: str | None = None,
        action: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get DLP exact-data-match template(s).

        Args:
            name: Template name. If provided, gets specific template.
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned results are in ascending order
            search: Filter objects by search value
            scope: Scope - 'global', 'vdom', or 'both'
            datasource: Include datasource information for each linked object
            with_meta: Include meta information (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (pipe-separated)
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual Domain(s). Use 'root' for single VDOM, or '*' for all
            **kwargs: Additional query parameters

        Returns:
            API response dictionary with exact-data-match template(s)

        Examples:
            >>> # Get all templates
            >>> result = fgt.cmdb.dlp.exact_data_match.get()
            >>> print(f"Total templates: {len(result['results'])}")

            >>> # Get specific template
            >>> result = fgt.cmdb.dlp.exact_data_match.get('employee-db')
            >>> print(f"Data source: {result['results']['data']}")

            >>> # Get with metadata
            >>> result = fgt.cmdb.dlp.exact_data_match.get(with_meta=True)
        """
        # Build path
        path = "dlp/exact-data-match"
        if name:
            path = f"dlp/exact-data-match/{name}"

        # Build query parameters
        params = {}
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(self, vdom: str | None = None, **kwargs) -> dict[str, Any]:
        """
        List all DLP exact-data-match templates (convenience method).

        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters

        Returns:
            API response dictionary with all templates

        Examples:
            >>> # List all templates
            >>> result = fgt.cmdb.dlp.exact_data_match.list()
            >>> for t in result['results']:
            ...     print(f"{t['name']}: {t.get('data', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Template configuration
        optional: int | None = None,
        data: str | None = None,
        columns: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Create a new DLP exact-data-match template.

        Args:
            payload_dict: Complete configuration as dictionary (alternative to individual params)
            name: Name of the template (max 35 chars)
            optional: Number of optional columns need to match (0-32)
            data: External resource for exact data match (max 35 chars)
            columns: List of column definitions. Each column is a dict with:
                - index (int): Column index (1-32)
                - type (str): Data-type for this column (max 35 chars)
                - optional (str): Enable/disable optional match - 'enable' or 'disable'
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create template for employee data
            >>> result = fgt.cmdb.dlp.exact_data_match.create(
            ...     name='employee-ssn-db',
            ...     data='employee-data-source',
            ...     optional=1,
            ...     columns=[
            ...         {'index': 1, 'type': 'ssn-us', 'optional': 'disable'},
            ...         {'index': 2, 'type': 'keyword', 'optional': 'enable'}
            ...     ]
            ... )

            >>> # Create template with credit card data
            >>> result = fgt.cmdb.dlp.exact_data_match.create(
            ...     name='cc-database',
            ...     data='credit-card-source',
            ...     columns=[
            ...         {'index': 1, 'type': 'credit-card', 'optional': 'disable'},
            ...         {'index': 2, 'type': 'keyword', 'optional': 'disable'}
            ...     ]
            ... )
        """
        data_payload = {}
        param_map = {
            "name": name,
            "optional": optional,
            "data": data,
            "columns": columns,
        }

        # Map to API field names
        api_field_map = {
            "name": "name",
            "optional": "optional",
            "data": "data",
            "columns": "columns",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data_payload[api_name] = value

        data_payload.update(kwargs)

        return self._client.post(
            "cmdb", "dlp/exact-data-match", data_payload, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Template configuration
        optional: int | None = None,
        data: str | None = None,
        columns: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update an existing DLP exact-data-match template.

        Args:
            payload_dict: Complete configuration as dictionary (alternative to individual params)
            name: Name of the template to update
            optional: Number of optional columns need to match (0-32)
            data: External resource for exact data match (max 35 chars)
            columns: List of column definitions. Each column is a dict with:
                - index (int): Column index (1-32)
                - type (str): Data-type for this column (max 35 chars)
                - optional (str): Enable/disable optional match - 'enable' or 'disable'
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update optional count
            >>> result = fgt.cmdb.dlp.exact_data_match.update(
            ...     name='employee-ssn-db',
            ...     optional=2
            ... )

            >>> # Update columns
            >>> result = fgt.cmdb.dlp.exact_data_match.update(
            ...     name='employee-ssn-db',
            ...     columns=[
            ...         {'index': 1, 'type': 'ssn-us', 'optional': 'disable'},
            ...         {'index': 2, 'type': 'keyword', 'optional': 'enable'},
            ...         {'index': 3, 'type': 'keyword', 'optional': 'enable'}
            ...     ]
            ... )
        """
        data_payload = {}
        param_map = {
            "name": name,
            "optional": optional,
            "data": data,
            "columns": columns,
        }

        # Map to API field names
        api_field_map = {
            "name": "name",
            "optional": "optional",
            "data": "data",
            "columns": "columns",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data_payload[api_name] = value

        data_payload.update(kwargs)

        return self._client.put(
            "cmdb", f"dlp/exact-data-match/{name}", data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a DLP exact-data-match template.

        Args:
            name: Name of the template to delete
            vdom: Virtual Domain(s)

        Returns:
            API response dictionary

        Examples:
            >>> # Delete template
            >>> result = fgt.cmdb.dlp.exact_data_match.delete('employee-ssn-db')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete(
            "cmdb", f"dlp/exact-data-match/{name}", vdom=vdom, raw_json=raw_json
        )
