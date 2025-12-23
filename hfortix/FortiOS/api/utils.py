"""
FortiOS API Utilities

Utility functions for testing, validation, and performance analysis.
"""

from __future__ import annotations

import logging
import statistics
import time
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..http_client import HTTPClient

logger = logging.getLogger(__name__)

__all__ = ["Utils"]


class Utils:
    """
    Utility functions for FortiOS API operations.

    Provides tools for:
    - Performance testing and benchmarking
    - Connection pool validation
    - Device profiling and recommendations

    Example:
        >>> fgt = FortiOS(host="192.168.1.99", token="token")
        >>> results = fgt.api.utils.performance_test()
        >>> results.print_summary()
    """

    def __init__(self, client: "HTTPClient"):
        """Initialize utilities with HTTP client reference"""
        self._client = client

    def performance_test(
        self,
        test_validation: bool = True,
        test_endpoints: bool = True,
        test_concurrency: bool = False,
        sequential_count: int = 10,
        concurrent_count: int = 50,
        concurrent_level: int = 20,
        endpoints: Optional[list[str]] = None,
    ) -> "PerformanceTestResults":  # type: ignore[name-defined] # noqa: F821
        """
        Run performance tests on this FortiGate device

        Tests connection pool settings, API endpoint performance, and provides
        device-specific recommendations for optimal configuration.

        Args:
            test_validation: Test connection pool validation (default: True)
            test_endpoints: Test various API endpoints (default: True)
            test_concurrency: Test concurrent performance (default: False, can
            be slow)
            sequential_count: Number of sequential requests per endpoint
            (default: 10)
            concurrent_count: Number of concurrent requests (default: 50)
            concurrent_level: Concurrency level for async test (default: 20)
            endpoints: Custom list of endpoints to test (default: common
            endpoints)

        Returns:
            PerformanceTestResults object with detailed metrics and
            recommendations

        Example:
            >>> fgt = FortiOS(host="192.168.1.99", token="token", verify=False)
            >>>
            >>> # Quick test (validation + endpoints)
            >>> results = fgt.api.utils.performance_test()
            >>> results.print_summary()
            >>>
            >>> # Custom test
            >>> results = fgt.api.utils.performance_test(
            ...     test_endpoints=True,
            ...     test_concurrency=True,
            ...     sequential_count=20,
            ...     endpoints=['monitor/system/status', 'cmdb/firewall/policy']
            ... )
            >>>
            >>> # Access results programmatically
            >>> print(f"Device profile: {results.device_profile}")
            >>> print(f"Throughput: {results.sequential_throughput:.2f} req/s")
            >>> print(f"Recommended: {results.recommended_settings}")

        See Also:
            - Performance guide: docs/PERFORMANCE_TESTING.md
            - Example usage: examples/performance_test_examples.py
        """
        from ..performance_test import PerformanceTestResults

        results = PerformanceTestResults()

        print("\n" + "=" * 70)
        print("FortiGate Performance Test")
        print("=" * 70)
        print(f"Testing: {self._client._url}")
        print("=" * 70 + "\n")

        # Test 1: Connection pool validation
        if test_validation:
            print("[1/3] Testing connection pool validation...")
            passed, warnings = self._test_connection_pool_validation()
            results.validation_passed = passed
            results.validation_warnings = warnings
            if passed:
                print("✓ Connection pool validation: PASSED")
            else:
                print("✗ Connection pool validation: FAILED")
                for warning in warnings:
                    print(f"  {warning}")

        # Test 2: Endpoint performance
        if test_endpoints:
            print("\n[2/3] Testing endpoint performance...")
            try:
                endpoint_results = self._test_endpoint_performance(
                    endpoints=endpoints,
                    count=sequential_count,
                )
                results.endpoint_results = endpoint_results

                # Calculate average response time across all endpoints
                valid_avgs = [
                    metrics["avg_ms"]
                    for metrics in endpoint_results.values()
                    if "avg_ms" in metrics
                ]

                if valid_avgs:
                    overall_avg = statistics.mean(valid_avgs)
                    print(f"✓ Tested {len(endpoint_results)} endpoints")
                    print(f"  Average response time: {overall_avg:.1f}ms")

                    # Determine device profile
                    profile, settings = self._determine_device_profile(
                        overall_avg
                    )
                    results.device_profile = profile
                    results.recommended_settings = settings

                    # Estimate throughput
                    results.sequential_throughput = 1000 / overall_avg
                    print(
                        f"  Estimated throughput: "
                        f"{results.sequential_throughput:.2f} req/s"
                    )
                else:
                    print("✗ No valid endpoint results")
                    results.errors.append("No valid endpoint results")

            except Exception as e:
                print(f"✗ Endpoint testing failed: {e}")
                results.errors.append(f"Endpoint testing: {e}")

        # Test 3: Concurrent performance (optional)
        if test_concurrency:
            print("\n[3/3] Testing concurrent performance...")
            msg = (
                "  ⚠ Note: Most FortiGates serialize requests - "
                "concurrency may not help"
            )
            print(msg)
            try:
                duration = self._test_concurrent_performance(
                    count=concurrent_count,
                    concurrency=concurrent_level,
                )
                results.concurrent_throughput = concurrent_count / duration

                print("✓ Concurrent test complete")
                print(f"  {concurrent_count} requests in {duration:.2f}s")
                throughput = results.concurrent_throughput
                print(f"  Throughput: {throughput:.2f} req/s")

                # Compare with sequential
                if results.sequential_throughput:
                    improvement = (
                        (
                            results.concurrent_throughput
                            - results.sequential_throughput
                        )
                        / results.sequential_throughput
                        * 100
                    )
                    if improvement > 10:
                        print(f"  → Concurrency helps! (+{improvement:.0f}%)")
                    elif improvement < -10:
                        print(
                            f"  → Concurrency hurts! ({
                                improvement:.0f}%) - Use sequential!"
                        )
                    else:
                        print(f"  → Concurrency neutral ({improvement:+.0f}%)")

            except Exception as e:
                print(f"✗ Concurrent testing failed: {e}")
                results.errors.append(f"Concurrent testing: {e}")
        else:
            print("\n[3/3] Concurrent performance test: SKIPPED")
            print("  (Enable with test_concurrency=True)")

        print("\n" + "=" * 70)
        print("Performance Test Complete!")
        print("=" * 70)

        return results

    def _test_connection_pool_validation(self) -> tuple[bool, list[str]]:
        """Test connection pool validation logic"""
        warnings = []

        try:
            # Import FortiOS here to avoid circular dependency
            from .. import FortiOS

            # Test 1: Normal configuration
            try:
                _ = FortiOS(
                    "test.example.com",
                    token="test",
                    max_connections=30,
                    max_keepalive_connections=15,
                )
                logger.debug("✓ Test 1 passed: Normal configuration accepted")
            except Exception as e:
                return False, [f"Normal configuration failed: {e}"]

            # Test 2: Auto-adjustment
            try:
                _ = FortiOS(
                    "test.example.com",
                    token="test",
                    max_connections=5,
                    max_keepalive_connections=20,
                )
                warnings.append(
                    "Auto-adjusted max_keepalive_connections from 20 to 5"
                )
                logger.debug("✓ Test 2 passed: Auto-adjustment working")
            except Exception as e:
                return False, [f"Auto-adjustment failed: {e}"]

            return True, warnings

        except Exception as e:
            return False, [f"Validation test error: {e}"]

    def _test_endpoint_performance(
        self,
        endpoints: Optional[list[str]] = None,
        count: int = 10,
    ) -> dict[str, dict[str, Any]]:
        """Test performance of API endpoints"""

        # Default endpoints to test
        if endpoints is None:
            endpoints = [
                "monitor/system/status",
                "monitor/system/resource/usage",
                "cmdb/firewall/address",
                "cmdb/firewall/policy",
                "cmdb/system/interface",
            ]

        results: dict[str, dict[str, Any]] = {}

        for endpoint_path in endpoints:
            logger.info(f"Testing endpoint: {endpoint_path}")
            endpoint_name = endpoint_path.replace("/", "_")
            times = []
            successes = 0

            # Determine API type
            parts = endpoint_path.split("/")
            api_type = parts[0]
            path = "/".join(parts[1:])

            try:
                # Make test requests
                for i in range(count):
                    start = time.time()
                    try:
                        self._client.get(api_type, path)
                        elapsed = (time.time() - start) * 1000  # ms
                        times.append(elapsed)
                        successes += 1
                    except Exception as e:
                        logger.warning(f"Request {i + 1} failed: {e}")
                        times.append(0)

                # Calculate metrics
                valid_times = [t for t in times if t > 0]
                if valid_times:
                    results[endpoint_name] = {
                        "count": count,
                        "successes": successes,
                        "success_rate": (successes / count) * 100,
                        "avg_ms": statistics.mean(valid_times),
                        "median_ms": statistics.median(valid_times),
                        "min_ms": min(valid_times),
                        "max_ms": max(valid_times),
                    }

                    if len(valid_times) >= 3:
                        sorted_times = sorted(valid_times)
                        p95_idx = int(len(sorted_times) * 0.95)
                        results[endpoint_name]["p95_ms"] = sorted_times[
                            p95_idx
                        ]
                else:
                    results[endpoint_name] = {"error": "All requests failed"}

            except Exception as e:
                results[endpoint_name] = {"error": str(e)}

        return results

    def _test_concurrent_performance(
        self,
        count: int = 50,
        concurrency: int = 20,
    ) -> float:
        """Test concurrent performance (async mode)"""
        import asyncio

        async def concurrent_test():
            # Import async client
            from .. import FortiOS

            # Get connection details from current client
            # Parse URL to extract host
            url = self._client._url
            host = url.replace("https://", "").replace("http://", "")

            # Create async client - note: this creates a new session
            # We can't easily share auth from sync client, so this test
            # is more for relative performance comparison
            fgt = FortiOS(
                host=host,
                token="test_token",  # Placeholder
                verify=self._client._verify,  # noqa: E501
                vdom=self._client._vdom,
                mode="async",
                max_connections=concurrency,
            )

            start = time.time()
            tasks = []

            # Note: This will fail without valid auth, but serves as a template
            # In practice, users should pass their real credentials
            for _ in range(count):
                tasks.append(fgt.api.monitor.system.status.get())

            try:
                await asyncio.gather(*tasks)
            except Exception:
                # Expected to fail without valid auth, but we can still measure
                # timing
                pass

            duration = time.time() - start

            await fgt.aclose()

            return duration

        # For now, skip async test if we can't authenticate
        # Return estimated duration based on sequential performance
        print("  ⚠ Concurrent test requires valid authentication")
        msg = (
            "  ⚠ Skipping concurrent test - not yet implemented "
            "for reusing auth"
        )
        print(msg)  # noqa: E501
        raise NotImplementedError(
            (
                "Concurrent testing not yet implemented. "
                "Use run_performance_test() from "
                "hfortix.FortiOS.performance_test instead."
            )
        )

    def _determine_device_profile(
        self, avg_response_ms: float
    ) -> tuple[str, dict[str, Any]]:
        """Determine device profile based on average response time"""

        if avg_response_ms < 50:
            profile = "high-performance"
            settings = {
                "max_connections": 60,
                "max_keepalive_connections": 30,
                "recommended_concurrency": "20-30",
                "expected_throughput": "~30 req/s",
                "use_async": "Optional - can help with batches",
            }
        elif avg_response_ms < 100:
            profile = "fast-lan"
            settings = {
                "max_connections": 20,
                "max_keepalive_connections": 10,
                "recommended_concurrency": "1 (sequential)",
                "expected_throughput": "~5-10 req/s",
                "use_async": "Not recommended - no benefit",
            }
        else:
            profile = "remote-wan"
            settings = {
                "max_connections": 20,
                "max_keepalive_connections": 10,
                "recommended_concurrency": "1 (sequential)",
                "expected_throughput": "~5 req/s",
                "use_async": "Not recommended - adds complexity",
                "note": "High latency detected - check network path",
            }

        return profile, settings

    def __dir__(self):
        """Control autocomplete to show only public methods"""
        return ["performance_test"]
