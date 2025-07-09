from functools import lru_cache
from decorators import measure_performance
from utils import print_metrics
from caching_fibonacci import caching_fibonacci


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
