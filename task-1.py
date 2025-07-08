import time
import tracemalloc
from functools import wraps, lru_cache
from typing import Callable, Dict, Any


def measure_performance(func: Callable) -> Callable[..., Dict[str, Any]]:
    """
    Decorator to measure the execution time and memory usage of a function.

    :param func: The function to be measured.

    :return: A wrapper function that returns a dictionary
        containing the function's result, execution time in seconds,
        current memory usage in KB, and peak memory usage in KB.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Dict[str, Any]:
        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        metrics = {
            "result": result,
            "execution_time_sec": end_time - start_time,
            "current_memory_kb": current / 1024,
            "peak_memory_kb": peak / 1024,
        }
        return metrics

    return wrapper


def print_metrics(name: str, metrics: Dict[str, Any]) -> None:
    print(f"{name}:")
    print(f"  Result: {metrics['result']}")
    print(f"  Execution time: {metrics['execution_time_sec'] * 1000:.4f} ms")
    print(f"  Current memory: {metrics['current_memory_kb']:.2f} KB")
    print(f"  Peak memory: {metrics['peak_memory_kb']:.2f} KB")
    print()


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def plain_fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return plain_fib(n - 1) + plain_fib(n - 2)


@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_lru(n - 1) + fib_lru(n - 2)


@measure_performance
def run_cached_fib(n):
    fib = caching_fibonacci()
    return fib(n)


@measure_performance
def run_plain_fib(n):
    return plain_fib(n)


@measure_performance
def run_lru_cache_fib(n):
    return fib_lru(n)


metrics_cached = run_cached_fib(30)
print_metrics("Cached Fibonacci", metrics_cached)
metrics_plain = run_plain_fib(30)
print_metrics("Plain Fibonacci", metrics_plain)
metrics_lru = run_lru_cache_fib(30)
print_metrics("LRU Cache Fibonacci", metrics_lru)
