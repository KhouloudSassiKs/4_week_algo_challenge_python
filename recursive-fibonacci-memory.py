def fibonacci(n, saved={}):
    """
    Compute the nth Fibonacci number using recursion with memoization.

    Fibonacci sequence:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1

    Memoization avoids redundant calculations, making this O(n) time.

    Example:
        fibonacci(10) -> 55
    """
    if n in saved:
        return saved[n]

    if n <= 1:
        saved[n] = n
    else:
        saved[n] = fibonacci(n - 1, saved) + fibonacci(n - 2, saved)

    return saved[n]


if __name__ == "__main__":
    # Example usages
    print(fibonacci(0))   # Output: 0
    print(fibonacci(1))   # Output: 1
    print(fibonacci(5))   # Output: 5
    print(fibonacci(10))  # Output: 55
    print(fibonacci(50))  # Output: 12586269025 (fast even for large n)
