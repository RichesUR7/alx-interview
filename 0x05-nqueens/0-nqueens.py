#!/usr/bin/python3
"""
N Queens problem solver
"""

import sys


class NQueensSolver:
    """
    Class to solve the N Queens problem
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.solutions = []

    def is_safe(self, row: int, col: int) -> bool:
        """
        Check if it's safe to place a queen at board[row][col]
        """
        # Check this row on left side
        if any(self.board[row][i] == 1 for i in range(col)):
            return False

        # Check upper diagonal on left side
        if any(
            self.board[i][j] == 1
            for i, j in zip(range(row, -1, -1), range(col, -1, -1))
        ):
            return False

        # Check lower diagonal on left side
        if any(
            self.board[i][j] == 1
            for i, j in zip(range(row, self.size, 1), range(col, -1, -1))
        ):
            return False

        return True

    def solve_nqueens_util(self, col: int) -> None:
        """
        Utilizes backtracking to solve the N Queens problem
        """
        if col >= self.size:
            self.solutions.append(self._create_solution())
            return

        for row in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve_nqueens_util(col + 1)
                self.board[row][col] = 0

    def _create_solution(self):
        """
        Creates a solution from the current board state
        """
        return [
            [row, col]
            for row in range(self.size)
            for col in range(self.size)
            if self.board[row][col] == 1
        ]

    def solve(self) -> None:
        """
        Solves the N Queens problem and prints all solutions
        """
        self.solve_nqueens_util(0)
        for solution in self.solutions:
            print(solution)


def main() -> None:
    """
    Main function to handle command line arguments and start the solver
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve()


if __name__ == "__main__":
    main()
