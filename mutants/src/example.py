"""Example module for mutation testing demonstration."""
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

def x_add__mutmut_orig(a, b):
    """Simple addition function for testing."""
    return a + b

def x_add__mutmut_1(a, b):
    """Simple addition function for testing."""
    return a - b

x_add__mutmut_mutants : ClassVar[MutantDict] = {
'x_add__mutmut_1': x_add__mutmut_1
}

def add(*args, **kwargs):
    result = _mutmut_trampoline(x_add__mutmut_orig, x_add__mutmut_mutants, args, kwargs)
    return result 

add.__signature__ = _mutmut_signature(x_add__mutmut_orig)
x_add__mutmut_orig.__name__ = 'x_add'

def x_multiply__mutmut_orig(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b == 0:
        return 0
    return a * b

def x_multiply__mutmut_1(a, b):
    """Simple multiplication function for testing."""
    if a == 0 and b == 0:
        return 0
    return a * b

def x_multiply__mutmut_2(a, b):
    """Simple multiplication function for testing."""
    if a != 0 or b == 0:
        return 0
    return a * b

def x_multiply__mutmut_3(a, b):
    """Simple multiplication function for testing."""
    if a == 1 or b == 0:
        return 0
    return a * b

def x_multiply__mutmut_4(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b != 0:
        return 0
    return a * b

def x_multiply__mutmut_5(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b == 1:
        return 0
    return a * b

def x_multiply__mutmut_6(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b == 0:
        return 1
    return a * b

def x_multiply__mutmut_7(a, b):
    """Simple multiplication function for testing."""
    if a == 0 or b == 0:
        return 0
    return a / b

x_multiply__mutmut_mutants : ClassVar[MutantDict] = {
'x_multiply__mutmut_1': x_multiply__mutmut_1, 
    'x_multiply__mutmut_2': x_multiply__mutmut_2, 
    'x_multiply__mutmut_3': x_multiply__mutmut_3, 
    'x_multiply__mutmut_4': x_multiply__mutmut_4, 
    'x_multiply__mutmut_5': x_multiply__mutmut_5, 
    'x_multiply__mutmut_6': x_multiply__mutmut_6, 
    'x_multiply__mutmut_7': x_multiply__mutmut_7
}

def multiply(*args, **kwargs):
    result = _mutmut_trampoline(x_multiply__mutmut_orig, x_multiply__mutmut_mutants, args, kwargs)
    return result 

multiply.__signature__ = _mutmut_signature(x_multiply__mutmut_orig)
x_multiply__mutmut_orig.__name__ = 'x_multiply'

def x_is_even__mutmut_orig(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return True
    else:
        return False

def x_is_even__mutmut_1(n):
    """Check if a number is even."""
    if n / 2 == 0:
        return True
    else:
        return False

def x_is_even__mutmut_2(n):
    """Check if a number is even."""
    if n % 3 == 0:
        return True
    else:
        return False

def x_is_even__mutmut_3(n):
    """Check if a number is even."""
    if n % 2 != 0:
        return True
    else:
        return False

def x_is_even__mutmut_4(n):
    """Check if a number is even."""
    if n % 2 == 1:
        return True
    else:
        return False

def x_is_even__mutmut_5(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return False
    else:
        return False

def x_is_even__mutmut_6(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return True
    else:
        return True

x_is_even__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_even__mutmut_1': x_is_even__mutmut_1, 
    'x_is_even__mutmut_2': x_is_even__mutmut_2, 
    'x_is_even__mutmut_3': x_is_even__mutmut_3, 
    'x_is_even__mutmut_4': x_is_even__mutmut_4, 
    'x_is_even__mutmut_5': x_is_even__mutmut_5, 
    'x_is_even__mutmut_6': x_is_even__mutmut_6
}

def is_even(*args, **kwargs):
    result = _mutmut_trampoline(x_is_even__mutmut_orig, x_is_even__mutmut_mutants, args, kwargs)
    return result 

is_even.__signature__ = _mutmut_signature(x_is_even__mutmut_orig)
x_is_even__mutmut_orig.__name__ = 'x_is_even'

def x_divide__mutmut_orig(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def x_divide__mutmut_1(a, b):
    """Divide a by b with zero check."""
    if b != 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def x_divide__mutmut_2(a, b):
    """Divide a by b with zero check."""
    if b == 1:
        raise ValueError("Cannot divide by zero")
    return a / b

def x_divide__mutmut_3(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError(None)
    return a / b

def x_divide__mutmut_4(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("XXCannot divide by zeroXX")
    return a / b

def x_divide__mutmut_5(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

def x_divide__mutmut_6(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("CANNOT DIVIDE BY ZERO")
    return a / b

def x_divide__mutmut_7(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b

x_divide__mutmut_mutants : ClassVar[MutantDict] = {
'x_divide__mutmut_1': x_divide__mutmut_1, 
    'x_divide__mutmut_2': x_divide__mutmut_2, 
    'x_divide__mutmut_3': x_divide__mutmut_3, 
    'x_divide__mutmut_4': x_divide__mutmut_4, 
    'x_divide__mutmut_5': x_divide__mutmut_5, 
    'x_divide__mutmut_6': x_divide__mutmut_6, 
    'x_divide__mutmut_7': x_divide__mutmut_7
}

def divide(*args, **kwargs):
    result = _mutmut_trampoline(x_divide__mutmut_orig, x_divide__mutmut_mutants, args, kwargs)
    return result 

divide.__signature__ = _mutmut_signature(x_divide__mutmut_orig)
x_divide__mutmut_orig.__name__ = 'x_divide'

def x_factorial__mutmut_orig(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_1(n):
    """Calculate factorial of n."""
    if n < 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_2(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_3(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 2
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_4(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = None
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_5(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 2
    for i in range(1, n + 1):
        result *= i
    return result

def x_factorial__mutmut_6(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(None, n + 1):
        result *= i
    return result

def x_factorial__mutmut_7(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, None):
        result *= i
    return result

def x_factorial__mutmut_8(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(n + 1):
        result *= i
    return result

def x_factorial__mutmut_9(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, ):
        result *= i
    return result

def x_factorial__mutmut_10(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def x_factorial__mutmut_11(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n - 1):
        result *= i
    return result

def x_factorial__mutmut_12(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 2):
        result *= i
    return result

def x_factorial__mutmut_13(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = i
    return result

def x_factorial__mutmut_14(n):
    """Calculate factorial of n."""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result /= i
    return result

x_factorial__mutmut_mutants : ClassVar[MutantDict] = {
'x_factorial__mutmut_1': x_factorial__mutmut_1, 
    'x_factorial__mutmut_2': x_factorial__mutmut_2, 
    'x_factorial__mutmut_3': x_factorial__mutmut_3, 
    'x_factorial__mutmut_4': x_factorial__mutmut_4, 
    'x_factorial__mutmut_5': x_factorial__mutmut_5, 
    'x_factorial__mutmut_6': x_factorial__mutmut_6, 
    'x_factorial__mutmut_7': x_factorial__mutmut_7, 
    'x_factorial__mutmut_8': x_factorial__mutmut_8, 
    'x_factorial__mutmut_9': x_factorial__mutmut_9, 
    'x_factorial__mutmut_10': x_factorial__mutmut_10, 
    'x_factorial__mutmut_11': x_factorial__mutmut_11, 
    'x_factorial__mutmut_12': x_factorial__mutmut_12, 
    'x_factorial__mutmut_13': x_factorial__mutmut_13, 
    'x_factorial__mutmut_14': x_factorial__mutmut_14
}

def factorial(*args, **kwargs):
    result = _mutmut_trampoline(x_factorial__mutmut_orig, x_factorial__mutmut_mutants, args, kwargs)
    return result 

factorial.__signature__ = _mutmut_signature(x_factorial__mutmut_orig)
x_factorial__mutmut_orig.__name__ = 'x_factorial'