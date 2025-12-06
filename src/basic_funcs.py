def greet(name: str) -> str:
    """Return greeting for given name."""
    return f"Hello, {name}!"

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Return factorial of n iteratively. Raise ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
