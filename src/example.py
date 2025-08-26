"""Example module for mutation testing demonstration."""

def add(a, b):
    """Simple addition function for testing."""
    return a + b

def multiply(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b == 0:
        return 0
    return a * b

def is_even(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return True
    else:
        return False

def divide(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result