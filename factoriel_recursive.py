def get_sum(n):
    """
    Recursively compute the sum of all integers from 1 to n (inclusive).
    Example: get_sum(4) -> 1 + 2 + 3 + 4 = 10
    """
    if n <= 1:
        return n
    return n + get_sum(n - 1)


if __name__ == "__main__":
    # Example usages
    print(get_sum(1))   # Output: 1
    print(get_sum(4))   # Output: 10  (1+2+3+4)
    print(get_sum(10))  # Output: 55
