from typing import Callable

def make_multiplier(m: int) -> Callable[[int], int]:
    """Return function that multiplies input by m."""
    return lambda x: x * m

def apply_on_list(fn, items: list) -> list:
    """Return list after applying fn on each item."""
    return [fn(x) for x in items]

def filter_custom(items: list, predicate) -> list:
    """Return filtered list where predicate(item) is True."""
    return [item for item in items if predicate(item)]
