import pytest

from greet import greet


def test_greet_returns_greeting():
    assert greet("World") == "Hello, World!"


def test_greet_rejects_blank_name():
    with pytest.raises(ValueError):
        greet("   ")
