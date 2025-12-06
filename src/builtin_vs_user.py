def safe_len(obj):
    """Return length for list, tuple, dict, str. Raise TypeError otherwise."""
    if isinstance(obj, (list, tuple, dict, str)):
        return len(obj)
    raise TypeError(f"Unsupported type: {type(obj)}")

def call_if_callable(obj, *args, **kwargs):
    """Call obj if callable, else return obj."""
    if callable(obj):
        return obj(*args, **kwargs)
    return obj
