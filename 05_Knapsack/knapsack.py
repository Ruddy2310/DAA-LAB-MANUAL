"""
Program 5: Implementation of 0/1 Knapsack Problem using Dynamic Programming

Problem:
    Given weights and values of 'n' items, and a knapsack with capacity W,
    find the maximum value that can be put in the knapsack such that the
    sum of weights is less than or equal to W. Each item can be picked at
    most once (0/1 knapsack).

Time Complexity : O(n * W)
Space Complexity: O(n * W)
"""


def knapsack_01(weights, values, capacity):
    """
    Solve 0/1 knapsack using bottom-up dynamic programming.
    Returns (max_value, chosen_items, dp_table)
    """
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # include item
                    dp[i - 1][w]                                    # exclude item
                )
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    # Backtrack to find which items were chosen
    chosen_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i - 1)  # index of item included
            w -= weights[i - 1]
    chosen_items.reverse()

    return max_value, chosen_items, dp


def print_dp_table(dp):
    print("\nDP Table (rows = items considered, cols = capacity):")
    for row in dp:
        print(" ".join(f"{val:4}" for val in row))


def main():
    print("=" * 60)
    print("0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING")
    print("=" * 60)

    try:
        n = int(input("Enter number of items: "))
        weights = list(map(int, input(f"Enter {n} weights separated by space: ").split()))
        values = list(map(int, input(f"Enter {n} values separated by space: ").split()))
        capacity = int(input("Enter knapsack capacity: "))
    except ValueError:
        print("Invalid input.")
        return

    if len(weights) != n or len(values) != n:
        print("Number of weights/values must match number of items.")
        return

    max_value, chosen_items, dp = knapsack_01(weights, values, capacity)

    print(f"\nMaximum value that can be put in knapsack = {max_value}")
    print("Items included (0-indexed):", chosen_items)
    for idx in chosen_items:
        print(f"  Item {idx}: weight = {weights[idx]}, value = {values[idx]}")

    print_dp_table(dp)


if __name__ == "__main__":
    # Example run if user just wants a demo:
    # weights = [1, 3, 4, 5]
    # values  = [1, 4, 5, 7]
    # capacity = 7
    # print(knapsack_01(weights, values, capacity))
    main()
