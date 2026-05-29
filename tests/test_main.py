# test_max.py
import pytest

def test_max():
    assert max(5, 10) == 10
    assert max(-5, 0) == 0
    assert max(-5, -10) == -5
    assert max(5, 5) == 5
    assert max(-5, -5) == -5
