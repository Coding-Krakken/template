"""Tests for the example module."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from example import add, multiply, is_even, divide, factorial

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 4) == -4
    assert multiply(3, 3) == 9

def test_is_even():
    """Test the is_even function."""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_divide():
    """Test the divide function."""
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_factorial():
    """Test the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120

if __name__ == "__main__":
    test_add()
    test_multiply() 
    test_is_even()
    test_divide()
    test_factorial()
    print("All tests passed!")