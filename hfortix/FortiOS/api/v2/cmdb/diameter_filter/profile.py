"""
FortiOS CMDB Diameter Filter Profile API
Configure Diameter filter profiles
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Profile:
    """
    Diameter Filter Profile API endpoint
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Profile endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "diameter-filter/profile"

    def get(
        self,
        name: Optional[str] = None,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Get diameter filter profile details

        Args:
            name: Profile name (None=get all with query parameters)
            params: Optional query parameters
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            Profile details or list of profiles
        """
        if name:
            return self._client.get(
                "cmdb", f"{self._base_path}/{name}", params=params, vdom=vdom, raw_json=raw_json
            )
        return self.list(params=params, vdom=vdom)

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        monitor_all_messages: Optional[str] = None,
        log_packet: Optional[str] = None,
        track_requests_answers: Optional[str] = None,
        missing_request_action: Optional[str] = None,
        protocol_version_invalid: Optional[str] = None,
        message_length_invalid: Optional[str] = None,
        request_error_flag_set: Optional[str] = None,
        cmd_flags_reserve_set: Optional[str] = None,
        command_code_invalid: Optional[str] = None,
        command_code_range: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create diameter filter profile

        Args:
            name: Profile name (max 47 chars)
            comment: Comment (max 255 chars)
            monitor_all_messages: Enable/disable logging for all User Name and Result Code AVP messages
                                  ('disable', 'enable')
            log_packet: Enable/disable packet log for triggered diameter settings
                       ('disable', 'enable')
            track_requests_answers: Enable/disable validation that each answer has a corresponding request
                                   ('disable', 'enable')
            missing_request_action: Action for answers without corresponding request
                                   ('allow', 'block', 'reset', 'monitor')
            protocol_version_invalid: Action for invalid protocol version
                                     ('allow', 'block', 'reset', 'monitor')
            message_length_invalid: Action for invalid message length
                                   ('allow', 'block', 'reset', 'monitor')
            request_error_flag_set: Action for request messages with error flag set
                                   ('allow', 'block', 'reset', 'monitor')
            cmd_flags_reserve_set: Action for messages with cmd flag reserve bits set
                                  ('allow', 'block', 'reset', 'monitor')
            command_code_invalid: Action for messages with invalid command code
                                 ('allow', 'block', 'reset', 'monitor')
            command_code_range: Valid range for command codes (0-16777215)
            **kwargs: Additional parameters
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            Creation response
        """
        vdom = kwargs.pop("vdom", None)

        data = {"name": name}

        if comment is not None:
            data["comment"] = comment
        if monitor_all_messages is not None:
            data["monitor-all-messages"] = monitor_all_messages
        if log_packet is not None:
            data["log-packet"] = log_packet
        if track_requests_answers is not None:
            data["track-requests-answers"] = track_requests_answers
        if missing_request_action is not None:
            data["missing-request-action"] = missing_request_action
        if protocol_version_invalid is not None:
            data["protocol-version-invalid"] = protocol_version_invalid
        if message_length_invalid is not None:
            data["message-length-invalid"] = message_length_invalid
        if request_error_flag_set is not None:
            data["request-error-flag-set"] = request_error_flag_set
        if cmd_flags_reserve_set is not None:
            data["cmd-flags-reserve-set"] = cmd_flags_reserve_set
        if command_code_invalid is not None:
            data["command-code-invalid"] = command_code_invalid
        if command_code_range is not None:
            data["command-code-range"] = command_code_range

        # Add any additional parameters
        data.update(kwargs)

        return self._client.post("cmdb", self._base_path, data=data, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        monitor_all_messages: Optional[str] = None,
        log_packet: Optional[str] = None,
        track_requests_answers: Optional[str] = None,
        missing_request_action: Optional[str] = None,
        protocol_version_invalid: Optional[str] = None,
        message_length_invalid: Optional[str] = None,
        request_error_flag_set: Optional[str] = None,
        cmd_flags_reserve_set: Optional[str] = None,
        command_code_invalid: Optional[str] = None,
        command_code_range: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update diameter filter profile

        Args:
            name: Profile name
            comment: Comment (max 255 chars)
            monitor_all_messages: Enable/disable logging for all User Name and Result Code AVP messages
                                  ('disable', 'enable')
            log_packet: Enable/disable packet log for triggered diameter settings
                       ('disable', 'enable')
            track_requests_answers: Enable/disable validation that each answer has a corresponding request
                                   ('disable', 'enable')
            missing_request_action: Action for answers without corresponding request
                                   ('allow', 'block', 'reset', 'monitor')
            protocol_version_invalid: Action for invalid protocol version
                                     ('allow', 'block', 'reset', 'monitor')
            message_length_invalid: Action for invalid message length
                                   ('allow', 'block', 'reset', 'monitor')
            request_error_flag_set: Action for request messages with error flag set
                                   ('allow', 'block', 'reset', 'monitor')
            cmd_flags_reserve_set: Action for messages with cmd flag reserve bits set
                                  ('allow', 'block', 'reset', 'monitor')
            command_code_invalid: Action for messages with invalid command code
                                 ('allow', 'block', 'reset', 'monitor')
            command_code_range: Valid range for command codes (0-16777215)
            **kwargs: Additional parameters
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            Update response
        """
        vdom = kwargs.pop("vdom", None)

        data = {}

        if comment is not None:
            data["comment"] = comment
        if monitor_all_messages is not None:
            data["monitor-all-messages"] = monitor_all_messages
        if log_packet is not None:
            data["log-packet"] = log_packet
        if track_requests_answers is not None:
            data["track-requests-answers"] = track_requests_answers
        if missing_request_action is not None:
            data["missing-request-action"] = missing_request_action
        if protocol_version_invalid is not None:
            data["protocol-version-invalid"] = protocol_version_invalid
        if message_length_invalid is not None:
            data["message-length-invalid"] = message_length_invalid
        if request_error_flag_set is not None:
            data["request-error-flag-set"] = request_error_flag_set
        if cmd_flags_reserve_set is not None:
            data["cmd-flags-reserve-set"] = cmd_flags_reserve_set
        if command_code_invalid is not None:
            data["command-code-invalid"] = command_code_invalid
        if command_code_range is not None:
            data["command-code-range"] = command_code_range

        # Add any additional parameters
        data.update(kwargs)

        return self._client.put(
            "cmdb", f"{self._base_path}/{name}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a diameter filter profile

        Args:
            name: Profile name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            Deletion response
        """
        return self._client.delete(
            "cmdb", f"{self._base_path}/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if a diameter filter profile exists

        Args:
            name: Profile name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if profile exists, False otherwise
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
