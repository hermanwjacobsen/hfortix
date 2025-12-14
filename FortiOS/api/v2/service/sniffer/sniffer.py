"""
FortiOS Service - Packet Sniffer

Manage packet captures on FortiOS devices.

API Endpoints:
    GET    /api/v2/service/sniffer/list/     - List all packet captures
    POST   /api/v2/service/sniffer/start/    - Start a new packet capture
    POST   /api/v2/service/sniffer/stop/     - Stop a running packet capture
    POST   /api/v2/service/sniffer/download/ - Download packet capture as PCAP
    POST   /api/v2/service/sniffer/delete/   - Delete a packet capture
    GET    /api/v2/service/sniffer/meta/     - Get system limitations and meta info
"""
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....client import FortiOS


class Sniffer:
    """Packet sniffer service endpoint"""

    def __init__(self, client: 'FortiOS') -> None:
        self._client = client

    def list(self, mkey: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all packet captures

        Returns list of all packet captures and their status information.

        Args:
            mkey (str, optional): Filter by packet capture name
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with list of packet captures

        Response fields:
            - mkey (str): Packet capture name
            - status (str): Status - 'not_started', 'running', 'finished', 'error'
            - config (dict): Packet capture configuration
            - start_time (int): Unix timestamp when capture started
            - end_time (int): Unix timestamp when capture ended
            - vdom (str): VDOM the packet capture is in

        Examples:
            >>> # List all packet captures
            >>> captures = fgt.service.sniffer.list()

            >>> # List specific packet capture
            >>> capture = fgt.service.sniffer.list(mkey='my-capture')
        """
        params = {}
        if mkey is not None:
            params['mkey'] = mkey

        params.update(kwargs)

        return self._client.get('service', 'sniffer/list/',
                               params=params if params else None, vdom=vdom)

    def start(self, mkey: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Start a new packet capture

        Creates a new packet capture and starts it. The packet capture must be
        configured in the FortiOS configuration before starting.

        Args:
            mkey (str, required): Packet capture name
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response with start status

        Response fields:
            - status (str): Start status - 'success'
            - mkey (str): Name of the packet capture that was started

        Examples:
            >>> # Start a packet capture
            >>> result = fgt.service.sniffer.start('my-capture')

            >>> # Start capture in specific VDOM
            >>> result = fgt.service.sniffer.start('my-capture', vdom='root')
        """
        data = {'mkey': mkey}
        data.update(kwargs)

        return self._client.post('service', 'sniffer/start/', data, vdom=vdom)

    def stop(self, mkey: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Stop a running packet capture

        Stops a running packet capture.

        Args:
            mkey (str, required): Packet capture name
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Stop a packet capture
            >>> result = fgt.service.sniffer.stop('my-capture')

            >>> # Stop capture in specific VDOM
            >>> result = fgt.service.sniffer.stop('my-capture', vdom='root')
        """
        data = {'mkey': mkey}
        data.update(kwargs)

        return self._client.post('service', 'sniffer/stop/', data, vdom=vdom)

    def download(self, mkey: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> bytes:
        """
        Download packet capture as PCAP file

        Returns a PCAP file of the packet capture. The capture must be stopped
        before it can be downloaded.

        Args:
            mkey (str, required): Packet capture name
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            bytes: PCAP file data (binary)

        Examples:
            >>> # Download a packet capture
            >>> pcap_data = fgt.service.sniffer.download('my-capture')

            >>> # Save to file
            >>> with open('capture.pcap', 'wb') as f:
            ...     f.write(pcap_data)
            >>> print(f"Saved {len(pcap_data)} bytes")
        """
        # Build URL and parameters
        url = f"{self._client.url}/api/v2/service/sniffer/download/"
        params = {}

        # Add vdom parameter if specified
        if vdom is not None:
            params['vdom'] = vdom
        elif self._client.vdom is not None:
            params['vdom'] = self._client.vdom

        # Prepare request data
        data = {'mkey': mkey}
        data.update(kwargs)

        # Make request - download returns binary PCAP data, not JSON
        res = self._client.session.request(
            method='POST',
            url=url,
            json=data,
            params=params if params else None
        )

        # Check for errors
        if not res.ok:
            try:
                error_detail = res.json()
                from ....exceptions import APIError
                raise APIError(f"HTTP {res.status_code}: {error_detail}")
            except ValueError:
                res.raise_for_status()

        # Return raw binary content (PCAP file)
        return res.content

    def delete(self, mkey: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Delete a packet capture

        Deletes a packet capture from the FortiGate.

        Args:
            mkey (str, required): Packet capture name
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Delete a packet capture
            >>> result = fgt.service.sniffer.delete('my-capture')

            >>> # Delete capture from specific VDOM
            >>> result = fgt.service.sniffer.delete('my-capture', vdom='root')
        """
        data = {'mkey': mkey}
        data.update(kwargs)

        return self._client.post('service', 'sniffer/delete/', data, vdom=vdom)

    def meta(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get system limitations and meta information

        Returns system limitations and meta information about the packet capture
        feature on this FortiGate.

        Args:
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with meta information

        Response fields:
            - max_packet_captures (int): Maximum number of packet captures per VDOM
            - max_packet_count (int): Maximum number of packets in a capture
            - default_packet_count (int): Default number of packets in a capture
            - has_disk (int): True (1) if FortiGate has a disk to store captures

        Examples:
            >>> # Get packet capture meta information
            >>> meta = fgt.service.sniffer.meta()
            >>> print(f"Max captures: {meta['results']['max_packet_captures']}")
            >>> print(f"Max packets: {meta['results']['max_packet_count']}")
            >>> print(f"Has disk: {meta['results']['has_disk']}")
        """
        params = {}
        params.update(kwargs)

        return self._client.get('service', 'sniffer/meta/',
                               params=params if params else None, vdom=vdom)
