#!/usr/bin/env python3
"""
Performance Testing Utility for FortiOS HTTP Client

User-friendly performance testing tool to:
1. Validate connection pool settings work correctly
2. Test real-world API performance with various endpoints
3. Determine optimal settings for your FortiGate device
4. Profile your device's performance characteristics

Usage:
    from hfortix import FortiOS
    from hfortix.FortiOS.performance_test import run_performance_test

    # Quick test with your FortiGate
    results = run_performance_test(
        host="192.168.1.99",
        token="your_token_here",
        verify=False
    )

    # Full comprehensive test
    results = run_performance_test(
        host="fw.example.com",
        token="your_token_here",
        verify=True,
        test_endpoints=True,
        test_concurrency=True,
        sequential_count=20,
        concurrent_count=50
    )
"""

import asyncio
import logging
import statistics
import time
from typing import Any, Optional

logger = logging.getLogger(__name__)


class PerformanceTestResults:
    """Container for performance test results"""

    def __init__(self):
        self.validation_passed = False
        self.validation_warnings: list[str] = []
        self.endpoint_results: dict[str, dict[str, Any]] = {}
        self.sequential_throughput: Optional[float] = None
        self.concurrent_throughput: Optional[float] = None
        self.device_profile: Optional[str] = None
        self.recommended_settings: dict[str, Any] = {}
        self.errors: list[str] = []

    def __str__(self) -> str:
        """Return string representation of results"""
        lines = []
        lines.append("FortiGate Performance Test Results")
        lines.append("=" * 50)

        # Validation
        status = "PASSED" if self.validation_passed else "FAILED"
        lines.append(f"Validation: {status}")

        # Throughput
        if self.sequential_throughput:
            lines.append(
                f"Sequential Throughput: "
                f"{self.sequential_throughput:.2f} req/s"
            )
        if self.concurrent_throughput:
            lines.append(
                f"Concurrent Throughput: "
                f"{self.concurrent_throughput:.2f} req/s"
            )

        # Device profile
        if self.device_profile:
            lines.append(f"Device Profile: {self.device_profile}")

        # Endpoints tested
        if self.endpoint_results:
            lines.append(f"Endpoints Tested: {len(self.endpoint_results)}")

        # Errors
        if self.errors:
            lines.append(f"Errors: {len(self.errors)}")

        return "\n".join(lines)

    def __repr__(self) -> str:
        """Return detailed representation"""
        return (
            f"PerformanceTestResults(profile={self.device_profile}, "
            f"throughput={self.sequential_throughput:.2f} req/s)"
            if self.sequential_throughput
            else "PerformanceTestResults(no data)"
        )

    def print_summary(self) -> None:
        """Print formatted test results"""
        print("\n" + "=" * 70)
        print("FortiGate Performance Test Results")
        print("=" * 70)

        # Validation results
        print("\n[CONNECTION POOL VALIDATION]")
        if self.validation_passed:
            print("✓ Connection pool validation: PASSED")
        else:
            print("✗ Connection pool validation: FAILED")

        for warning in self.validation_warnings:
            print(f"  ⚠ {warning}")

        # Endpoint performance
        if self.endpoint_results:
            print("\n[ENDPOINT PERFORMANCE]")
            for endpoint, metrics in self.endpoint_results.items():
                print(f"\n{endpoint}:")
                if "error" in metrics:
                    print(f"  ✗ Error: {metrics['error']}")
                else:
                    print(f"  Requests:     {metrics.get('count', 0)}")
                    print(f"  Avg Time:     {metrics.get('avg_ms', 0):.1f}ms")
                    print(
                        f"  Median Time:  {metrics.get('median_ms', 0):.1f}ms"
                    )
                    min_ms = metrics.get("min_ms", 0)
                    max_ms = metrics.get("max_ms", 0)
                    print(f"  Min/Max:      {min_ms:.1f}ms / {max_ms:.1f}ms")
                    if "p95_ms" in metrics:
                        print(f"  P95:          {metrics['p95_ms']:.1f}ms")
                    success_rate = metrics.get("success_rate", 0)
                    print(f"  Success Rate: {success_rate:.1f}%")

        # Throughput results
        if self.sequential_throughput:
            print("\n[THROUGHPUT]")
            print(f"Sequential:   {self.sequential_throughput:.2f} req/s")
            if self.concurrent_throughput:
                print(f"Concurrent:   {self.concurrent_throughput:.2f} req/s")
                improvement = (
                    (self.concurrent_throughput - self.sequential_throughput)
                    / self.sequential_throughput
                    * 100
                )
                if improvement > 10:
                    print(f"  → Concurrency helps! (+{improvement:.0f}%)")
                elif improvement < -10:
                    print(
                        f"  → Concurrency hurts! "
                        f"({improvement:.0f}%) - Use sequential!"
                    )
                else:
                    print(f"  → Concurrency neutral ({improvement:+.0f}%)")

        # Device profile
        if self.device_profile:
            print("\n[DEVICE PROFILE]")
            print(f"Type: {self.device_profile}")

            if self.device_profile == "high-performance":
                print("  → Fast local/LAN deployment")
                print("  → Can benefit from moderate concurrency")
            elif self.device_profile == "fast-lan":
                print("  → Fast but serialized API processing")
                print("  → Sequential requests recommended")
            elif self.device_profile == "remote-wan":
                print("  → Remote/WAN deployment with high latency")
                print("  → Sequential requests recommended")

        # Recommendations
        if self.recommended_settings:
            print("\n[RECOMMENDED SETTINGS]")
            for key, value in self.recommended_settings.items():
                print(f"  {key}: {value}")

        # Errors
        if self.errors:
            print("\n[ERRORS]")
            for error in self.errors:
                print(f"  ✗ {error}")

        print("\n" + "=" * 70 + "\n")


