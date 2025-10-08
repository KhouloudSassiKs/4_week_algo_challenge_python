import math

def get_prime_factors(n: int) -> list[int]:
    """
    Return all unique prime factors of a number.

    Args:
        n (int): The number to factorize.

    Returns:
        list[int]: Sorted list of unique prime factors of n.
    """
    output = []

    # Factor out 2
    while n % 2 == 0:
        if 2 not in output:
            output.append(2)
        n //= 2

    # Factor out odd numbers from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in output:
                output.append(i)
            n //= i

    # If remaining n is a prime number greater than 2
    if n > 2 and n not in output:
        output.append(n)

    return output


# Example usage
if __name__ == "__main__":
    test_numbers = [18, 28, 45, 97, 100]
    for num in test_numbers:
        print(f"Prime factors of {num}: {get_prime_factors(num)}")
