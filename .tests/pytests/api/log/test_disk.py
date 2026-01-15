"""
Auto-generated tests for LOG disk endpoint.

These are basic smoke tests to verify:
  1. Endpoint class can be imported
  2. Nested classes exist
  3. Basic structure is correct

Note: These tests do NOT make actual API calls.
      They only verify the generated code structure.
"""

import pytest
from unittest.mock import Mock, MagicMock

from hfortix_fortios.api.v2.log.disk import Disk


class TestDiskStructure:
    """Test disk endpoint structure."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock HTTP client."""
        client = Mock()
        client.get = MagicMock(return_value={"status": "success"})
        client.post = MagicMock(return_value={"status": "success"})
        client.put = MagicMock(return_value={"status": "success"})
        client.delete = MagicMock(return_value={"status": "success"})
        return client

    @pytest.fixture
    def disk_endpoint(self, mock_client):
        """Create disk endpoint instance."""
        return Disk(mock_client)

    def test_import_disk(self):
        """Test that disk class can be imported."""
        from hfortix_fortios.api.v2.log.disk import Disk
        assert Disk is not None

    def test_disk_instantiation(self, disk_endpoint):
        """Test that endpoint can be instantiated."""
        assert disk_endpoint is not None
        assert hasattr(disk_endpoint, "_client")

    def test_disk_has_attributes(self, disk_endpoint):
        """Test that endpoint has expected nested attributes."""
        # Get all attributes (excluding private/magic methods)
        attrs = [a for a in dir(disk_endpoint) if not a.startswith("_")]
        
        # Should have at least some nested classes or methods
        assert len(attrs) > 0, "Endpoint should have nested classes or methods"
        
        # Print discovered structure for debugging
        print(f"\nDiscovered disk attributes: {attrs}")