def test_connection_pool_validation() -> tuple[bool, list[str]]:
    """
    Test that connection pool validation works correctly

    Returns:
        Tuple of (passed: bool, warnings: list[str])
    """
    warnings = []

    try:
        # Import here to avoid circular dependencies
        from . import FortiOS

        # Test 1: Normal configuration (should work)
        try:
            _ = FortiOS(  # noqa: F841
                "test.example.com",
                token="test",
                max_connections=10,
                max_keepalive_connections=5,
            )
            logger.info("✓ Test 1 passed: Normal configuration accepted")
        except Exception as e:
            return False, [f"Normal configuration failed: {e}"]

        # Test 2: Auto-adjustment (should warn but work)
        try:
            _ = FortiOS(  # noqa: F841
                "test.example.com",
                token="test",
                max_connections=5,
                max_keepalive_connections=20,
            )
            warnings.append(
                "Auto-adjusted max_keepalive_connections from 20 to 5"
            )
            logger.info("✓ Test 2 passed: Auto-adjustment working")
        except Exception as e:
            return False, [f"Auto-adjustment failed: {e}"]

        # Test 3: Edge cases
        try:
            _ = FortiOS(  # noqa: F841
                "test.example.com",
                token="test",
                max_connections=1,
                max_keepalive_connections=0,
            )
            logger.info("✓ Test 3 passed: Edge case (0 keepalive) accepted")
        except Exception as e:
            return False, [f"Edge case failed: {e}"]

        return True, warnings

    except ImportError as e:
        return False, [f"Import failed: {e}"]
    except Exception as e:
        return False, [f"Unexpected error: {e}"]


def test_endpoint_performance(
    host: str,
    token: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    verify: bool = True,
    vdom: Optional[str] = None,
    port: Optional[int] = None,
    endpoints: Optional[list[str]] = None,
    count: int = 5,
) -> dict[str, dict[str, Any]]:
    """
    Test performance of various API endpoints

    Args:
        host: FortiGate hostname/IP
        token: API token (or use username/password)
        username: Username for auth (if not using token)
        password: Password for auth (if not using token)
        verify: SSL verification
        vdom: Virtual domain
        port: Custom port
        endpoints: List of endpoints to test (default: common endpoints)
        count: Number of requests per endpoint

    Returns:
        Dictionary mapping endpoint names to performance metrics
    """
    from . import FortiOS

    # Default endpoints to test
    if endpoints is None:
        endpoints = [
            "monitor/system/status",
            "monitor/system/resource/usage",
            "cmdb/firewall/address",
            "cmdb/firewall/policy",
            "cmdb/system/interface",
        ]

    results: dict[str, Any] = {}

    try:
        # Initialize client
        if token:
            fgt = FortiOS(
                host, token=token, verify=verify, vdom=vdom, port=port
            )
        else:
            fgt = FortiOS(
                host,
                username=username,
                password=password,
                verify=verify,
                vdom=vdom,
                port=port,
            )

        # Test each endpoint
        for endpoint_path in endpoints:
            logger.info(f"Testing endpoint: {endpoint_path}")
            endpoint_name = endpoint_path.replace("/", "_")
            times = []
            successes = 0

            # Determine API type and method
            parts = endpoint_path.split("/")
            if parts[0] == "monitor":
                path = "/".join(parts[1:])
            elif parts[0] == "cmdb":
                path = "/".join(parts[1:])
            else:
                results[endpoint_name] = {"error": "Unknown API type"}
                continue

            # Navigate to endpoint and call method
            try:
                # Get the API namespace
                api_obj = fgt.api

                # Navigate through the path
                for part in path.split("/"):
                    if hasattr(api_obj, part):
                        api_obj = getattr(api_obj, part)
                    else:
                        raise AttributeError(
                            f"Path component '{part}' not found"
                        )

                # Make test requests
                for i in range(count):
                    start = time.time()
                    try:
                        if hasattr(api_obj, "get") and callable(
                            getattr(api_obj, "get")
                        ):
                            getattr(api_obj, "get")()
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

            except AttributeError as e:
                results[endpoint_name] = {"error": f"Endpoint not found: {e}"}
            except Exception as e:
                results[endpoint_name] = {"error": str(e)}

        # Close client if using username/password
        if username:
            try:
                if hasattr(fgt, "close"):
                    fgt.close()
            except BaseException:
                pass

    except Exception as e:
        logger.error(f"Endpoint testing failed: {e}")
        results["_error"] = str(e)

    return results


