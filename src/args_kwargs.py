def concat(*parts, sep=" ") -> str:
    """Join multiple strings with a separator."""
    return sep.join(parts)

def update_profile(user: dict, **kwargs) -> dict:
    """Return updated copy of user dict without modifying original."""
    new_user = user.copy()
    new_user.update(kwargs)
    return new_user

def sum_multiples_of(n: int, *multiples) -> int:
    """Return sum of numbers from 1..n that are multiples of any given multiples."""
    total = 0
    for i in range(1, n+1):
        if any(i % m == 0 for m in multiples):
            total += i
    return total
