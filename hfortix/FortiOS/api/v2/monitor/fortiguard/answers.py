"""Monitor API - Answers operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Answers:
    """Answers operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Answers endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        page: int | None = None,
        pagesize: int | None = None,
        sortkey: str | None = None,
        topics: str | None = None,
        limit: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of questions on answers.
        
        Args:
            page: Page number to retrieve. (optional)
            pagesize: Page size of a list of response. (optional)
            sortkey: Sort key of a list of response. (optional)
            topics: Topic to retrieve. (optional)
            limit: Limit of the number of entries. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.fortiguard.answers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if page is not None:
            params['page'] = page
        if pagesize is not None:
            params['pagesize'] = pagesize
        if sortkey is not None:
            params['sortkey'] = sortkey
        if topics is not None:
            params['topics'] = topics
        if limit is not None:
            params['limit'] = limit
        params.update(kwargs)
        return self._client.get("monitor", "/fortiguard/answers", params=params)
