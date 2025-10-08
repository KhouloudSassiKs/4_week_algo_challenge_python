import math

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n: int) -> int:
    """
    Find the next prime number after n.

    Args:
        n (int): Starting number.

    Returns:
        int: The next prime greater than n.
    """
    next_number = n + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1


# Example usage
if __name__ == "__main__":
    test_numbers = [3, 8, 14, 29]
    for num in test_numbers:
        print(f"Next prime after {num} is {next_prime(num)}")
