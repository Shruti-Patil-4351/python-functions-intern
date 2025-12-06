import pytest
from src.recursion import fibonacci, fibonacci_memo, flatten

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_memo():
    assert fibonacci_memo(0) == 0
    assert fibonacci_memo(10) == 55
    # Check performance: n=30
    assert fibonacci_memo(30) == 832040

def test_flatten():
    assert flatten([1, [2, [3,4]], 5]) == [1,2,3,4,5]
    assert flatten([]) == []
    assert flatten([1,[[]],2]) == [1,2]
