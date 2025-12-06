import pytest
from src.higher_order import make_multiplier, apply_on_list, filter_custom

def test_make_multiplier():
    times3 = make_multiplier(3)
    assert times3(5) == 15
    assert times3(0) == 0

def test_apply_on_list():
    result = apply_on_list(lambda x: x**2, [1,2,3])
    assert result == [1,4,9]

def test_filter_custom():
    nums = [1,2,3,4,5,6]
    result = filter_custom(nums, lambda x: x%2==0)
    assert result == [2,4,6]
