import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from mypackage.greeter import Greeter

def test_say_hello():
    g = Greeter("Alice")
    assert g.say_hello() == "Hello, Alice!"

def test_empty_name():
    g = Greeter("")
    assert g.say_hello() == "Hello, !"

def test_name_with_spaces():
    g = Greeter("  Bob  ")
    assert g.say_hello() == "Hello,   Bob  !"

def test_name_is_not_string():
    with pytest.raises(TypeError) as excinfo:
        Greeter(123)
    assert "Name must be a string" in str(excinfo.value)