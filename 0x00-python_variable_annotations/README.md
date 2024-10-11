# Python Variable Annotations

This project focuses on using Python 3 type annotations. It contains a series of tasks that demonstrate various aspects of type hinting in Python, from basic to more complex annotations.

## Project Overview

The tasks in this project cover:

1. Basic type annotations for simple functions
2. Complex types including lists, tuples, and callable objects
3. Duck typing and type variables
4. Use of mypy for static type checking

## Key Concepts

- Type hinting in Python 3
- Using `typing` module for complex type annotations
- Understanding and implementing duck typing
- Working with TypeVar for more flexible type hints

## Files and Descriptions

- `0-add.py`: Basic function with float annotations
- `1-concat.py`: String concatenation with annotations
- `2-floor.py`: Floor function with float to int annotation
- `3-to_str.py`: Float to string conversion annotation
- `4-define_variables.py`: Variable definitions with annotations
- `5-sum_list.py`: Sum of float list with annotations
- `6-sum_mixed_list.py`: Sum of mixed integer and float list
- `7-to_kv.py`: Complex function with multiple types
- `8-make_multiplier.py`: Higher-order function with annotations
- `9-element_length.py`: Working with iterable objects
- `100-safe_first_element.py`: Annotating functions with Any type
- `101-safely_get_value.py`: Using TypeVar for annotations
- `102-type_checking.py`: Fixing type annotations to pass mypy checks

## Requirements

- Python 3.7
- mypy

## Usage

Each file contains a separate function implementation. To test, import the function into your Python environment or create a main file to call the function.

Example:
```python
from 0-add import add

result = add(1.11, 2.22)
print(result)
```

For type checking:
```
mypy filename.py
```

## Author

<Victor paul>
