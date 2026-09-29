"""
Program 6: Implementation of Chain Matrix Multiplication using Dynamic Programming

Problem:
    Given the dimensions of a sequence of matrices, find the most efficient
    way (minimum number of scalar multiplications) to multiply them together.
    We are NOT actually multiplying the matrices, just deciding the order.

    If matrix Ai has dimension p[i-1] x p[i], then the array p[] of size n+1
    represents the dimensions of n matrices.

Time Complexity : O(n^3)
Space Complexity: O(n^2)
"""


def matrix_chain_order(p):
    """
    p: list of dimensions, len(p) = n+1 for n matrices
    Returns (m, s):
        m[i][j] = minimum number of scalar multiplications to compute
                  the product of matrices i..j
        s[i][j] = index at which the optimal split occurs
    """
    n = len(p) - 1  # number of matrices
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # chain_length is the length of the chain of matrices being multiplied
    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    """Recursively build the optimal parenthesization string."""
    if i == j:
        return f"A{i}"
    else:
        k = s[i][j]
        left = print_optimal_parens(s, i, k)
        right = print_optimal_parens(s, k + 1, j)
        return f"({left} x {right})"


def main():
    print("=" * 60)
    print("MATRIX CHAIN MULTIPLICATION - DYNAMIC PROGRAMMING")
    print("=" * 60)

    try:
        n = int(input("Enter number of matrices: "))
        print(f"Enter dimensions as {n + 1} space separated numbers")
        print("(matrix i has dimension p[i-1] x p[i]):")
        p = list(map(int, input().split()))
    except ValueError:
        print("Invalid input.")
        return

    if len(p) != n + 1:
        print(f"Expected {n + 1} dimension values, got {len(p)}.")
        return

    m, s = matrix_chain_order(p)

    print(f"\nMinimum number of scalar multiplications = {m[1][n]}")
    print("Optimal Parenthesization:", print_optimal_parens(s, 1, n))

    print("\nCost Table m[i][j]:")
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(f"{m[i][j] if m[i][j] != 0 else 0:6}")
        print(" ".join(row))


if __name__ == "__main__":
    # Example: p = [30, 35, 15, 5, 10, 20, 25] for 6 matrices
    main()
