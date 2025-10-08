import math

def is_perfect_square(n: int) -> bool:
    """
    Check if a given number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


# Example usage
if __name__ == "__main__":
    test_numbers = [0, 1, 4, 15, 16, 25, 26]
    for num in test_numbers:
        print(f"{num} -> {is_perfect_square(num)}")
