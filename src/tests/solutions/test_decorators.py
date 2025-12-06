def type_check(**type_hints):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for name, expected_type in type_hints.items():
                if name in kwargs:
                    if not isinstance(kwargs[name], expected_type):
                        raise TypeError(f"{name} must be {expected_type.__name__}")
            # If you want, also check args by matching function signature
            return func(*args, **kwargs)
        return wrapper
    return decorator
