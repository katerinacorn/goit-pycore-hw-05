from typing import Dict, Any


def print_metrics(name: str, metrics: Dict[str, Any]) -> None:
    print(f"{name}:")
    print(f"  Result: {metrics['result']}")
    print(f"  Execution time: {metrics['execution_time_sec'] * 1000:.4f} ms")
    print(f"  Current memory: {metrics['current_memory_kb']:.2f} KB")
    print(f"  Peak memory: {metrics['peak_memory_kb']:.2f} KB")
    print()
