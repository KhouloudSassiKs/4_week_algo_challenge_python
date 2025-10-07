def count_min(numbers):
    """
    Count how many times the smallest integer appears in the list.

    Args:
        numbers (list of int): List of integers.

    Returns:
        int: Number of times the smallest integer occurs.
    """
    if not numbers:
        return 0

    smallest = numbers[0]
    count = 0

    for number in numbers:
        if number < smallest:
            smallest = number
            count = 1
        elif number == smallest:
            count += 1

    return count


# Example usage
if __name__ == "__main__":
    example_list = [3, 1, 2, 1, 4, 1]
    print(f"{example_list} -> {count_min(example_list)}")  # Output: 3
