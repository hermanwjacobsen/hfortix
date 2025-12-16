"""
FortiOS CMDB - CASB Attribute Match

Configure CASB attribute match rules.

API Endpoints:
    GET    /casb/attribute-match       - List all attribute match rules
    GET    /casb/attribute-match/{name} - Get specific attribute match rule
    POST   /casb/attribute-match       - Create attribute match rule
    PUT    /casb/attribute-match/{name} - Update attribute match rule
    DELETE /casb/attribute-match/{name} - Delete attribute match rule
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AttributeMatch:
    """CASB attribute match endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize AttributeMatch endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all CASB attribute match rules

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with list of attribute match rules

        Examples:
            >>> # List all attribute match rules
            >>> rules = fgt.cmdb.casb.attribute_match.list()
            >>> print(f"Total rules: {len(rules['results'])}")

            >>> # List with specific VDOM
            >>> rules = fgt.cmdb.casb.attribute_match.list(vdom='root')
        """
        return self.get(vdom=vdom, **kwargs)

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get CASB attribute match rule(s)

        Args:
            name (str, optional): Attribute match rule name (for specific rule)
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (dict, optional): Skip to provided table's Nth entry
            acs (int, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope [global|vdom|both]
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names (pipe-separated)
            action (str, optional): Special actions (default, schema, revision)
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with attribute match rule(s)

        Examples:
            >>> # Get all attribute match rules
            >>> rules = fgt.cmdb.casb.attribute_match.get()
            >>> for rule in rules['results']:
            ...     print(f"Rule: {rule['name']}")

            >>> # Get specific rule
            >>> rule = fgt.cmdb.casb.attribute_match.get('my-rule')
            >>> print(f"Application: {rule['results']['application']}")

            >>> # Get with metadata
            >>> rule = fgt.cmdb.casb.attribute_match.get('my-rule', with_meta=True)
        """
        # Build path
        path = f"casb/attribute-match/{name}" if name else "casb/attribute-match"

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

        # Add any additional parameters
        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        application: Optional[str] = None,
        match_strategy: Optional[str] = None,
        match: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create CASB attribute match rule

        Args:
            name (str): Attribute match rule name (max 79 chars)
            application (str, optional): CASB attribute application name (max 79 chars)
            match_strategy (str, optional): Match strategy - 'or', 'and', 'subset'
                - 'or': Match when any rule is satisfied
                - 'and': Match when all rules are satisfied
                - 'subset': Match when extracted attributes are found within defined rules
            match (list, optional): List of tenant match rules (each rule is a dict with:
                - id (int): Rule ID
                - rule_strategy (str): 'and' or 'or'
                - rule (list): List of attribute rules (each with id, attribute, match_pattern, match_value, case_sensitive, negate)
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create simple attribute match rule
            >>> result = fgt.cmdb.casb.attribute_match.create(
            ...     name='my-rule',
            ...     application='office365',
            ...     match_strategy='or'
            ... )

            >>> # Create rule with match conditions
            >>> result = fgt.cmdb.casb.attribute_match.create(
            ...     name='advanced-rule',
            ...     application='google-workspace',
            ...     match_strategy='and',
            ...     match=[{
            ...         'id': 1,
            ...         'rule_strategy': 'or',
            ...         'rule': [{
            ...             'id': 1,
            ...             'attribute': 'domain',
            ...             'match_pattern': 'simple',
            ...             'match_value': 'example.com',
            ...             'case_sensitive': 'enable',
            ...             'negate': 'disable'
            ...         }]
            ...     }]
            ... )
        """
        # Build data dictionary
        data = {"name": name}

        # Map parameters
        param_map = {"application": application, "match_strategy": match_strategy, "match": match}

        api_field_map = {"match_strategy": "match-strategy"}

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map.get(param_name, param_name)

                # Handle nested match rules
                if param_name == "match" and isinstance(value, list):
                    # Convert snake_case to hyphen-case in nested structures
                    converted_match = []
                    for match_item in value:
                        converted_item = {}
                        if "id" in match_item:
                            converted_item["id"] = match_item["id"]
                        if "rule_strategy" in match_item:
                            converted_item["rule-strategy"] = match_item["rule_strategy"]
                        if "rule" in match_item and isinstance(match_item["rule"], list):
                            converted_rules = []
                            for rule in match_item["rule"]:
                                converted_rule = {}
                                field_mapping = {
                                    "id": "id",
                                    "attribute": "attribute",
                                    "match_pattern": "match-pattern",
                                    "match_value": "match-value",
                                    "case_sensitive": "case-sensitive",
                                    "negate": "negate",
                                }
                                for py_key, api_key in field_mapping.items():
                                    if py_key in rule:
                                        converted_rule[api_key] = rule[py_key]
                                converted_rules.append(converted_rule)
                            converted_item["rule"] = converted_rules
                        converted_match.append(converted_item)
                    data[api_name] = converted_match
                else:
                    data[api_name] = value

        # Add any additional parameters
        data.update(kwargs)

        return self._client.post("cmdb", "casb/attribute-match", data, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        application: Optional[str] = None,
        match_strategy: Optional[str] = None,
        match: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update CASB attribute match rule

        Args:
            name (str): Attribute match rule name
            application (str, optional): CASB attribute application name (max 79 chars)
            match_strategy (str, optional): Match strategy - 'or', 'and', 'subset'
            match (list, optional): List of tenant match rules
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update match strategy
            >>> result = fgt.cmdb.casb.attribute_match.update(
            ...     name='my-rule',
            ...     match_strategy='and'
            ... )

            >>> # Update application
            >>> result = fgt.cmdb.casb.attribute_match.update(
            ...     name='my-rule',
            ...     application='salesforce'
            ... )
        """
        # Build data dictionary
        data = {}

        # Map parameters
        param_map = {"application": application, "match_strategy": match_strategy, "match": match}

        api_field_map = {"match_strategy": "match-strategy"}

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map.get(param_name, param_name)

                # Handle nested match rules (same as create)
                if param_name == "match" and isinstance(value, list):
                    converted_match = []
                    for match_item in value:
                        converted_item = {}
                        if "id" in match_item:
                            converted_item["id"] = match_item["id"]
                        if "rule_strategy" in match_item:
                            converted_item["rule-strategy"] = match_item["rule_strategy"]
                        if "rule" in match_item and isinstance(match_item["rule"], list):
                            converted_rules = []
                            for rule in match_item["rule"]:
                                converted_rule = {}
                                field_mapping = {
                                    "id": "id",
                                    "attribute": "attribute",
                                    "match_pattern": "match-pattern",
                                    "match_value": "match-value",
                                    "case_sensitive": "case-sensitive",
                                    "negate": "negate",
                                }
                                for py_key, api_key in field_mapping.items():
                                    if py_key in rule:
                                        converted_rule[api_key] = rule[py_key]
                                converted_rules.append(converted_rule)
                            converted_item["rule"] = converted_rules
                        converted_match.append(converted_item)
                    data[api_name] = converted_match
                else:
                    data[api_name] = value

        # Add any additional parameters
        data.update(kwargs)

        return self._client.put(
            "cmdb", f"casb/attribute-match/{name}", data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete CASB attribute match rule

        Args:
            name (str): Attribute match rule name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Delete attribute match rule
            >>> result = fgt.cmdb.casb.attribute_match.delete('my-rule')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete(
            "cmdb", f"casb/attribute-match/{name}", vdom=vdom, raw_json=raw_json
        )
