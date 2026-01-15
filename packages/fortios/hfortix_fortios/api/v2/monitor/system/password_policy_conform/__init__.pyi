"""Type stubs for PASSWORD_POLICY_CONFORM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .select import Select

__all__ = [
    "Select",
    "PasswordPolicyConform",
]


class PasswordPolicyConform:
    """PASSWORD_POLICY_CONFORM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    select: Select

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize password_policy_conform category with HTTP client."""
        ...