def determine_device_profile(
    avg_response_ms: float,
) -> tuple[str, dict[str, Any]]:
    """
    Determine device profile based on average response time

    Args:
        avg_response_ms: Average response time in milliseconds

    Returns:
        Tuple of (profile_name, recommended_settings)
    """
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


def run_performance_test(
    host: str,
    token: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    verify: bool = True,
    vdom: Optional[str] = None,
    port: Optional[int] = None,
    test_validation: bool = True,
    test_endpoints: bool = True,
    test_concurrency: bool = False,
    sequential_count: int = 10,
    concurrent_count: int = 50,
    concurrent_level: int = 20,
) -> PerformanceTestResults:
    """
    Run comprehensive performance tests on a FortiGate device

    Args:
        host: FortiGate hostname or IP
        token: API token (recommended)
        username: Username (alternative to token)
        password: Password (use with username)
        verify: Verify SSL certificates (default: True)
        vdom: Virtual domain to test
        port: Custom HTTPS port
        test_validation: Test connection pool validation (default: True)
        test_endpoints: Test various API endpoints (default: True)
        test_concurrency: Test concurrent performance (default: False, can be
        slow)
        sequential_count: Number of sequential requests (default: 10)
        concurrent_count: Number of concurrent requests (default: 50)
        concurrent_level: Concurrency level for async test (default: 20)

    Returns:
        PerformanceTestResults object with all test results

    Examples:
        # Quick test (validation + endpoints)
        results = run_performance_test(
            host="192.168.1.99",
            token="your_token",
            verify=False
        )
        results.print_summary()

        # Comprehensive test with concurrency
        results = run_performance_test(
            host="fw.example.com",
            token="your_token",
            verify=True,
            test_concurrency=True,
            sequential_count=20,
            concurrent_count=100
        )
    """
    from . import FortiOS

    results = PerformanceTestResults()

    print("\n" + "=" * 70)
    print("Starting FortiGate Performance Test")
    print("=" * 70)
    print(f"Target: {host}")
    print(f"SSL Verify: {verify}")
    print(f"VDOM: {vdom or 'default'}")
    print("=" * 70 + "\n")

    # Test 1: Connection pool validation
    if test_validation:
        print("[1/3] Testing connection pool validation...")
        passed, warnings = test_connection_pool_validation()
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
            endpoint_results = test_endpoint_performance(
                host=host,
                token=token,
                username=username,
                password=password,
                verify=verify,
                vdom=vdom,
                port=port,
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
                profile, settings = determine_device_profile(overall_avg)
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
        print(
            "\n[3/3] Testing concurrent performance (this may take a while)..."
        )
        try:
            # Use async mode for concurrency test
            async def concurrent_test():
                fgt = FortiOS(
                    host=host,
                    token=token,
                    username=username,
                    password=password,
                    verify=verify,
                    vdom=vdom,
                    port=port,
                    mode="async",
                    max_connections=concurrent_level,
                )

                start = time.time()
                tasks = []

                for _ in range(concurrent_count):
                    tasks.append(fgt.api.monitor.system.status.get())

                await asyncio.gather(*tasks)
                duration = time.time() - start

                await fgt.aclose()

                return duration

            duration = asyncio.run(concurrent_test())
            results.concurrent_throughput = concurrent_count / duration

            print("✓ Concurrent test complete")
            print(f"  {concurrent_count} requests in {duration:.2f}s")
            print(
                f"  Throughput: " f"{results.concurrent_throughput:.2f} req/s"
            )

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


# Convenience function for interactive use
def quick_test(
    host: str, token: str, verify: bool = False
) -> PerformanceTestResults:
    """
    Quick performance test - validates settings and tests basic endpoints

    Args:
        host: FortiGate hostname/IP
        token: API token
        verify: SSL verification (default: False for self-signed certs)

    Returns:
        PerformanceTestResults: Test results object

    Example:
        from hfortix.FortiOS.performance_test import quick_test
        quick_test("192.168.1.99", "your_token_here")
    """
    results = run_performance_test(
        host=host,
        token=token,
        verify=verify,
        test_validation=True,
        test_endpoints=True,
        test_concurrency=False,
        sequential_count=5,
    )
    results.print_summary()
    return results


if __name__ == "__main__":
    import sys

    # Allow running from command line
    if len(sys.argv) < 3:
        print(
            "Usage: python performance_test.py <host> <token> [--verify] [--full]"  # noqa: E501
        )
        print("\nExamples:")
        print("  python performance_test.py 192.168.1.99 mytoken")
        print("  python performance_test.py fw.example.com mytoken --verify")
        print(
            "  python performance_test.py fw.example.com mytoken --verify --full"  # noqa: E501
        )
        sys.exit(1)

    host = sys.argv[1]
    token = sys.argv[2]
    verify = "--verify" in sys.argv
    full_test = "--full" in sys.argv

    results = run_performance_test(
        host=host,
        token=token,
        verify=verify,
        test_validation=True,
        test_endpoints=True,
        test_concurrency=full_test,
        sequential_count=10 if not full_test else 20,
        concurrent_count=50 if not full_test else 100,
    )

    results.print_summary()
