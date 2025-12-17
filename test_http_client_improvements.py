"""
Test script to demonstrate HTTP Client improvements:
1. Retry logic with exponential backoff
2. URL normalization
"""

import sys
from pathlib import Path

# Add hfortix to path
sys.path.insert(0, str(Path(__file__).parent / "hfortix"))

from FortiOS.http_client import HTTPClient


def test_url_normalization():
    """Test that trailing slashes are stripped from base URL"""
    print("=" * 60)
    print("TEST 1: URL Normalization")
    print("=" * 60)

    test_cases = [
        ("https://192.0.2.10", "https://192.0.2.10"),
        ("https://192.0.2.10/", "https://192.0.2.10"),
        ("https://192.0.2.10//", "https://192.0.2.10"),
        ("https://192.0.2.10:8443", "https://192.0.2.10:8443"),
        ("https://192.0.2.10:8443/", "https://192.0.2.10:8443"),
    ]

    for input_url, expected_url in test_cases:
        client = HTTPClient(
            url=input_url,
            verify=False,
            token="test-token-12345",
        )
        
        actual_url = client._url
        status = "✓ PASS" if actual_url == expected_url else "✗ FAIL"
        
        print(f"\n{status}")
        print(f"  Input:    {input_url}")
        print(f"  Expected: {expected_url}")
        print(f"  Actual:   {actual_url}")
        
        client.close()

    print("\n")


def test_retry_configuration():
    """Test retry logic configuration"""
    print("=" * 60)
    print("TEST 2: Retry Logic Configuration")
    print("=" * 60)

    # Test different retry configurations
    configs = [
        {"max_retries": 0, "desc": "No retries"},
        {"max_retries": 3, "desc": "Default (3 retries)"},
        {"max_retries": 5, "desc": "High reliability (5 retries)"},
    ]

    for config in configs:
        client = HTTPClient(
            url="https://192.0.2.10",
            verify=False,
            token="test-token",
            max_retries=config["max_retries"],
        )
        
        print(f"\n✓ {config['desc']}")
        print(f"  max_retries = {client._max_retries}")
        print(f"  Total attempts = {client._max_retries + 1}")
        
        client.close()

    print("\n")


def test_retry_delay_calculation():
    """Test exponential backoff calculation"""
    print("=" * 60)
    print("TEST 3: Exponential Backoff Delays")
    print("=" * 60)

    client = HTTPClient(
        url="https://192.0.2.10",
        verify=False,
        token="test-token",
        max_retries=5,
    )

    print("\nExponential backoff delays (no Retry-After header):")
    for attempt in range(6):
        delay = client._get_retry_delay(attempt)
        print(f"  Attempt {attempt + 1}: {delay:.1f}s")

    client.close()
    print("\n")


def test_should_retry_logic():
    """Test retry decision logic"""
    print("=" * 60)
    print("TEST 4: Retry Decision Logic")
    print("=" * 60)

    client = HTTPClient(
        url="https://192.0.2.10",
        verify=False,
        token="test-token",
        max_retries=3,
    )

    from requests.exceptions import ConnectionError, Timeout
    import requests

    test_cases = [
        (ConnectionError("Connection refused"), 0, True, "Connection error"),
        (Timeout("Read timed out"), 0, True, "Timeout"),
        (ValueError("Invalid value"), 0, False, "ValueError (not retryable)"),
        (ConnectionError("Connection refused"), 3, False, "Max retries reached"),
    ]

    print("\nRetry decisions:")
    for error, attempt, expected, description in test_cases:
        should_retry = client._should_retry(error, attempt)
        status = "✓" if should_retry == expected else "✗"
        
        print(f"\n{status} {description}")
        print(f"  Error: {type(error).__name__}")
        print(f"  Attempt: {attempt + 1}/{client._max_retries + 1}")
        print(f"  Should retry: {should_retry} (expected: {expected})")

    client.close()
    print("\n")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("HTTP Client Improvements Test Suite")
    print("=" * 60 + "\n")

    test_url_normalization()
    test_retry_configuration()
    test_retry_delay_calculation()
    test_should_retry_logic()

    print("=" * 60)
    print("All tests completed!")
    print("=" * 60 + "\n")
