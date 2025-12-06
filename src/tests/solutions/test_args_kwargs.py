import pytest
from src.args_kwargs import concat, update_profile, sum_multiples_of

def test_concat():
    assert concat("one","two") == "one two"
    assert concat("one","two", sep="-") == "one-two"
    assert concat() == ""

def test_update_profile():
    user = {"name": "Alice", "age": 25}
    updated = update_profile(user, age=30, city="NY")
    assert updated["age"] == 30
    assert updated["city"] == "NY"
    assert user["age"] == 25  # original not mutated

def test_sum_multiples_of():
    assert sum_multiples_of(10, 3,5) == 33
    assert sum_multiples_of(5, 2) == 6  # 2 + 4
    assert sum_multiples_of(0, 1) == 0
