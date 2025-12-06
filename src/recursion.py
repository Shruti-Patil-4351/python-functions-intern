from functools import lru_cache

def fibonacci(n: int) -> int:
    """Return nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """Return nth Fibonacci number with memoization for efficiency."""
    if n in (0, 1):
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

def flatten(nested_list: list) -> list:
    """Recursively flatten a nested list of arbitrary depth."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
