# 0x08. Making Change

Welcome to the "Making Change" project! This project tackles the classic coin change problem, where the objective is to determine the minimum number of coins required to make up a given amount using a list of coin denominations.

## Project Overview

In this project, you'll be implementing solutions for the coin change problem using two primary approaches:

1. **Greedy Algorithm**: A heuristic approach that selects the largest denomination first and works its way downwards. This method is efficient but may not always provide the optimal solution for all coin sets.

2. **Dynamic Programming (DP)**: A more comprehensive approach that guarantees an optimal solution by breaking down the problem into smaller subproblems and solving them iteratively. This approach is generally applicable to any set of coin denominations.

## Key Concepts

- **Greedy Algorithms**: Understand how to apply greedy strategies and recognize their limitations.
- **Dynamic Programming**: Learn the basics of DP, including overlapping subproblems and optimal substructure.
- **Algorithmic Complexity**: Analyze and optimize the time and space complexity of your solutions.
- **Python Programming**: Use Python effectively to implement and test the algorithms.

## Implementation

### Greedy Algorithm

The greedy algorithm selects the largest denomination possible at each step. This approach is straightforward but may fail to find the optimal solution in some cases. 

**Example Implementation:**

```python
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1
```

### Dynamic Programming

The dynamic programming approach uses a table to keep track of the minimum number of coins needed for each amount up to the target. This approach is more robust and guarantees the optimal solution.

**Example Implementation:**

```python
def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

## Running the Code

To run the provided implementations, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd 0x08-Making-Change
   ```

2. Ensure you have Python 3.x installed.

3. Run the code with sample inputs:
   ```bash
   python greedy_coin_change.py
   python dp_coin_change.py
   ```

4. Modify the input values in the scripts to test different scenarios.

## Resources

- **Python Official Documentation**: [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- **GeeksforGeeks**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-find-minimum-number-coins/)
- **YouTube Tutorials**: Look for videos on Dynamic Programming and the Coin Change Problem for a visual explanation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the details based on your project's specific requirements or additional features you may have included.
