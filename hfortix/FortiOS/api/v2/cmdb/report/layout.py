"""
Report layout endpoint module.

This module provides access to the report/layout endpoint
for managing report layout configurations.

API Path: report/layout
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Layout:
    """
    Interface for managing report layouts.

    This class provides CRUD operations for report layout configuration.

    Example usage:
        # List all report layouts
        layouts = fgt.api.cmdb.report.layout.get()

        # Get specific report layout
        layout = fgt.api.cmdb.report.layout.get(pkey='daily-report')

        # POST - Create report layout
        fgt.api.cmdb.report.layout.create(
            name='custom-report',
            title='Custom Report',
            schedule_type='daily'
        )

        # PUT - Update report layout
        fgt.api.cmdb.report.layout.update(
            pkey='custom-report',
            title='Updated Report'
        )

        # Delete report layout
        fgt.api.cmdb.report.layout.delete(pkey='custom-report')
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the Layout instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "report/layout"

    def get(
        self, pkey: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Retrieve report layout configuration.

        Args:
            pkey: Layout name (retrieves specific layout if provided)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing report layout configuration

        Example:
            >>> # Get all report layouts
            >>> result = fgt.api.cmdb.report.layout.get()
            >>>
            >>> # Get specific report layout
            >>> result = fgt.api.cmdb.report.layout.get(pkey='daily-report')
        """
        path = f"{self._endpoint}/{pkey}" if pkey else self._endpoint
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        body_item: Optional[list] = None,
        cutoff_option: Optional[str] = None,
        cutoff_time: Optional[str] = None,
        day: Optional[str] = None,
        description: Optional[str] = None,
        email_recipients: Optional[str] = None,
        email_send: Optional[str] = None,
        format: Optional[str] = None,
        max_pdf_report: Optional[int] = None,
        name: Optional[str] = None,
        options: Optional[str] = None,
        page: Optional[dict] = None,
        schedule_type: Optional[str] = None,
        style_theme: Optional[str] = None,
        subtitle: Optional[str] = None,
        time: Optional[str] = None,
        title: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Create report layout.

        Args:
            data_dict: Dictionary with API format parameters
            body_item: Report body items configuration
            cutoff_option: Cutoff option (run-time | custom)
            cutoff_time: Cutoff time
            day: Day of week/month for scheduled reports
            description: Description
            email_recipients: Email recipients
            email_send: Enable/disable email sending (enable | disable)
            format: Report format (pdf | html)
            max_pdf_report: Maximum number of PDF reports to keep
            name: Report layout name
            options: Report options
            page: Page settings (header, footer, etc.)
            schedule_type: Schedule type (demand | daily | weekly | monthly)
            style_theme: Style theme
            subtitle: Report subtitle
            time: Time for scheduled reports
            title: Report title
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.report.layout.create(
            ...     name='custom-report',
            ...     title='Custom Daily Report',
            ...     schedule_type='daily',
            ...     format='pdf'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "body_item": "body-item",
            "cutoff_option": "cutoff-option",
            "cutoff_time": "cutoff-time",
            "day": "day",
            "description": "description",
            "email_recipients": "email-recipients",
            "email_send": "email-send",
            "format": "format",
            "max_pdf_report": "max-pdf-report",
            "name": "name",
            "options": "options",
            "page": "page",
            "schedule_type": "schedule-type",
            "style_theme": "style-theme",
            "subtitle": "subtitle",
            "time": "time",
            "title": "title",
        }

        for py_name, api_name in param_map.items():
            value_param = locals().get(py_name)
            if value_param is not None:
                payload[api_name] = value_param

        payload.update(kwargs)

        return self._client.post("cmdb", self._endpoint, data=payload, vdom=vdom)

    def put(
        self,
        pkey: str,
        data_dict: Optional[Dict[str, Any]] = None,
        body_item: Optional[list] = None,
        cutoff_option: Optional[str] = None,
        cutoff_time: Optional[str] = None,
        day: Optional[str] = None,
        description: Optional[str] = None,
        email_recipients: Optional[str] = None,
        email_send: Optional[str] = None,
        format: Optional[str] = None,
        max_pdf_report: Optional[int] = None,
        name: Optional[str] = None,
        options: Optional[str] = None,
        page: Optional[dict] = None,
        schedule_type: Optional[str] = None,
        style_theme: Optional[str] = None,
        subtitle: Optional[str] = None,
        time: Optional[str] = None,
        title: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update report layout.

        Args:
            pkey: Layout name to update
            data_dict: Dictionary with API format parameters
            body_item: Report body items configuration
            cutoff_option: Cutoff option (run-time | custom)
            cutoff_time: Cutoff time
            day: Day of week/month for scheduled reports
            description: Description
            email_recipients: Email recipients
            email_send: Enable/disable email sending (enable | disable)
            format: Report format (pdf | html)
            max_pdf_report: Maximum number of PDF reports to keep
            name: Report layout name
            options: Report options
            page: Page settings (header, footer, etc.)
            schedule_type: Schedule type (demand | daily | weekly | monthly)
            style_theme: Style theme
            subtitle: Report subtitle
            time: Time for scheduled reports
            title: Report title
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.report.layout.update(
            ...     pkey='custom-report',
            ...     title='Updated Report Title',
            ...     email_send='enable'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "body_item": "body-item",
            "cutoff_option": "cutoff-option",
            "cutoff_time": "cutoff-time",
            "day": "day",
            "description": "description",
            "email_recipients": "email-recipients",
            "email_send": "email-send",
            "format": "format",
            "max_pdf_report": "max-pdf-report",
            "name": "name",
            "options": "options",
            "page": "page",
            "schedule_type": "schedule-type",
            "style_theme": "style-theme",
            "subtitle": "subtitle",
            "time": "time",
            "title": "title",
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
        Delete a report layout.

        Args:
            pkey: Layout name to delete
            vdom: Virtual domain

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.report.layout.delete(pkey='custom-report')
        """
        path = f"{self._endpoint}/{pkey}"
        return self._client.delete("cmdb", path, vdom=vdom)
