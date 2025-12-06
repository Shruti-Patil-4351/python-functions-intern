import pytest
from src.builtin_vs_user import safe_len, call_if_callable

def test_safe_len():
    assert safe_len([1,2,3]) == 3
    assert safe_len((1,)) == 1
    assert safe_len({"a":1}) == 1
    assert safe_len("hi") == 2
    with pytest.raises(TypeError):
        safe_len(42)

def test_call_if_callable():
    assert call_if_callable(5) == 5
    assert call_if_callable(lambda x: x+1, 5) == 6
