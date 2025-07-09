import time
import tracemalloc
from functools import wraps
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
