"""
Type protocols for CRUD operations.

This module defines Protocol classes that provide base signatures
for common CRUD operations (GET, POST, PUT, DELETE). These protocols
ensure consistent structure across all generated endpoint classes.

Note: The generated .pyi stub files provide the actual type hints with
endpoint-specific field signatures. These protocols serve as a base
structure that the stubs override.

Since v0.5.71, all API methods return FortiObject/FortiObjectList instances.
Use the .raw property to access the full API envelope.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from hfortix_fortios.models import FortiObject, FortiObjectList


class GetProtocol(Protocol):
    """
    Protocol defining base signature for GET operations.

    The generated .pyi stub files provide endpoint-specific overloads
    with proper return types (FortiObject vs FortiObjectList).
    
    Access the full API envelope via .raw property on the returned object.
    """

    def get(
        self,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> FortiObject | FortiObjectList: ...


class PostProtocol(Protocol):
    """
    Protocol defining signature for POST (create) operations.

    Returns FortiObject (MutationResponse).
    Access the full API envelope via .raw property.
    """

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> FortiObject: ...


class PutProtocol(Protocol):
    """
    Protocol defining signature for PUT (update) operations.

    Returns FortiObject (MutationResponse).
    Access the full API envelope via .raw property.
    """

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> FortiObject: ...


class DeleteProtocol(Protocol):
    """
    Protocol defining signature for DELETE operations.

    Returns FortiObject (MutationResponse).
    Access the full API envelope via .raw property.
    """

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> FortiObject: ...


class CRUDEndpoint(
    GetProtocol, PostProtocol, PutProtocol, DeleteProtocol, Protocol
):
    """
    Combined protocol for full CRUD endpoints.

    Endpoint classes inherit from this to get base CRUD signatures.
    The generated .pyi stub files provide endpoint-specific type hints
    that override these base signatures with field-aware autocomplete.
    """

    pass
