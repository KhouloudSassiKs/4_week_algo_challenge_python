import math

def are_coprime(a: int, b: int) -> bool:
    """
    Check if two numbers are coprime (i.e., their greatest common divisor is 1).

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        bool: True if a and b are coprime, False otherwise.
    """
    smaller = min(a, b)
    for i in range(2, smaller + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


# Example usage
if __name__ == "__main__":
    print(are_coprime(15, 28))  # True
    print(are_coprime(12, 18))  # False
