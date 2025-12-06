import time
from functools import wraps

def timeit(fn):
    """Decorator: return tuple (result, elapsed_seconds)."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = round(time.time() - start, 4)
        return result, elapsed
    return wrapper

def type_check(**types):
    """Decorator: check argument types at runtime."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for name, expected_type in types.items():
                if name in kwargs and not isinstance(kwargs[name], expected_type):
                    raise TypeError(f"{name} must be {expected_type}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator
