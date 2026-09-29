"""
Program 4: Implementation and Time Analysis of Factorial Program
using Iterative and Recursive Method

Time Complexity:
    Iterative Method : O(n)
    Recursive Method  : O(n)   (n recursive calls, each O(1) work)
Space Complexity:
    Iterative Method : O(1)
    Recursive Method  : O(n)   (recursion call stack)
"""

import time
import sys

sys.setrecursionlimit(10000)


def factorial_iterative(n):
    """Compute n! iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Compute n! recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def measure_time(func, n):
    """Run func(n) and return (result, time_taken_in_seconds)."""
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


def main():
    print("=" * 60)
    print("FACTORIAL: ITERATIVE vs RECURSIVE - TIME ANALYSIS")
    print("=" * 60)

    try:
        n = int(input("Enter a number to find its factorial: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    iter_result, iter_time = measure_time(factorial_iterative, n)
    rec_result, rec_time = measure_time(factorial_recursive, n)

    print(f"\nInput n = {n}")
    print("-" * 60)
    print(f"Iterative Result : {iter_result}")
    print(f"Recursive Result : {rec_result}")
    print("-" * 60)
    print(f"Iterative Time   : {iter_time:.8f} seconds")
    print(f"Recursive Time   : {rec_time:.8f} seconds")
    print("-" * 60)

    # Comparison table for a range of values (average of multiple runs)
    print("\nComparison Table (average of 1000 runs each):")
    print(f"{'n':>5} | {'Iterative (s)':>15} | {'Recursive (s)':>15}")
    print("-" * 45)

    test_values = [5, 10, 50, 100, 500, 900]
    runs = 1000
    for val in test_values:
        it_total = 0.0
        rc_total = 0.0
        for _ in range(runs):
            _, t1 = measure_time(factorial_iterative, val)
            _, t2 = measure_time(factorial_recursive, val)
            it_total += t1
            rc_total += t2
        print(f"{val:>5} | {it_total / runs:>15.8f} | {rc_total / runs:>15.8f}")

    print("\nObservation:")
    print("- Both methods have O(n) time complexity.")
    print("- Recursive method uses extra O(n) space due to the call stack,")
    print("  and has additional overhead from function calls, making it")
    print("  slightly slower than the iterative method in practice.")
    print("- Iterative method uses O(1) space and is generally preferred")
    print("  for large n to avoid stack overflow.")


if __name__ == "__main__":
    main()
