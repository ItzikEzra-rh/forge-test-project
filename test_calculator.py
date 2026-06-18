"""Unit tests for the calculator module."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 5) == 15

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -5) == -15

    def test_add_mixed_signs(self):
        """Test adding numbers with different signs."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2

    def test_add_with_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 7) == 3

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -7) == -3

    def test_subtract_mixed_signs(self):
        """Test subtracting numbers with different signs."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8

    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.3) == pytest.approx(3.2)
        assert subtract(0.3, 0.1) == pytest.approx(0.2)


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(5, 6) == 30

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, -4) == 12
        assert multiply(-5, -6) == 30

    def test_multiply_mixed_signs(self):
        """Test multiplying numbers with different signs."""
        assert multiply(3, -4) == -12
        assert multiply(-5, 6) == -30

    def test_multiply_with_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0

    def test_multiply_with_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == pytest.approx(10.0)
        assert multiply(0.5, 0.2) == pytest.approx(0.1)


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, -2) == 5
        assert divide(-15, -3) == 5

    def test_divide_mixed_signs(self):
        """Test dividing numbers with different signs."""
        assert divide(10, -2) == -5
        assert divide(-15, 3) == -5

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5
        assert divide(-5, 1) == -5

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(5.0, 2.0) == pytest.approx(2.5)
        assert divide(0.6, 0.3) == pytest.approx(2.0)

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)
