# 0x09. Island Perimeter

## Description

The **Island Perimeter** project is designed to help you practice problem-solving skills related to grid-based algorithms. The task involves computing the perimeter of an island represented in a grid of `0`s and `1`s.

### Problem Statement

You are given a 2D grid map of `1`s (land) and `0`s (water). Your goal is to calculate the perimeter of the island(s) formed by the `1`s. The island is surrounded by water and has a rectangular shape where each cell is connected to its neighboring cells (up, down, left, and right).

### Requirements

Write a function in Python that computes the perimeter of the island. The function should have the following signature:

```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

### Input

- `grid`: A list of lists of integers representing the 2D grid map. Each integer is either `0` (water) or `1` (land). The grid will have at least one row and one column, and each row and column will have a length between `1` and `100`.

### Output

- Returns an integer representing the perimeter of the island.

### Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

### Explanation

In the example grid above, the island has a perimeter of 12 units. The perimeter is calculated by summing the boundaries of the island cells that are adjacent to water or the edge of the grid.

### Notes

- The grid is guaranteed to be rectangular.
- Cells on the border of the grid or adjacent to water contribute to the perimeter.

### Installation

There are no special installation requirements for this project. Simply clone the repository and use the provided Python script to test and run the function.

### Usage

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/0x09-Island-Perimeter.git
   ```

2. Navigate to the project directory:

   ```sh
   cd 0x09-Island-Perimeter
   ```

3. Run the Python script or import the function into your project to use it.

### Contributing

Feel free to contribute to the project by submitting issues or pull requests. Ensure that your contributions adhere to the project's coding standards and include appropriate tests.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize any parts of this `README.md` to better fit your project specifics!
