"""Shared validation helpers for firewall convenience wrappers."""

from datetime import datetime
from typing import Union

from ..api._helpers import (
    validate_color,
    validate_ip_address,
    validate_ip_network,
    validate_ipv6_address,
    validate_mac_address,
    validate_status,
)

__all__ = [
    "validate_color",
    "validate_status",
    "validate_mac_address",
    "validate_ip_address",
    "validate_ipv6_address",
    "validate_ip_network",
    "validate_policy_id",
    "validate_address_pairs",
    "validate_seq_num",
    "validate_schedule_name",
    "validate_time_format",
    "validate_day_names",
]


def validate_policy_id(
    policy_id: Union[str, int, None], operation: str = "operation"
) -> None:
    """
    Validate policy ID is provided and within valid range (0 to 4294967295).

    Args:
        policy_id: The policy ID to validate
        operation: Name of the operation (for error messages)

    Raises:
        ValueError: If policy_id is None, empty, or out of range
    """
    if policy_id is None:
        raise ValueError(f"Policy ID is required for {operation} operation")

    if isinstance(policy_id, str) and not policy_id.strip():
        raise ValueError(
            f"Policy ID cannot be empty for {operation} operation"
        )

    try:
        policy_id_int = int(policy_id)
    except (ValueError, TypeError):
        raise ValueError(
            f"Policy ID must be a valid integer, got: {policy_id}"
        )

    if not 0 <= policy_id_int <= 4294967295:
        raise ValueError(
            f"Policy ID must be between 0 and 4294967295, got {policy_id_int}"
        )


def validate_address_pairs(
    srcaddr: Union[str, list, None],
    dstaddr: Union[str, list, None],
    srcaddr6: Union[str, list, None],
    dstaddr6: Union[str, list, None],
) -> None:
    """
    Validate address pairs are complete and at least one pair is provided.

    Args:
        srcaddr: Source IPv4 address(es)
        dstaddr: Destination IPv4 address(es)
        srcaddr6: Source IPv6 address(es)
        dstaddr6: Destination IPv6 address(es)

    Raises:
        ValueError: If address pairs are incomplete or missing
    """
    has_ipv4_src = srcaddr is not None
    has_ipv4_dst = dstaddr is not None
    has_ipv6_src = srcaddr6 is not None
    has_ipv6_dst = dstaddr6 is not None

    if has_ipv4_src and not has_ipv4_dst:
        raise ValueError(
            "IPv4 source address provided ('srcaddr') but destination "
            "address missing: provide 'dstaddr' to complete the IPv4 "
            "address pair."
        )
    if has_ipv4_dst and not has_ipv4_src:
        raise ValueError(
            "IPv4 destination address provided ('dstaddr') but source "
            "address missing: provide 'srcaddr' to complete the IPv4 "
            "address pair."
        )

    if has_ipv6_src and not has_ipv6_dst:
        raise ValueError(
            "IPv6 source address provided ('srcaddr6') but destination "
            "address missing: provide 'dstaddr6' to complete the IPv6 "
            "address pair."
        )
    if has_ipv6_dst and not has_ipv6_src:
        raise ValueError(
            "IPv6 destination address provided ('dstaddr6') but source "
            "address missing: provide 'srcaddr6' to complete the IPv6 "
            "address pair."
        )

    has_ipv4_pair = has_ipv4_src and has_ipv4_dst
    has_ipv6_pair = has_ipv6_src and has_ipv6_dst

    if not has_ipv4_pair and not has_ipv6_pair:
        raise ValueError(
            "At least one complete address pair is required: "
            "provide either ('srcaddr' AND 'dstaddr') for IPv4, "
            "or ('srcaddr6' AND 'dstaddr6') for IPv6, "
            "or both pairs for dual-stack."
        )


def validate_seq_num(
    seq_num: Union[str, int, None], operation: str = "operation"
) -> None:
    """
    Validate sequence number is provided and within valid range
    (0 to 4294967295).

    Args:
        seq_num: The sequence number to validate
        operation: Name of the operation (for error messages)

    Raises:
        ValueError: If seq_num is None, empty, or out of range
    """
    if seq_num is None:
        raise ValueError(
            f"Sequence number is required for {operation} operation"
        )

    if isinstance(seq_num, str) and not seq_num.strip():
        raise ValueError(
            f"Sequence number cannot be empty for {operation} " f"operation"
        )

    try:
        seq_num_int = int(seq_num)
    except (ValueError, TypeError):
        raise ValueError(
            f"Sequence number must be a valid integer, got: {seq_num}"
        )

    if not 0 <= seq_num_int <= 4294967295:
        raise ValueError(
            f"Sequence number must be between 0 and 4294967295, "
            f"got {seq_num_int}"
        )


def validate_schedule_name(
    name: Union[str, None], operation: str = "operation"
) -> None:
    """
    Validate schedule name (max 31 characters).

    Args:
        name: Schedule name to validate
        operation: Name of the operation (for error messages)

    Raises:
        ValueError: If name is None, empty, or exceeds max length
    """
    if name is None:
        raise ValueError(
            f"Schedule name is required for {operation} operation"
        )

    if isinstance(name, str) and not name.strip():
        raise ValueError(
            f"Schedule name cannot be empty for {operation} operation"
        )

    if isinstance(name, str) and len(name) > 31:
        raise ValueError(
            f"Schedule name must be 31 characters or less, got {len(name)}"
        )


def validate_time_format(time_str: str, field_name: str = "time") -> None:
    """
    Validate time format is HH:MM (00:00-23:59).

    Args:
        time_str: Time string to validate
        field_name: Name of the field (for error messages)

    Raises:
        ValueError: If time format is invalid
    """
    if not time_str:
        raise ValueError(f"{field_name} time is required")

    try:
        datetime.strptime(time_str, "%H:%M")
    except ValueError as e:
        raise ValueError(
            f"{field_name} must be in format HH:MM (00:00-23:59), "
            f"got: {time_str}"
        ) from e


def validate_day_names(day_str: str) -> None:
    """
    Validate day names for recurring schedule.

    Args:
        day_str: Space-separated day names

    Raises:
        ValueError: If day names are invalid
    """
    valid_days = {
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "none",
    }

    if not day_str:
        raise ValueError("At least one day must be specified")

    days = day_str.lower().split()
    for day in days:
        if day not in valid_days:
            raise ValueError(
                f"Invalid day '{day}'. Must be one of: "
                f"{', '.join(sorted(valid_days))}"
            )
