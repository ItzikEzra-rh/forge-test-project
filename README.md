# Forge Test Project

Sandbox repo for testing Forge SDLC orchestrator.

## Calculator Module

A simple Python calculator module providing basic arithmetic operations.

### Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling)

### Installation

```bash
# Install with test dependencies
pip install -e ".[test]"
```

### Usage

```python
from calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Subtraction
result = subtract(10, 4)
print(f"10 - 4 = {result}")  # Output: 10 - 4 = 6

# Multiplication
result = multiply(6, 7)
print(f"6 * 7 = {result}")  # Output: 6 * 7 = 42

# Division
result = divide(15, 3)
print(f"15 / 3 = {result}")  # Output: 15 / 3 = 5.0

# Division by zero handling
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=calculator
```

### Development

The module follows PEP 8 style guidelines and includes comprehensive unit tests.
