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

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n: int) -> int:
    """
    Return the nth prime number.

    Args:
        n (int): The ordinal of the prime to find (1st, 2nd, etc.).

    Returns:
        int: The nth prime number.
    """
    count = 0
    number = 1  # Start from 1 so the first prime (2) is counted

    while count < n:
        number += 1
        if is_prime(number):
            count += 1

    return number


# Example usage
if __name__ == "__main__":
    print(nth_prime(1))   # Output: 2
    print(nth_prime(5))   # Output: 11
    print(nth_prime(10))  # Output: 29
