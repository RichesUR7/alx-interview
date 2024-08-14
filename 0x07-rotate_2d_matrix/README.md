# 0x07. Rotate 2D Matrix

## Description

This project involves implementing a function to rotate a given 2D matrix by 90 degrees clockwise. The rotation should be done in-place, meaning that the transformation must occur within the matrix without using additional space for another matrix.

## Directory Structure

```
0x07-rotate-2d-matrix/
├── main.py          # Main script to execute the rotation function
├── matrix_functions.py # Contains the rotation function implementation
├── README.md        # This file
└── test.py          # Contains test cases for validating the rotation function
```

## Requirements

- Python 3.x

## Functionality

### `rotate_matrix(matrix)`

Rotates the given `matrix` 90 degrees clockwise. The function modifies the matrix in-place.

**Parameters:**

- `matrix` (List[List[int]]): A square matrix (2D list) to be rotated.

**Returns:**

- None: The matrix is rotated in-place.

### Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)
print(matrix)
```

**Output:**

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Running the Tests

To ensure the rotation function works as expected, run the `test.py` script:

```bash
python test.py
```

This script includes various test cases to validate the correctness of the rotation function.

## Usage

To use the `rotate_matrix` function, you need to import it from `matrix_functions.py` in your own scripts. For example:

```python
from matrix_functions import rotate_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)
print(matrix)
```

## Contributing

If you have suggestions or improvements, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
