# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),           # Test adding zeros
        (1000000, 2000000, 3000000),  # Test adding large integers
        (0.1, 0.2, pytest.approx(0.3)),  # Test floating point precision
        (0, 5, 5),           # Test identity: adding zero to a number
        (-5, 5, 0),          # Test additive inverse: opposite numbers sum to zero
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
        "add_large_integers",
        "add_floating_point_precision",
        "add_identity_zero",
        "add_inverse_to_zero",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


def test_add_commutativity() -> None:
    """
    Test that addition is commutative: add(a, b) == add(b, a).
    """
    assert add(7, 3) == add(3, 7), "Addition should be commutative"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),           # Test subtracting zeros
        (10, 10, 0),         # Test subtracting equal numbers yields zero
        (0, 5, -5),          # Test subtracting from zero yields negative
        (1000000, 999999, 1),  # Test subtracting large numbers
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
        "subtract_equal_numbers",
        "subtract_from_zero",
        "subtract_large_numbers",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


def test_subtract_self_is_zero() -> None:
    """
    Test that subtracting a number from itself always yields zero.
    """
    assert subtract(42, 42) == 0, "Subtracting a number from itself should return 0"
    assert subtract(-7.5, -7.5) == 0, "Subtracting a negative number from itself should return 0"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),           # Test multiplying zero with a positive integer
        (1, 99, 99),         # Test multiplicative identity: multiplying by 1
        (-1, -1, 1),         # Test negative times negative is positive
        (0.5, 0.5, 0.25),    # Test multiplying fractions
        (1000, 1000, 1000000),  # Test multiplying large numbers
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
        "multiply_identity_one",
        "multiply_two_negatives",
        "multiply_fractions",
        "multiply_large_numbers",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


def test_multiply_commutativity() -> None:
    """
    Test that multiplication is commutative: multiply(a, b) == multiply(b, a).
    """
    assert multiply(7, 3) == multiply(3, 7), "Multiplication should be commutative"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),           # Test dividing zero by a positive integer
        (7, 2, 3.5),           # Test division that produces a non-integer result
        (1, 3, pytest.approx(0.333333, rel=1e-4)),  # Test repeating decimal
        (100, 1, 100.0),       # Test dividing by 1 returns the dividend
        (-6, -3, 2.0),         # Test negative divided by negative is positive
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
        "divide_non_integer_result",
        "divide_repeating_decimal",
        "divide_by_one",
        "divide_negative_by_negative",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message.
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


def test_divide_by_zero_with_float_zero() -> None:
    """
    Test that dividing by 0.0 (float zero) also raises a ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0.0)
    
    assert "Cannot divide by zero!" in str(excinfo.value)


# ---------------------------------------------
# Return Type Tests
# ---------------------------------------------

def test_divide_returns_float() -> None:
    """
    Test that the divide function always returns a float.
    """
    result = divide(6, 3)
    assert isinstance(result, float), f"Expected float, got {type(result)}"


def test_add_returns_number() -> None:
    """
    Test that add returns the correct numeric type.
    """
    assert isinstance(add(2, 3), int), "Adding two ints should return int"
    assert isinstance(add(2.0, 3.0), float), "Adding two floats should return float"
