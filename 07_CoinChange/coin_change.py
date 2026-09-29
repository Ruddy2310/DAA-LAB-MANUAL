"""
Program 7: Implementation of Making a Change Problem using Dynamic Programming

Problem:
    Given a set of coin denominations and a target amount, find:
      (a) the minimum number of coins needed to make the amount, and
      (b) the total number of distinct ways to make the amount.

Time Complexity : O(n * amount)  for each sub-problem (n = number of coin types)
Space Complexity: O(amount)  [O(n * amount) if using 2D table for ways-with-table]
"""


def min_coins(coins, amount):
    """
    Minimum number of coins needed to make 'amount'.
    Returns (min_count, coins_used) or (-1, []) if not possible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coin = [-1] * (amount + 1)  # to reconstruct the solution

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                used_coin[a] = coin

    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct which coins were used
    result_coins = []
    a = amount
    while a > 0:
        c = used_coin[a]
        result_coins.append(c)
        a -= c

    return dp[amount], result_coins


def count_ways(coins, amount):
    """
    Total number of distinct ways to make 'amount' using given coins
    (order doesn't matter, unlimited supply of each coin).
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make amount 0: use no coins

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


def main():
    print("=" * 60)
    print("MAKING A CHANGE PROBLEM - DYNAMIC PROGRAMMING")
    print("=" * 60)

    try:
        coins = list(map(int, input("Enter coin denominations separated by space: ").split()))
        amount = int(input("Enter the target amount: "))
    except ValueError:
        print("Invalid input.")
        return

    if amount < 0:
        print("Amount must be non-negative.")
        return

    # Part (a): Minimum number of coins
    min_count, coins_used = min_coins(coins, amount)
    print("\n--- Minimum Coins Required ---")
    if min_count == -1:
        print(f"It is not possible to make amount {amount} with given coins.")
    else:
        print(f"Minimum coins needed = {min_count}")
        print(f"Coins used = {coins_used}")

    # Part (b): Number of distinct ways
    ways = count_ways(coins, amount)
    print("\n--- Total Number of Ways ---")
    print(f"Number of distinct ways to make amount {amount} = {ways}")


if __name__ == "__main__":
    # Example: coins = [1, 2, 5], amount = 11
    main()
