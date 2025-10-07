def solution(nums):
    """
    Count the number of even and odd integers in a list.

    Args:
        nums (list of int): List of integers to check.

    Returns:
        tuple: (even_count, odd_count)
    """
    even_count = 0
    odd_count = 0

    for number in nums:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)


# Example usage
if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5, 6]
    print(f"{example_list} -> {solution(example_list)}")
